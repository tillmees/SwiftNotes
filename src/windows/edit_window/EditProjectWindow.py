from PySide6.QtWidgets import QDialogButtonBox

from windows.edit_window.EditWindow import EditWindow


class EditProjectWindow(EditWindow):
    def __init__(self, color_id=0):
        super(EditProjectWindow, self).__init__(color_id)
        self.setWindowTitle("Edit Project")
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
    
    def get_attributes_from_user_input(self):
        return self.get_title(), self.get_description(), self.get_color_id()

    def setup_window(self, project):
        super().setup_window(project)
        self.ui.label_NoTasks.setText(
            f"{project.get_task_count()}"
        )
        self.ui.label_NoOpen.setText(
            f"{project.get_task_count_in('open')}"
        )
        self.ui.label_NoInProgress.setText(
            f"{project.get_task_count_in('in progress')}"
        )
        self.ui.label_NoStuckTest.setText(
            f"{project.get_task_count_in('stuck/test')}"
        )
        self.ui.label_NoDone.setText(
            f"{project.get_task_count_in('done')}"
        )
        self.ui.label_Project.hide()
        self.ui.comboBoxProjects.hide()
