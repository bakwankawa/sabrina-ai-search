from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
import os, dotenv

dotenv.load_dotenv()

class AzureBlobDownloader:
    def __init__(self, storage_api_key, storage_account_name, container_name, download_folder_path):
        self.storage_api_key = storage_api_key
        self.storage_account_name = storage_account_name
        self.container_name = container_name
        self.download_folder_path = download_folder_path

    def get_blob_service_client_token_credential(self):
        # Replace <storage-account-name> with your actual storage account name
        account_url = f"https://{self.storage_account_name}.blob.core.windows.net"
        shared_access_key = self.storage_api_key
        credential = shared_access_key

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(account_url, credential=credential)

        return blob_service_client

    def download_blob_to_file(self, blob_service_client: BlobServiceClient, blob_name):
        # Ensure the download folder exists
        os.makedirs(self.download_folder_path, exist_ok=True)
        
        blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=blob_name)
        local_download_path = os.path.join(self.download_folder_path, blob_name)
        
        with open(file=local_download_path, mode="wb") as blob_file:
            download_stream = blob_client.download_blob()
            blob_file.write(download_stream.readall())
            print(f"Downloaded blob to {local_download_path}")

    def download_all_blobs(self):
        # Get the BlobServiceClient using Azure identity
        blob_service_client = self.get_blob_service_client_token_credential()

        # List all blobs in the container and download them
        container_client = blob_service_client.get_container_client(self.container_name)
        blobs_list = container_client.list_blobs()
        for blob in blobs_list:
            self.download_blob_to_file(blob_service_client, blob.name)

# Usage
if __name__ == "__main__":
    # Replace these values with your Azure Storage account name, container name, and local download folder path
    storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")
    container_name = os.getenv("BLOB_CONTAINER_NAME_PROD")
    storage_api_key = os.getenv("STORAGE_API_KEY")
    download_folder_path = "./prod-knowledge"

    downloader = AzureBlobDownloader(storage_api_key, storage_account_name, container_name, download_folder_path)
    downloader.download_all_blobs()
