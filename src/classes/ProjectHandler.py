from classes.Project import Project


class ProjectHandler:
    def __init__(self):
        self.projects = {}
        self.current_project = None

    def add_project(self, project):
        self.projects[project.get_title()] = project

    def remove_project_by_hash(self, hash_value):
        for project in self.projects.values():
            if project.get_hash() == hash_value:
                self.projects.pop(project.title)
                return
        return None

    def get_all_project_titles(self):
        project_names = [
            project.get_title() for project in self.projects.values()
        ]
        return project_names

    def get_project_by_title(self, title):
        return self.projects[title]

    def get_project_by_hash(self, hash_value):
        for project in self.projects.values():
            if project.get_hash() == hash_value:
                return project
        return None

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

    def get_list_of_projects(self, sort_member=None):
        project_list = [project for project in self.projects.values()]
        if sort_member is not None and project_list:
            project_list = self.sort_list_of_projects(project_list,
                                                      sort_member)
        return project_list

    @staticmethod
    def sort_list_of_projects(project_list, sort_member):
        if not hasattr(project_list[0], sort_member):
            raise ValueError(
                f"'{sort_member} not a member of the 'Project' class."
            )
        sorted_project_list = sorted(
            project_list,
            key=lambda project: getattr(project, sort_member)
        )
        if sort_member in ["last_changed_string", "open_task_count"]:
            sorted_project_list = sorted_project_list[::-1]

        return sorted_project_list
