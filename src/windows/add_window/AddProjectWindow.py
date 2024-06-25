from PySide6.QtWidgets import QDialogButtonBox

from project.Project import Project
from windows.add_window.AddWindow import AddWindow


class AddProjectWindow(AddWindow):
    def __init__(self):
        super(AddProjectWindow, self).__init__()
        self.setWindowTitle("Add Project")
        self.already_existing_project_titles = []

    def exec(self, already_existing_project_titles):
        self.already_existing_project_titles = already_existing_project_titles

        success = super().exec()

        self.already_existing_project_titles = []

        return success

    def is_title_already_used(self):
        if self.ui.lineEditTaskname.text() in self.already_existing_project_titles:
            self.ui.label_okDisabledExplanation.setText("This title is already used.")
            return True
        else:
            self.ui.label_okDisabledExplanation.setText("")
            return False
        
    def enable_ok_button(self):
        currently_given_title = self.ui.lineEditTaskname.text()
        if currently_given_title == "" or self.is_title_already_used():
            self.ui.buttonBoxAddCancelTask.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBoxAddCancelTask.button(QDialogButtonBox.Ok).setEnabled(True)

    def get_project_from_user_input(self):
        project = Project(
            title=self.get_title(),
            description=self.get_description(),
            color_id=self.get_color_id()
        )
        return project
