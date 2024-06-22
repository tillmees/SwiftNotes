from PySide6.QtWidgets import QScrollArea
from PySide6.QtCore import Signal


class CustomScrollArea(QScrollArea):

    drop_signal = Signal(str)

    def __init__(self, name, parent=None):
        super(CustomScrollArea, self).__init__(parent)
        self.name = name
        self.setAcceptDrops(True)

    def get_name(self):
        return self.name
        
    def dragEnterEvent(self, event):
        event.accept()
    
    def dropEvent(self, event):
        self.drop_signal.emit(self.name)
        event.accept()
