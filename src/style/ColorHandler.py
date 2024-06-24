from settings.StyleSettingsHandler import StyleSettingsHandler


class ColorHandler():

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ColorHandler, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.style_settings_handler = StyleSettingsHandler()
            self.colors_dict = self.style_settings_handler.get_colors_dict()
            self.color_mapping = {}
            for key, val in self.colors_dict.items():
                index = key.split("_")[1]
                self.color_mapping[int(index)] = val

    def get_color_id_by_string(self, string):
        for key, val in self.color_mapping.items():
            if val == string:
                return key
        return None