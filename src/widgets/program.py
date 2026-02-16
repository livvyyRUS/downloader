import httpx
import subprocess
from pathlib import Path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt

from widgets.program import Ui_Program
from src.downloader import Downloader


class UI_Program(QWidget):
    def __init__(self, name: str, icon: str, url: str) -> None:
        super().__init__()
        self.ui = Ui_Program()
        self.ui.setupUi(self)
        self.name = name
        self.icon = icon
        self.url = url 
        self.downloader = Downloader()
        self.self_ui()
        
    def self_ui(self):
        self.ui.install_button.clicked.connect(self.install_action)
        self.ui.download_button.clicked.connect(self.download_action)
        self.ui.download_and_install_button.clicked.connect(self.download_and_install_action)
        self.ui.label.setText(self.name)
        self.ui.progress_bar.hide()
        
        
        self.set_icon()
        
    def set_icon(self):
        self.downloader.init_dir()
        path = f"icons\\downloaded\\{self.name}.png"
        answer = self.downloader.download_file(path, self.icon)
        
        if answer:
            pixmap = QPixmap(path)
            if not pixmap.isNull():
                # Масштабируем под размер label
                scaled_pixmap = pixmap.scaled(
                    self.ui.icon_label.size(), 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.ui.icon_label.setPixmap(scaled_pixmap)
        
        
    def download_action(self):
        self.ui.progress_bar.show()
        self.ui.status_label.setText("Загрузка...")
        try:
            with httpx.stream("GET", self.url, follow_redirects=True) as response:
                # Проверяем, прислал ли сервер размер файла
                total_size = int(response.headers.get("Content-Length", 0))
                
                if response.status_code != 200:
                    return False

                with open(f"downloaded\\{self.name}.exe", "wb") as file:
                    downloaded = 0
                    for chunk in response.iter_bytes(chunk_size=8192):
                        file.write(chunk)
                        downloaded += len(chunk)
                        
                        if total_size > 0:
                            # Считаем процент
                            progress = int((downloaded / total_size) * 100)
                            self.ui.progress_bar.setValue(progress)
                            
                            # Принудительно обновляем интерфейс, чтобы он не "зависал"
                            QApplication.processEvents() 
                
                self.ui.status_label.setText("")
                return True
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return False
        
    def install_action(self):
        self.ui.status_label.setText("Установка")
        self.ui.progress_bar.hide()
        # Формируем путь к файлу
        exe_path = Path("downloaded") / f"{self.name}.exe"
        
        # 1. Проверяем, существует ли файл
        if not exe_path.exists():
            print(f"Ошибка: Файл не найден по пути {exe_path}")
            return False

        try:
            print(f"Запуск установки: {self.name}...")
            
            # 2. Запускаем процесс
            # Используем Popen, чтобы не блокировать интерфейс программы
            subprocess.Popen(
                [str(exe_path.absolute())], 
                shell=True,
                creationflags=subprocess.CREATE_NEW_CONSOLE # Откроет в новом процессе
            )
            return True
            
        except Exception as e:
            print(f"Не удалось запустить установщик: {e}")
            return False
        
    def download_and_install_action(self):
        self.download_action()
        self.install_action()