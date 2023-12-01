# from azure.storage.blob import BlobServiceClient
import os
import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, generate_blob_sas, BlobSasPermissions
from dotenv import load_dotenv
import logging


load_dotenv()


class BlobStorageHandler():
    account_name = os.getenv("STORAGE_ACCOUNT_NAME")
    account_key =  os.getenv("STORAGE_ACCOUNT_KEY")
    container_name =os.getenv("CONTAINER_NAME")
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
        
    def upload_file(self,local_folder_path, local_file_path):
                    # Get the local path and name of the file
                    blob_name = os.path.relpath(local_file_path, local_folder_path).replace("\\", "/")
                    # Create a BlobClient object for the file
                    blob_client = self.container_client.get_blob_client(blob_name)
                    # Upload the file to Azure Blob Storage     
                    with open(local_file_path, "rb") as data:
                        try:
                            blob_client.upload_blob(data, overwrite=False)
                            logging.info(f"Blob {blob_name} uploaded successfully")
                            return blob_name
                        except:
                            logging.error(f" Cloud not upload blob {blob_name}")

    def create_service_sas_blob(self,blob_name):
        # Create a SAS token that's valid for one day, as an example
        blob_client = self.container_client.get_blob_client(blob_name)
        if blob_client.exists():
            start_time = datetime.datetime.now(datetime.timezone.utc)
        
            expiry_time = start_time + datetime.timedelta(days=1)
            
            sas_token = generate_blob_sas(
                account_name=blob_client.account_name,
                container_name=blob_client.container_name,
                blob_name=blob_client.blob_name,
                account_key=self.account_key,
                permission=BlobSasPermissions(read=True),
                expiry=expiry_time,
                start=start_time
            )
            blob_url = blob_client.url
            sas_url = f"{blob_client.url}?{sas_token}"
            return sas_url
        else:
            raise Exception("This blob does not exist")

blob_storage_handler = BlobStorageHandler()


# Create a ContainerClient object

# Loop through all the local folders



# def get_blob_names():
#     blob_list = container_client.list_blobs()
    
#     blob_names = [blob.name for blob in blob_list]
#     print(blob_names)
#     return blob_names
#     # print(blob_list)



