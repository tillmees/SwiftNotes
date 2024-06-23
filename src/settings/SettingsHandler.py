import os
import json


class SettingsHandler:
    def __init__(self, file_name):
        self._settings_file_name = file_name

        # set default values
        self._settings_dict = None
        self.set_settings_dict()    

        self.__on_startup()

    def __on_startup(self):
        if not os.path.exists(self._settings_file_name):
            self.__create_settings_json()
        else:
            self.__parse_settings_json()
                                
    def __parse_settings_json(self):
        with open(self._settings_file_name, "r") as file:
            data = json.load(file)
        
        for key, value in data.items():
            self._settings_dict[key] = value

    def __create_settings_json(self):
        self.__update_settings_json()
            
    def __update_settings_json(self):
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

    def set_settings_dict(self):
        self._settings_dict = {}
