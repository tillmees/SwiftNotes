from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QMouseEvent

from base.UtilityFunctions import lighten_color, darken_color, transparent_color, get_current_time_string
from style.ColorHandler import ColorHandler


class CustomBaseWidget(QDialog):

    def __init__(
            self,
            title,
            created_string,
            last_changed_string,
            color_id,
            hash_value
    ):
        super(CustomBaseWidget, self).__init__()
        self.color_handler = ColorHandler()

        self.title = title
        self.created_string = created_string
        self.last_changed_string = last_changed_string
        self.color_id = color_id
        self.hash_value = hash_value

        self.color_string = None
        self.set_color_string()
        self.lighter_color_string = lighten_color(self.color_string)
        self.darker_color_string = darken_color(self.color_string)
        self.transparent_color_string = transparent_color(self.color_string)
        self.is_transparent = False

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
        if self.is_transparent == False:
            self.setStyleSheet(
                f"background-color: {self.lighter_color_string};\n "
            )
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Change back to the initial background color when mouse leaves
        if self.is_transparent == False:
            self.setStyleSheet(f"background-color: {self.color_string};")
        super().leaveEvent(event)

    def get_hash(self):
        return self.hash_value

    def get_title(self):
        return self.title
    
    def set_title(self, new_title):
        self.title = new_title
        self.update_last_changed_string()

    def get_created_string(self):
        return self.created_string

    def get_last_changed_string(self):
        return self.last_changed_string

    def update_last_changed_string(self):
        self.last_changed_string = get_current_time_string()

    def get_color_id(self):
        return self.color_id
    
    def set_color_id(self, color_id):
        self.color_id = color_id
        self.set_color_string()

    def set_color_string(self):
        self.color_string = self.color_handler.color_mapping[self.color_id]

    def get_color_string(self):
        return self.color_string
