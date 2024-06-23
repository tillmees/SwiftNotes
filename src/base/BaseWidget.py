from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QMouseEvent

from style.Colors import lighten_color, darken_color


class BaseWidget(QDialog):

    def __init__(
            self,
            color_string
    ):
        super(BaseWidget, self).__init__()

        self.color_string = color_string
        self.lighter_color_string = lighten_color(self.color_string)
        self.darker_color_string = darken_color(self.color_string)

    def mousePressEvent(self, event: QMouseEvent):
        self.setStyleSheet(
            f"background-color: {self.darker_color_string};\n "
        )
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.setStyleSheet(
            f"background-color: {self.lighter_color_string};\n "
        )
        super().mouseReleaseEvent(event)

    def enterEvent(self, event):
        # Change background color when mouse hovers over/enters widget
        self.setStyleSheet(
            f"background-color: {self.lighter_color_string};\n "
        )
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Change back to the initial background color when mouse leaves
        self.setStyleSheet(f"background-color: {self.color_string};")
        super().leaveEvent(event)
