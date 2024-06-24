from base.UtilityFunctions import get_current_time_string, get_hash_from_time

from style.ColorHandler import ColorHandler


class Project:
    def __init__(self,
                 title,
                 description,
                 created_string=None,
                 last_changed_string=None,
                 hash_value=None,
                 tasks=None,
                 color_id=0):
        self.title = title
        self.description = description

        self.created_string = self._set_created_string(created_string)
        self.last_changed_string = self._set_last_changed_string(last_changed_string)
        self.hash_value = self._set_hash_value(hash_value)

        self.task_creators = self._init_task_creatorss(tasks)
        self.temp_disabled_tasks = []

        self.color_id = color_id
        self.color_handler = ColorHandler()
        self.color_string = self.color_handler.color_mapping[self.color_id]
        self.open_task_count = 0

    def add_task(self, task_creator):
        self.task_creators.append(task_creator)
        self.update_last_changed_string()
        self.update_open_task_count()

    def _set_created_string(self, created_string=None):
        return get_current_time_string() if \
            created_string is None else created_string

    def _set_last_changed_string(self, last_changed_string=None):
        return self.created_string if \
            last_changed_string is None else last_changed_string

    def _set_hash_value(self, hash_value=None):
        return get_hash_from_time(self.created_string) if \
            hash_value is None else hash_value

    def _init_task_creatorss(self, task_creators):
        return [] if task_creators is None else task_creators

    def get_hash(self):
        return self.hash_value

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title
        self.update_last_changed_string()

    def get_created_string(self):
        return self.created_string

    def get_last_changed_string(self):
        return self.last_changed_string

    def update_last_changed_string(self):
        self.last_changed_string = get_current_time_string()

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description
        self.update_last_changed_string()

    def get_tasks_in(self, bin_string=None):
        return [
            task_creator for task_creator in self.task_creators if task_creator.task_bin == bin_string
        ]

    def get_task_by_hash(self, hash_value):
        for task_creator in self.task_creators:
            if task_creator.hash_value == hash_value:
                return task_creator
        return None

    def remove_task_by_hash(self, hash_value):
        task_creator = self.get_task_by_hash(hash_value)
        if task_creator is not None:
            self.task_creators.remove(task_creator)
            self.update_last_changed_string()
            self.update_open_task_count()
            return

    def move_task_by_hash_in_bin(self, hash_value, new_task_bin):
        task_creator = self.get_task_by_hash(hash_value)
        if task_creator is not None:
            task_creator.set_task_bin(new_task_bin)
            self.update_last_changed_string()
            self.update_open_task_count()

    def get_task_count_in(self, bin_string=None):
        # possible bins: "open", "in progress", "stuck/test", "done"
        return len(
            [task_creator for task_creator in self.task_creators if task_creator.task_bin == bin_string]
        )

    def get_task_count(self):
        return len(self.task_creators)

    def update_open_task_count(self):
        self.open_task_count = (
                self.get_task_count_in("open") + \
                self.get_task_count_in("in progress") + \
                self.get_task_count_in("stuck/test")
        )

    def set_color_string(self):
        self.color_string = self.color_handler.color_mapping[self.color_id]

    def get_color_id(self):
        return self.color_id
    
    def set_color_id(self, color_id):
        self.color_id = color_id
        self.set_color_string()
        self.update_last_changed_string()