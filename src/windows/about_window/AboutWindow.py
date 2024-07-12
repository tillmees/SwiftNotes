from PySide6.QtWidgets import QDialog

from windows.about_window.AboutUi import Ui_About


class AboutWindow(QDialog):
    def __init__(self, version):
        super(AboutWindow, self).__init__()
        
        self.version = version
        self.ui = Ui_About()
        self.ui.setupUi(self)

        self.ui.set_text(self.version)
