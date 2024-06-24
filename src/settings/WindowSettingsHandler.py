from settings.SettingsHandler import SettingsHandler


class WindowSettingsHandler(SettingsHandler):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WindowSettingsHandler, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, file_name=None):
        if not hasattr(self, 'initialized'):
            super().__init__(file_name)
            self.initialized = True
        else:
            assert file_name == None, f"{type(self).__name__} singleton should have been initialized already"

    def _set_default_settings_dict(self):
        self._settings_dict = {
            "layout": "light",
            "width": "1080",
            "height": "520"
        }
