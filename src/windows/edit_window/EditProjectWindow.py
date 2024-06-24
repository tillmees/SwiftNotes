from windows.edit_window.EditWindow import EditWindow


class EditProjectWindow(EditWindow):
    def __init__(self):
        super(EditProjectWindow, self).__init__()
        self.setWindowTitle("Edit Project")

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
