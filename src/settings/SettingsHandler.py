import os
import json


class SettingsHandler:
    def __init__(self, file_name):
        self._settings_file_name = file_name

        # set default values
        self._settings_dict = {}
        self._set_settings_dict()
        self._on_startup()

    def _set_settings_dict(self):
        self._settings_dict = {}

    def _on_startup(self):
        if not os.path.exists(self._settings_file_name):
            self.__create_settings_json()
        else:
            self.__parse_settings_json()
                                
    def _parse_settings_json(self):
        with open(self._settings_file_name, "r") as file:
            data = json.load(file)
        
        for key, value in data.items():
            self._settings_dict[key] = value

    def _create_settings_json(self):
        self.__update_settings_json()
            
    def _update_settings_json(self):
        with open(self._settings_file_name, "w") as f:
            json.dump(self._settings_dict, f, indent=4)
            
    def get_value_for(self, attribute):
        if attribute in self._settings_dict:
            return self._settings_dict[attribute]
        else:
            return None
    
    def set_value_to(self, attribute, value):
        if attribute in self._settings_dict:
            self._settings_dict[attribute] = value
        self.__update_settings_json()

    def get_settings_dict(self):
        return self._settings_dict
