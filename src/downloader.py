import os
import httpx

from .config import default_file
from .models import ProgramFile, ProgramFiles

class Downloader(object):
    def __init__(self) -> None:
        self.url = default_file
        
    def init_dir(self):
        os.mkdir("downloaded")
        os.mkdir("icons")
        os.mkdir("service_files")
        
    def set_url(self, new_url: str):
        self.url = default_file
        
    def upload_file(self) -> bool:
        try:
            response = httpx.get(self.url)
            with open("service_files\\programs.json", 'w', encoding="utf8") as file:
                file.write(response.text)
            return True
        except:
            return False
        
        
    def load_file(self) -> ProgramFiles:
        with open("service_files\\programs.json", 'w', encoding="utf8") as file:
            data = file.read()
        program_files: ProgramFiles = ProgramFiles.model_validate_json(data)
        return program_files
        
    