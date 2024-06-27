import copy
import xml.etree.ElementTree as ET

from project.Project import Project


class ProjectManager:    
    
    def __init__(self,
                 projects=None,
                 current_project_hash_value=None):
        self.projects = self._init_project_list(projects)
        self.current_project_hash_value = current_project_hash_value
    
    def to_xml(self):
        element = ET.Element('ProjectManager')
        idx = 0
        for key, value in self.__dict__.items():
            var_element = ET.SubElement(element, key)
            if key == 'projects':
                for project in self.projects:
                    var_element.append(project.to_xml())
            else:
                var_element.text = str(value)
            idx += 1
        return element
    
    @classmethod
    def from_xml(cls, element):
        attributes = ["projects", "current_project_hash_value"]
        kwargs = {}
        for attr in attributes:
            if element.find(attr) is None:
                kwargs[attr] = ""
            else:
                if attr == "projects":
                    projects = []
                    for project_element in element.find(attr):
                        projects.append(Project.from_xml(project_element))
                    kwargs[attr] = projects
                else:
                    kwargs[attr] = element.find(attr).text
        return cls(**kwargs)
    
    def _init_project_list(self, projects):
        return [] if projects is None else projects

    def add_project(self, project):
        success = False
        if self.get_project_by_hash(project.get_hash()) is None:
            self.projects.append(project)
            self.set_current_project(project.get_hash())
            success = True
        return success

    def get_project_by_hash(self, hash_value):
        for project in self.projects:
            if project.hash_value == hash_value:
                return project
        return None

    def remove_project_by_hash(self, hash_value):
        project = self.get_project_by_hash(hash_value)
        if project is not None:
            self.projects.remove(project)
            return
    
    def get_project_hash_by_title(self, title):
        for project in self.projects:
            if project.get_title() == title:
                return project.get_hash()
        return None

    def get_current_project(self):
        if self.current_project_hash_value is not None:
            return self.get_project_by_hash(self.current_project_hash_value)
        else:
            return None

    def set_current_project(self, current_project_hash_value):
        self.current_project_hash_value = current_project_hash_value

    def get_list_of_all_titles(self):
        return [project.get_title() for project in self.projects]

    def project_edited(self, hash_value, new_title, new_description, new_color_id):
        self.set_current_project(hash_value)
        project = self.get_project_by_hash(hash_value)
        project.set_title(new_title)
        project.set_description(new_description)
        project.set_color_id(new_color_id)

    def get_list_of_projects(self, sort_member=None):
        project_list = copy.deepcopy(self.projects)
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
