import argparse
from asyncio import sleep
import dataclasses
import json
import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from data_preparation import create_or_update_search_index, upload_documents_to_index


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data_path", type=str, required=True)
    parser.add_argument("--config_file", type=str, required=True)

    args = parser.parse_args()

    with open(args.config_file) as f:
        config = json.load(f)

    if type(config) is not list:
        config = [config]
    
    for index_config in config:

        # Get Search Key
        search_key =  os.environ.get("SEARCH_KEY")
        if not search_key:
            raise ValueError("No search key provided in env file. Index will not be created.")

        search_service_name = index_config.get("search_service_name")
        if not search_service_name:
            raise ValueError("No search service name provided in config file. Index will not be created.")

        # Create Index
        print("Creating index...")
        index_name = index_config.get("index_name", "default-index")
        create_or_update_search_index(
            service_name=search_service_name,
            index_name=index_name,
            vector_config_name="default" if "embedding_endpoint" in index_config else None,
            admin_key=search_key
        )

        print(f"Index {index_name} created.")

        # Upload Documents
        print("Uploading documents...")
        with open(args.input_data_path) as input_file:
            documents = [json.loads(line) for line in input_file]
        
        print('search key:', search_key)
        
        upload_documents_to_index(search_service_name, "", "", index_name, documents, admin_key=search_key)
        print("Done.")

