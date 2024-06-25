class ProjectManager:    
    
    def __init__(self):
        self.projects = {}
        self.current_project_hash_value = None

    def add_project(self, project):
        success = False
        if self.get_project_hash_by_title(project.get_title()) is None:
            hash_value = project.get_hash()
            self.projects[hash_value] = project
            self.set_current_project(hash_value)
            success = True
        return success

    def get_project_by_hash(self, hash_value):
        return self.projects[hash_value]
    
    def get_project_hash_by_title(self, title):
        for project in self.projects.values():
            if project.get_title() == title:
                return project.get_hash()
        return None
    
    def remove_project_by_hash(self, hash_value):
        if hash_value in self.projects:
            self.projects.pop(hash_value)

    def get_current_project(self):
        if self.current_project_hash_value is not None:
            return self.projects[self.current_project_hash_value]
        else:
            return None

    def set_current_project(self, current_project_hash_value):
        self.current_project_hash_value = current_project_hash_value

    def get_list_of_all_titles(self):
        return [project.get_title() for project in self.projects.values()]

    def project_edited(self, hash_value, new_title, new_description, new_color_id):
        self.set_current_project(hash_value)
        self.projects[hash_value].set_title(new_title)
        self.projects[hash_value].set_description(new_description)
        self.projects[hash_value].set_color_id(new_color_id)

    def get_list_of_projects(self, sort_member=None):
        project_list = [project for project in self.projects.values()]
        if sort_member is not None and project_list:
            project_list = self.sort_list_of_projects(project_list, sort_member)
        return project_list

    @staticmethod
    def sort_list_of_projects(project_list, sort_member):
        if not hasattr(project_list[0], sort_member):
            raise ValueError(
                f"'{sort_member} not a member of the 'ProjectClass'."
            )
        sorted_project_list = sorted(
            project_list,
            key=lambda project: getattr(project, sort_member)
        )
        if sort_member in ["last_changed_string", "open_task_count"]:
            sorted_project_list = sorted_project_list[::-1]

        return sorted_project_list
