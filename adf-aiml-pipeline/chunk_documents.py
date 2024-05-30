import argparse
import dataclasses
import json
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

from data_utils import chunk_directory

def get_document_intelligence_client(config):
    print("Setting up Document Intelligence client...")
    key = os.environ.get("DOCUMENT_INTELLIGENCE_KEY")
    
    if not key:
        print("No Document Intelligence key provided in config file. Document Intelligence client will not be set up.")
        return None

    endpoint = config.get("document_intelligence_endpoint")
    if not endpoint:
        print("No endpoint provided in config file. Document Intelligence client will not be set up.")
        return None
    
    try:
        os.environ["FORM_RECOGNIZER_ENDPOINT"] =endpoint
        os.environ["FORM_RECOGNIZER_KEY"] = key
        document_intelligence_credential = AzureKeyCredential(key)

        document_intelligence_client = DocumentAnalysisClient(endpoint, document_intelligence_credential)
        print("Document Intelligence client set up.")
        return document_intelligence_client
    except Exception as e:
        print("Error setting up Document Intelligence client: {}".format(e))
        return None

def valid_range(n):
    n = int(n)
    if n < 1 or n > 32:
        raise argparse.ArgumentTypeError("njobs must be an Integer between 1 and 32.")
    return n

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data_path", type=str, required=True)
    parser.add_argument("--output_file_path", type=str, required=True)
    parser.add_argument("--config_file", type=str, required=True)
    parser.add_argument("--njobs", type=valid_range, default=4, help="Number of jobs to run (between 1 and 32). Default=4")

    try:
        args = parser.parse_args()

        with open(args.config_file) as f:
            config = json.load(f)

        if type(config) is not list:
            config = [config]
        
        for index_config in config:
            # Optional client for cracking documents
            document_intelligence_client = get_document_intelligence_client(index_config)

            # Crack and chunk documents
            print("Cracking and chunking documents...")

            chunking_result = chunk_directory(
                                directory_path=args.input_data_path, 
                                num_tokens=index_config.get("chunk_size", 1024),
                                token_overlap=index_config.get("token_overlap", 128),
                                form_recognizer_client=document_intelligence_client,
                                use_layout=bool(index_config.get("use_layout", False)),
                                njobs=args.njobs)
            
            print(f"Processed {chunking_result.total_files} files")
            print(f"Unsupported formats: {chunking_result.num_unsupported_format_files} files")
            print(f"Files with errors: {chunking_result.num_files_with_errors} files")
            print(f"Found {len(chunking_result.chunks)} chunks")

            print("Writing chunking result to {}...".format(args.output_file_path))
            with open(args.output_file_path, "w") as f:
                for chunk in chunking_result.chunks:
                    id = 0
                    d = dataclasses.asdict(chunk)
                    # add id to documents
                    d.update({"id": str(id)})
                    f.write(json.dumps(d) + "\n")
                    id += 1
            print("Chunking result written to {}.".format(args.output_file_path))
    except Exception as e:
            print("Error during chunking: {}".format(e))