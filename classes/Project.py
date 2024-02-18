import copy

from classes.TaskCreator import TaskCreator
from functions.UtilityFunctions import get_current_time_string, \
    get_hash_from_time


class Project:
    def __init__(self,
                 title,
                 description,
                 created_string=None,
                 last_changed_string=None,
                 hash_value=None,
                 tasks=None):
        self.title = title
        self.description = description

        self.created_string = self._set_created_string(
            created_string)
        self.last_changed_string = self._set_last_changed_string(
            last_changed_string)
        self.hash_value = self._set_hash_value(
            hash_value)

        self.tasks = self._set_tasks(
            tasks)

    def add_task(self, task):
        self.tasks.append(task)
        self.update_last_changed_string()

    def _set_created_string(self, created_string=None):
        return get_current_time_string() if \
            created_string is None else created_string

    def _set_last_changed_string(self, last_changed_string=None):
        return self.created_string if \
            last_changed_string is None else last_changed_string

    def _set_hash_value(self, hash_value=None):
        return get_hash_from_time(self.created_string) if \
            hash_value is None else hash_value

    def _set_tasks(self, tasks):
        return [] if tasks is None else tasks

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
            task for task in self.tasks if task.task_bin == bin_string
        ]

    def get_task_by_hash(self, hash_value):
        for task in self.tasks:
            if task.hash_value == hash_value:
                return task
        return None

    def remove_task_by_hash(self, hash_value):
        task = self.get_task_by_hash(hash_value)
        if task is not None:
            self.tasks.remove(task)
            self.update_last_changed_string()
            return

    def move_task_by_hash_in_bin(self, hash_value, new_task_bin):
        task = self.get_task_by_hash(hash_value)
        if task is not None:
            task.set_task_bin(new_task_bin)
            self.update_last_changed_string()


    def get_task_count_in(self, bin_string=None):
        return len(
            [task for task in self.tasks if task.task_bin == bin_string]
        )

    def get_task_count(self):
        return len(self.tasks)
