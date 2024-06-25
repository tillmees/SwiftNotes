from PySide6.QtWidgets import QDialogButtonBox, QDialog

from windows.add_window.AddUi import Ui_AddDialog
from style.ColorHandler import ColorHandler


class AddWindow(QDialog):
    def __init__(self):
        super(AddWindow, self).__init__()
        
        self.color_handler = ColorHandler()
        
        self.ui = Ui_AddDialog()
        self.ui.setupUi(self)

        self.setup_checkbox_ids()
        self.setup_stylesheets()

        self.max_chars = 100
        self.ui.lineEditTaskname.textChanged.connect(self.on_title_changed)
        self.ui.buttonBoxAddCancelTask.button(QDialogButtonBox.Ok).setEnabled(False)

    def exec(self):
        self.clear_edits()
        self.ui.lineEditTaskname.setFocus()
        self.ui.label_okDisabledExplanation.setText("")
        return super(AddWindow, self).exec()

    def clear_edits(self):
        self.ui.lineEditTaskname.clear()
        self.ui.plainTextEditDescription.clear()

    def on_title_changed(self):
        self.enable_ok_button()
        self.truncate_title_if_needed()

    def enable_ok_button(self):
        if self.ui.lineEditTaskname.text() == "":
            self.ui.buttonBoxAddCancelTask.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBoxAddCancelTask.button(QDialogButtonBox.Ok).setEnabled(True)

    def truncate_title_if_needed(self):
        current_text = self.ui.lineEditTaskname.text()

        # Truncate the text if it exceeds the maximum character count
        if len(current_text) > self.max_chars:
            self.ui.lineEditTaskname.setText(current_text[:self.max_chars])
            if self.ui.label_okDisabledExplanation.text() == "":
                self.ui.label_okDisabledExplanation.setText(f"Title reached its max. of {self.max_chars} characters.")

    def get_title(self):
        return self.ui.lineEditTaskname.text()

    def get_description(self):
        return self.ui.plainTextEditDescription.toPlainText()

    def get_color_id(self):
        checked_color_id = self.ui.buttonGroup.checkedId()
        return checked_color_id

    def setup_stylesheets(self):
        for id in range(10):
            eval(f"self.ui.color_{id+1}").setStyleSheet(f"background-color: {self.color_handler.color_mapping[id]}; border-radius: 10px;")

    def setup_checkbox_ids(self):
        for id in range(10):
            checkbox = eval(f"self.ui.checkBox_{id+1}")
            self.ui.buttonGroup.setId(checkbox, id)