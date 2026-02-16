from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from widgets.main_window import Ui_MainWindow
from .program import UI_Program

from src.models import ProgramFiles
from src.config import default_file
from src.downloader import Downloader



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.program_files: ProgramFiles = ProgramFiles(programs=[])
        self.downloader = Downloader()
        
    def init_ui(self):
        self.ui.link_line_edit.setPlaceholderText(default_file)
        
        self.ui.set_link_button.clicked.connect(self.set_link_action)
        
        
    def show_program_files(self):
        self.ui.list_widget.clear()
        for program_file in self.program_files.programs:
            program = UI_Program(
                program_file.name, 
                program_file.icon,
                program_file.url
            )
            
            
            item = QListWidgetItem(self.ui.list_widget)
            item.setSizeHint(program.sizeHint())
            self.ui.list_widget.setItemWidget(item, program)
            
        
    def set_link_action(self):
        text = self.ui.link_line_edit.text()
        if text:
            self.downloader.set_url(text)
        else:
            self.downloader.set_url(default_file)
        print(text)
        self.downloader.upload_file()
        self.program_files = self.downloader.load_config()
        self.show_program_files()
        