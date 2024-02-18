from classes.Project import Project


class ProjectHandler:
    def __init__(self):
        self.projects = {}
        self.current_project = None

    def add_project(self, project):
        self.projects[project.get_title()] = project

    def get_all_project_titles(self):
        project_names = [
            project.get_title() for project in self.projects.values()
        ]
        return project_names

    def get_project_by_title(self, title):
        return self.projects[title]

    def get_current_project(self):
        if self.current_project is not None:
            return self.projects[self.current_project]
        else:
            return None

    def set_current_project(self, current_project):
        self.current_project = current_project

    def project_edited(self, old_title, new_title, new_description):
        self.projects[new_title] = self.projects.pop(old_title)
        self.set_current_project(new_title)
        self.projects[self.current_project].set_title(new_title)
        self.projects[self.current_project].set_description(new_description)

