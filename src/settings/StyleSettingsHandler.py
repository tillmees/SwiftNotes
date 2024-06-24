from settings.SettingsHandler import SettingsHandler


class StyleSettingsHandler(SettingsHandler):
    def __init__(self, file_name):
        super().__init__(file_name)

    def _set_settings_dict(self):
        self._settings_dict = {
            "light": {
                "main_background": "#eeeeee",
                "title_bar_background": "#eeeeee",
                "popup_background": "rgb(245, 245, 245)",
                "popup_fields": "#ffffff",
                "popup_fields_font": "#000000",
                "combobox": "#f5f5f5",
                "combobox_border": "rgb(200, 200, 200)",
                "combobox_font": "#111111",
                "sidebar": "rgb(200, 200, 200)",
                "sidebar_divider": "rgb(180, 180, 180)",
                "sidebar_label": "#000000",
                "task_area": "#f5f5f5",
                "project_area": "#f5f5f5",
                "button": "rgba(0, 0, 0, 0.0)",
                "button_hover": "rgba(86, 101, 115, 0.5)",
                "button_pressed": "rgba(46, 61, 75, 0.5)",
                "label_view": "rgba(86, 101, 115, 0.5)",
                "label_projects_header": "#000000",
                "label_light": "#000000",
                "label_light_weight": "bold",
                "label_dark": "#000000",
                "label_dark_weight": "regular",
                "label_welcome": "rgb(200, 200, 200)",
                "button_titlebar_hover": "rgba(0, 0, 0, 0.125)",
                "button_titlebar_pressed": "rgba(0, 0, 0, 0.25)"
            },
            "dark": {
                "main_background": "#1e1f22",
                "title_bar_background": "#1e1f22",
                "popup_background": "#2b2d30",
                "popup_fields": "#43454a",
                "popup_fields_font": "#ffffff",
                "combobox": "#2b2d30",
                "combobox_border": "#1e1f22",
                "combobox_font": "#ffffff",
                "sidebar": "#2b2d30",
                "sidebar_divider": "#1e1f22",
                "sidebar_label": "#ffffff",
                "task_area": "#2b2d30",
                "project_area": "#2b2d30",
                "button": "rgba(0, 0, 0, 0.0)",
                "button_hover": "rgba(86, 101, 115, 0.5)",
                "button_pressed": "rgba(46, 61, 75, 0.5)",
                "label_view": "#acacac",
                "label_projects_header": "#acacac",
                "label_light": "#ffffff",
                "label_light_weight": "regular",
                "label_dark": "#ffffff",
                "label_dark_weight": "bold",
                "label_welcome": "rgb(200, 200, 200)",
                "button_titlebar_hover": "rgba(255, 255, 255, 0.125)",
                "button_titlebar_pressed": "rgba(255, 255, 255, 0.25)"
            }
        }
