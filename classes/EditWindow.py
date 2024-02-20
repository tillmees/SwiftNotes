from PySide6.QtWidgets import QDialogButtonBox, QDialog

from classes.TaskCreator import TaskCreator
from classes.TaskColors import TaskColors
from classes.Project import Project
from ui_windows.add_edit_window_ui import Ui_AddEditDialog


class AddEditWindow(QDialog):
    def __init__(self):
        super(AddEditWindow, self).__init__()

        self.ui = Ui_AddEditDialog()
        self.ui.setupUi(self)

        self.ui.buttonBoxAddCancelTask.button(
            QDialogButtonBox.Ok).setEnabled(False)

        self.ui.lineEditTaskname.textChanged.connect(self.on_task_name_changed)

        self.max_chars = 100

        self.colors = TaskColors()
        self.checkBoxes = []
        self.setup_checkbox_ids()
        self.setup_stylesheets()

    def exec_add(self):
        self.clear_edits()
        self.ui.lineEditTaskname.setFocus()
        return super(AddEditWindow, self).exec()

    def exec_edit(self):
        self.ui.lineEditTaskname.setFocus()
        return super(AddEditWindow, self).exec()

    def clear_edits(self):
        self.ui.lineEditTaskname.clear()
        self.ui.plainTextEditDescription.clear()

    def get_task_creator_from_user_input(self):
        task_creator = TaskCreator(
            self.get_title(),
            self.get_description(),
            self.get_color_string()
        )
        return task_creator

    def get_project_from_user_input(self):
        project = Project(
            self.get_title(),
            self.get_description(),
            color_string=self.get_color_string()
        )
        return project

    def on_task_name_changed(self):
        self.enable_ok_button()
        self.check_text_length()

    def enable_ok_button(self):
        if self.ui.lineEditTaskname.text() == "":
            self.ui.buttonBoxAddCancelTask.button(
                QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBoxAddCancelTask.button(
                QDialogButtonBox.Ok).setEnabled(True)

    def check_text_length(self):
        current_text = self.ui.lineEditTaskname.text()

        # Truncate the text if it exceeds the maximum character count
        if len(current_text) > self.max_chars:
            self.ui.lineEditTaskname.setText(current_text[:self.max_chars])

    def get_title(self):
        return self.ui.lineEditTaskname.text()

    def set_title(self, string):
        return self.ui.lineEditTaskname.setText(string)

    def get_description(self):
        return self.ui.plainTextEditDescription.toPlainText()

    def set_description(self, string):
        return self.ui.plainTextEditDescription.setPlainText(string)

    def get_color_string(self):
        checked_id = self.ui.buttonGroup.checkedId()
        return self.colors.color_mapping[checked_id]

    def set_color_checked_box(self, color_string):
        id = self.colors.get_color_id_by_string(color_string)
        self.checkBoxes[id - 1].setChecked(True)


    def setup_stylesheets(self):
        self.ui.color_1.setStyleSheet(
            f"background-color: {self.colors.Color1};\n "
            "border-radius: 10px;")
        self.ui.color_2.setStyleSheet(
            f"background-color: {self.colors.Color2};\n "
            "border-radius: 10px;")
        self.ui.color_3.setStyleSheet(
            f"background-color: {self.colors.Color3};\n "
            "border-radius: 10px;")
        self.ui.color_4.setStyleSheet(
            f"background-color: {self.colors.Color4};\n "
            "border-radius: 10px;")
        self.ui.color_5.setStyleSheet(
            f"background-color: {self.colors.Color5};\n "
            "border-radius: 10px;")
        self.ui.color_6.setStyleSheet(
            f"background-color: {self.colors.Color6};\n "
            "border-radius: 10px;")
        self.ui.color_7.setStyleSheet(
            f"background-color: {self.colors.Color7};\n "
            "border-radius: 10px;")
        self.ui.color_8.setStyleSheet(
            f"background-color: {self.colors.Color8};\n "
            "border-radius: 10px;")
        self.ui.color_9.setStyleSheet(
            f"background-color: {self.colors.Color9};\n "
            "border-radius: 10px;")
        self.ui.color_10.setStyleSheet(
            f"background-color: {self.colors.Color10};\n "
            "border-radius: 10px;")

    def setup_checkbox_ids(self):
        self.checkBoxes = [
            self.ui.checkBox_1,
            self.ui.checkBox_2,
            self.ui.checkBox_3,
            self.ui.checkBox_4,
            self.ui.checkBox_5,
            self.ui.checkBox_6,
            self.ui.checkBox_7,
            self.ui.checkBox_8,
            self.ui.checkBox_9,
            self.ui.checkBox_10,
        ]

        for id, checkBox in enumerate(self.checkBoxes):
            self.ui.buttonGroup.setId(
                checkBox,
                id + 1
            )