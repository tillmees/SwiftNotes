from PySide6.QtWidgets import QDialog

from classes.Project import Project
from ui_windows.info_project_ui import Ui_InfoProjectDialog


class InfoProject(QDialog):
    def __init__(self):
        super(InfoProject, self).__init__()

        self.ui = Ui_InfoProjectDialog()
        self.ui.setupUi(self)

    def execute(self, project):
        self.ui.label_Name.setText(project.get_title())
        self.ui.plainTextEditDescription.setPlainText(
            project.get_description()
        )
        self.ui.label_DateCreated.setText(
            project.get_created_string()
        )
        self.ui.label_DateChanged.setText(
            project.get_last_changed_string()
        )
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

        self.exec()
