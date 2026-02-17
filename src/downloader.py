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
        self.url = new_url
        
    def upload_file(self) -> bool:
        return self.download_file("config.json", self.url)
        
        
    def load_config(self) -> ProgramFiles:
        with open("config.json", 'r', encoding="utf8") as file:
            data = file.read()
        program_files: ProgramFiles = ProgramFiles.model_validate_json(data)
        return program_files
        
        
    def download_file(self, path: str, url: str):
        try:
            with httpx.stream("GET", url, follow_redirects=True, verify=False) as response:
                if response.status_code != 200:
                    return False

                with open(path, "wb") as file:
                    for chunk in response.iter_bytes(chunk_size=8192):
                        file.write(chunk)
                
                return True
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return False
    