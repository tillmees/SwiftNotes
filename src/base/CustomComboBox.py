from PySide6.QtWidgets import QComboBox


class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CustomComboBox, self).__init__(parent)

    def update_combo_box(self, string):
        index = self.findText(string)
        if index != -1:
            # a project with that name already exists
            return
        self.addItems([string])
        index = self.findText(string)
        self.setCurrentIndex(index)
        self.model().sort(0)

    def set_index_to_string(self, string):
        index = self.findText(string)
        if index == -1:
            # a project with that name doesn't yet exist
            return
        index = self.findText(string)
        self.setCurrentIndex(index)

    def add_string_to_combo_box(self, string):
        index = self.findText(string)
        if index != -1:
            # a project with that name already exists
            return
        self.addItems([string])
        self.model().sort(0)

    def add_whitespace_string_to_combo_box(self):
        self.addItems([" "])
        index = self.findText(" ")
        self.setCurrentIndex(index)
        self.model().sort(0)

    def delete_whitespace_string_from_combo_box(self):
        index = self.findText(" ")
        if index != -1:
            self.removeItem(index)

    def delete_string_from_combo_box(self, string):
        index = self.findText(string)
        if index != -1:
            self.removeItem(index)

    def get_current_project(self):
        return self.currentText()
