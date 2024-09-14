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
