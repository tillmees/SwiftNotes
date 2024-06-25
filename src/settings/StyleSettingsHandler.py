from settings.SettingsHandler import SettingsHandler


class StyleSettingsHandler(SettingsHandler):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(StyleSettingsHandler, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, file_name=None):
        if not hasattr(self, 'initialized'):
            super().__init__(file_name)
            self.initialized = True
        else:
            assert file_name == None, f"{type(self).__name__} singleton should have been initialized already"

    def get_light_layout_dict(self):
        return self._settings_dict["light"]

    def get_dark_layout_dict(self):
        return self._settings_dict["dark"]
    
    def get_colors_dict(self):
        return self._settings_dict["colors"]

    def _set_default_settings_dict(self):
        self._settings_dict = {
            "light": {
                "main_background": "rgba(238, 238, 238, 1.0)",
                "title_bar_background": "rgba(238, 238, 238, 1.0)",
                "popup_background": "rgba(245, 245, 245, 1.0)",
                "popup_fields": "rgba(255, 255, 255, 1.0)",
                "popup_fields_font": "rgba(0, 0, 0, 1.0)",
                "combobox": "rgba(245, 245, 245, 1.0)",
                "combobox_border": "rgba(200, 200, 200, 1.0)",
                "combobox_font": "rgba(17, 17, 17, 1.0)",
                "sidebar": "rgba(200, 200, 200, 1.0)",
                "sidebar_divider": "rgba(180, 180, 180, 1.0)",
                "sidebar_label": "rgba(0, 0, 0, 1.0)",
                "task_area": "rgba(245, 245, 245, 1.0)",
                "project_area": "rgba(245, 245, 245, 1.0)",
                "button": "rgba(0, 0, 0, 0.0)",
                "button_hover": "rgba(86, 101, 115, 0.5)",
                "button_pressed": "rgba(46, 61, 75, 0.5)",
                "label_view": "rgba(86, 101, 115, 0.5)",
                "label_projects_header": "rgba(0, 0, 0, 1.0)",
                "label_light": "rgba(0, 0, 0, 1.0)",
                "label_light_weight": "bold",
                "label_dark": "rgba(0, 0, 0, 1.0)",
                "label_dark_weight": "regular",
                "label_welcome": "rgba(200, 200, 200, 1.0)",
                "button_titlebar_hover": "rgba(0, 0, 0, 0.125)",
                "button_titlebar_pressed": "rgba(0, 0, 0, 0.25)"
            },
            "dark": {
                "main_background": "rgba(30, 31, 34, 1.0)",
                "title_bar_background": "rgba(30, 31, 34, 1.0)",
                "popup_background": "rgba(43, 45, 50, 1.0)",
                "popup_fields": "rgba(67, 69, 74, 1.0)",
                "popup_fields_font": "rgba(255, 255, 255, 1.0)",
                "combobox": "rgba(43, 45, 50, 1.0)",
                "combobox_border": "rgba(30, 31, 34, 1.0)",
                "combobox_font": "rgba(255, 255, 255, 1.0)",
                "sidebar": "rgba(43, 45, 50, 1.0)",
                "sidebar_divider": "rgba(30, 31, 34, 1.0)",
                "sidebar_label": "rgba(255, 255, 255, 1.0)",
                "task_area": "rgba(43, 45, 50, 1.0)",
                "project_area": "rgba(43, 45, 50, 1.0)",
                "button": "rgba(0, 0, 0, 0.0)",
                "button_hover": "rgba(86, 101, 115, 0.5)",
                "button_pressed": "rgba(46, 61, 75, 0.5)",
                "label_view": "rgba(172, 172, 172, 1.0)",
                "label_projects_header": "rgba(172, 172, 172, 1.0)",
                "label_light": "rgba(255, 255, 255, 1.0)",
                "label_light_weight": "regular",
                "label_dark": "rgba(255, 255, 255, 1.0)",
                "label_dark_weight": "bold",
                "label_welcome": "rgba(200, 200, 200, 1.0)",
                "button_titlebar_hover": "rgba(255, 255, 255, 0.125)",
                "button_titlebar_pressed": "rgba(255, 255, 255, 0.25)"
            },
            "colors": {
                "color_0": "#EE9B01",
                "color_1": "#CA6702",
                "color_2": "#BB3F03",
                "color_3": "#AE2012",
                "color_4": "#CCBC90",
                "color_5": "#099396",
                "color_6": "#005F73",
                "color_7": "#529352",
                "color_8": "#A3BF5F",
                "color_9": "#BF5D94",
            },
        }
