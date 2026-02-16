import os
import httpx

from .config import default_file
from .models import ProgramFile, ProgramFiles

class Downloader(object):
    def __init__(self) -> None:
        self.url = default_file
        
    def init_dir(self):
        os.makedirs("downloaded", exist_ok=True)
        os.makedirs("icons", exist_ok=True)
        os.makedirs("service_files", exist_ok=True)
        
    def set_url(self, new_url: str):
        self.url = default_file
        
    def upload_file(self) -> bool:
        return self.download_file("service_files\\programs.json", self.url)
        
        
    def load_config(self) -> ProgramFiles:
        with open("service_files\\programs.json", 'r', encoding="utf8") as file:
            data = file.read()
        program_files: ProgramFiles = ProgramFiles.model_validate_json(data)
        return program_files
        
        
    def download_file(self, path: str, url: str):
        try:
            response = httpx.get(url)
            with open(path, 'bw') as file:
                file.write(response.content)
            return True
        except Exception as e:
            print(e)
            return False
    