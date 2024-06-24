from project.Project import Project
from windows.add_window.AddWindow import AddWindow


class AddProjectWindow(AddWindow):
    def __init__(self):
        super(AddProjectWindow, self).__init__()
        self.setWindowTitle("Add Project")

    def get_project_from_user_input(self):
        project = Project(
            title=self.get_title(),
            description=self.get_description(),
            color_id=self.get_color_id()
        )
        return project
