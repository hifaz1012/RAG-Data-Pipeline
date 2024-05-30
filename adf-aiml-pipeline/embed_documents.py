import argparse
import json

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from data_utils import get_embedding
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data_path", type=str, required=True)
    parser.add_argument("--output_file_path", type=str, required=True)
    parser.add_argument("--config_file", type=str, required=True)

    args = parser.parse_args()

    with open(args.config_file) as f:
        config = json.load(f)

    if type(config) is not list:
        config = [config]
    
    for index_config in config:

        # Get Embedding key
        embedding_key = os.environ.get("EMBEDDING_KEY")
        if not embedding_key:
            raise ValueError("No embedding key secret key in env file. Embeddings will not be generated.")
       
        embedding_endpoint = index_config.get("embedding_endpoint")
        if not embedding_endpoint:
            raise ValueError("No embedding endpoint provided in config file. Embeddings will not be generated.")

        # Embed documents
        print("Generating embeddings...")
        with open(args.input_data_path) as input_file, open(args.output_file_path, "w") as output_file:
            for line in input_file:
                document = json.loads(line)
                try:
                    embedding = get_embedding(document["content"], embedding_endpoint,  embedding_key)
                    document["contentVector"] = embedding
                except:
                    print("Error generating embedding")
                
                output_file.write(json.dumps(document) + "\n")

        print("Embeddings generated and saved to {}.".format(args.output_file_path))

