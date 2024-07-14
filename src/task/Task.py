import xml.etree.ElementTree as ET

from base.UtilityFunctions import get_current_time_string, get_hash_from_time


task_attributes = [
        "title", "description", "color_id",
        "created_string", "last_changed_string",
        "hash_value", "task_bin"
    ]


class Task:
    def __init__(self,
                 title,
                 description,
                 color_id,
                 created_string=None,
                 last_changed_string=None,
                 hash_value=None,
                 task_bin=None):
        self.title = title
        self.description = "" if description is "None" else description
        self.color_id = int(color_id)
        self.created_string = self._init_created_string(created_string)
        self.last_changed_string = self._init_last_changed_string(last_changed_string)
        self.hash_value = self._init_hash_value(hash_value)
        self.task_bin = "open" if task_bin is None else task_bin

    def to_xml(self):
        element = ET.Element('Task')
        for attr in task_attributes:
            var_element = ET.SubElement(element, attr)
            var_element.text = str(eval(f"self.{attr}"))
        return element 
    
    @classmethod
    def from_xml(cls, element):
        kwargs = {}
        for attr in task_attributes:
            if element.find(attr) is None:
                kwargs[attr] = None
            else:
                kwargs[attr] = element.find(attr).text
        return cls(**kwargs)

    def _init_created_string(self, created_string):
        return get_current_time_string() if created_string is None else created_string

    def _init_last_changed_string(self, last_changed_string):
        return self.created_string if last_changed_string is None else last_changed_string

    def _init_hash_value(self, hash_value):
        return get_hash_from_time(self.created_string) if hash_value is None else hash_value

    def update_last_changed_string(self):
        self.last_changed_string = get_current_time_string()

    def get_created_string(self):
        return self.created_string
    
    def get_last_changed_string(self):
        return self.last_changed_string

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title
        self.update_last_changed_string()

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
        self.update_last_changed_string()

    def get_color_id(self):
        return self.color_id

    def set_color_id(self, color_id):
        self.color_id = color_id
        self.update_last_changed_string()

    def set_task_bin(self, task_bin):
        self.task_bin = task_bin
        self.update_last_changed_string()
