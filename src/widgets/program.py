from widgets.program import Ui_Program

class UI_Program(Ui_Program):
    def __init__(self) -> None:
        super().__init__()
        self.self_ui()
        
    def self_ui(self):
        self.install_button.clicked.connect(self.install_action)
        self.download_button.clicked.connect(self.download_action)
        self.download_and_install_button.clicked.connect(self.download_and_install_action)
        
        
    def download_action(self):
        ...
        
    def install_action(self):
        ...
        
    def download_and_install_action(self):
        self.download_action()
        self.install_action()