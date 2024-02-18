from PySide6.QtWidgets import QDialogButtonBox, QDialog

from classes.Project import Project
from ui_windows.add_project_ui import Ui_AddProjectDialog


class AddProject(QDialog):
    def __init__(self):
        super(AddProject, self).__init__()

        self.ui = Ui_AddProjectDialog()
        self.ui.setupUi(self)
        self.ui.buttonBoxAddCancelProject.button(
            QDialogButtonBox.Ok).setEnabled(False)
        self.ui.lineEditProjectname.textChanged.connect(self.enable_ok_button)

    def exec(self):
        self.ui.lineEditProjectname.setFocus()
        return super(AddProject, self).exec()

    def accept(self):
        super(AddProject, self).accept()

    def reject(self):
        super(AddProject, self).reject()

    def clear_edits(self):
        self.ui.lineEditProjectname.clear()
        self.ui.plainTextEditDescription.clear()

    def get_project_from_user_input(self):
        project = Project(
            self.get_title(),
            self.get_description()
        )
        return project

    def enable_ok_button(self):
        if self.ui.lineEditProjectname.text() == "":
            self.ui.buttonBoxAddCancelProject.button(
                QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBoxAddCancelProject.button(
                QDialogButtonBox.Ok).setEnabled(True)

    def get_title(self):
        return self.ui.lineEditProjectname.text()

    def set_title(self, string):
        return self.ui.lineEditProjectname.setText(string)

    def get_description(self):
        return self.ui.plainTextEditDescription.toPlainText()

    def set_description(self, string):
        return self.ui.plainTextEditDescription.setPlainText(string)