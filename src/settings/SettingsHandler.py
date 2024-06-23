import os
import json


class SettingsHandler:
    def __init__(self, file_name):
        self._settings_file_name = file_name

        # set default values
        self._settings_dict = {
            "layout": "light",
            "width": "978",
            "height": "510"
        }

        self.__on_startup()

    def __on_startup(self):
        if not os.path.exists(self._settings_file_name):
            self.__update_settings_json()
        else:
            self.__parse_settings_json()
                                
    def __parse_settings_json(self):
        with open(self._settings_file_name, "r") as file:
            data = json.load(file)
        
        for key, value in data.items():
            self._settings_dict[key] = value
            
    def __update_settings_json(self):
        with open(self._settings_file_name, "w") as f:
            f.write("{\n")
            for idx, (key, val) in enumerate(self._settings_dict.items()):
                if idx < len(self._settings_dict) - 1:
                    f.write(f'\t"{key}": "{val}",\n')
                else:
                    # no trailing comma on last entry
                    f.write(f'\t"{key}": "{val}"\n')
            f.write("}\n")
            
    def get_value_for(self, attribute):
        if attribute in self._settings_dict:
            return self._settings_dict[attribute]
        else:
            return None
        
    def get_value_for_as_int(self, attribute):
        if attribute in self._settings_dict:
            return int(self._settings_dict[attribute])
        else:
            return None
    
    def set_value_to(self, attribute, value):
        if attribute in self._settings_dict:
            self._settings_dict[attribute] = value
        self.__update_settings_json()
