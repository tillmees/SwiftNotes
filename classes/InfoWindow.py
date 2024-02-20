from PySide6.QtWidgets import QDialog

from classes.Project import Project
from classes.TaskCreator import TaskCreator
from ui_windows.info_window_ui import Ui_InfoDialog


class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()

        self.ui = Ui_InfoDialog()
        self.ui.setupUi(self)

    def execute(self, obj):
        if isinstance(obj, Project):
            self.setup_for_project(obj)
        elif isinstance(obj, TaskCreator):
            self.setup_for_task(obj)
        else:
            assert False

        self.exec()

    def setup_for_project(self, project):
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

        self.ui.label_6.show()
        self.ui.label_7.show()
        self.ui.label_8.show()
        self.ui.label_9.show()
        self.ui.label_10.show()

        self.ui.label_NoTasks.show()
        self.ui.label_NoOpen.show()
        self.ui.label_NoInProgress.show()
        self.ui.label_NoStuckTest.show()
        self.ui.label_NoDone.show()

    def setup_for_task(self, task):
        self.ui.label_Name.setText(
            task.title
        )
        self.ui.plainTextEditDescription.setPlainText(
            task.description
        )
        self.ui.label_DateCreated.setText(
            task.created_string
        )
        self.ui.label_DateChanged.setText(
            task.last_changed_string
        )

        self.ui.label_6.hide()
        self.ui.label_7.hide()
        self.ui.label_8.hide()
        self.ui.label_9.hide()
        self.ui.label_10.hide()

        self.ui.label_NoTasks.hide()
        self.ui.label_NoOpen.hide()
        self.ui.label_NoInProgress.hide()
        self.ui.label_NoStuckTest.hide()
        self.ui.label_NoDone.hide()