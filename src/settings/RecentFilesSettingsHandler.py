import os

from settings.SettingsHandler import SettingsHandler


class RecentFilesSettingsHandler(SettingsHandler):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RecentFilesSettingsHandler, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            file_name = "swiftnotes_recent_files.json"
            super().__init__(file_name)
            self.initialized = True

    def _set_default_settings_dict(self):
        self._settings_dict = {
            "recentFiles": [],
        }

    def update_recent_files(self, file_path):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        file_dict = {
            "name": file_name,
            "path": file_path
        }

        # remove from recentFiles list if file_dict already in it
        if file_dict in self._settings_dict["recentFiles"]:
            self._settings_dict["recentFiles"].remove(file_dict)

        self._settings_dict["recentFiles"].insert(0, file_dict)
        
        # limit to 5 recent files
        if len(self._settings_dict["recentFiles"]) > 5:
            self._settings_dict["recentFiles"].pop(5)

        self._update_settings_json()

    def get_recent_file_name_by_index(self, index):
        if index >= len(self._settings_dict["recentFiles"]):
            return ""
        return self._settings_dict["recentFiles"][index]["name"]
    
    def get_recent_file_path_by_index(self, index):
        if index >= len(self._settings_dict["recentFiles"]):
            return ""
        return self._settings_dict["recentFiles"][index]["path"]