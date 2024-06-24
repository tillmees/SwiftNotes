from task.Task import Task
from windows.add_window.AddWindow import AddWindow


class AddTaskWindow(AddWindow):
    def __init__(self):
        super(AddTaskWindow, self).__init__()
        self.setWindowTitle("Add Task")

    def get_task_from_user_input(self):
        project = Task(
            title=self.get_title(),
            description=self.get_description(),
            color_id=self.get_color_id()
        )
        return project
