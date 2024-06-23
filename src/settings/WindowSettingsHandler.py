from settings.SettingsHandler import SettingsHandler


class WindowSettingsHandler(SettingsHandler):
    def __init__(self, file_name):
        super().__init__(file_name)

    def set_settings_dict(self):
        self._settings_dict = {
            "layout": "light",
            "width": "1080",
            "height": "520"
        }
