from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, Signal


class CustomClickableLabel(QLabel):

    clicked = Signal()

    def __init__(self, parent=None):
        super(CustomClickableLabel, self).__init__(parent)

        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit()
