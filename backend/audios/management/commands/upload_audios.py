from django.core.management.base import BaseCommand
from ...blob_storage import blob_storage_handler
from ...models import Audio
import os 
class Command(BaseCommand):
    help = 'Uploads files'

    def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='The folder containing the audios to be uploaded')


    def handle(self, *args, **kwargs):
        local_folder_path = kwargs['folder_path']

        for root, _, files in os.walk(local_folder_path):
                for f in files:
                    print(f)
                    local_file_path = os.path.join(root, f)
                    blob_name = blob_storage_handler.upload_file(local_folder_path,local_file_path)
                    if blob_name:
                        name = '.'.join(blob_name.split('.')[:-1])
                        Audio.objects.create(name=name,azure_blob_name= blob_name)
                    



