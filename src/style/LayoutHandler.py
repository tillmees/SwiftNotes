from PySide6.QtGui import QFontDatabase, QIcon
from PySide6.QtCore import QSize

from settings.StyleSettingsHandler import StyleSettingsHandler
from settings.WindowSettingsHandler import WindowSettingsHandler


class LayoutHandler():

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LayoutHandler, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, ui=None):
        if not hasattr(self, 'initialized'):
            self.initialized = True

            style_settings_handler = StyleSettingsHandler()
            self.layout_dict = {
                "light": style_settings_handler.get_value_for("light"),
                "dark": style_settings_handler.get_value_for("dark")
            }
           
            window_settings_handler = WindowSettingsHandler()
            self.current_layout = window_settings_handler.get_value_for("layout")
            
            self.icons = self.get_icons()
            self.buttons = self.get_buttons(ui)

    def toggle_layout(self, app):
        if self.current_layout == "light":
            self.current_layout = "dark"
        elif self.current_layout == "dark":
            self.current_layout = "light"
        self.set_layout(app)

    def set_layout(self, app):
        style_dict = self.layout_dict[self.current_layout]
        stylesheet_content = self.get_stylesheet_content(style_dict)
        app.setStyleSheet(stylesheet_content)
        self.set_icons()

    def get_layout(self):
        return self.current_layout

    def set_icons(self):
        for button, icon_name in zip(self.buttons, self.icons):
            icon = QIcon()
            icon_path = icon_name + ".svg" if self.current_layout == "light" else icon_name + "-light.svg"
            icon_path = u"toggle-right-light.svg" if icon_path == u"toggle-left-light.svg" else icon_path
            icon.addFile(
                u":/icons/icons/" + icon_path,
                QSize(),
                QIcon.Normal,
                QIcon.Off
            )
            button.setIcon(icon)

    def get_icons(self):
        icons = [
            u"file-plus",
            u"file-plus",
            u"file",
            u"file",
            u"save",
            u"save",
            u"save-as",
            u"save-as",
            u"plus-circle",
            u"plus-circle",
            u"minimize-2",
            u"minimize-2",
            u"plus-square",
            u"plus-square",
            u"menu",
            u"toggle-left",
            u"sliders"
        ]
        return icons
    
    def get_buttons(self, ui):
        buttons = [
            ui.pushButtonIconNew,
            ui.pushButtonFullNew,
            ui.pushButtonIconOpen,
            ui.pushButtonFullOpen,
            ui.pushButtonIconSave,
            ui.pushButtonFullSave,
            ui.pushButtonIconSaveAs,
            ui.pushButtonFullSaveAs,
            ui.pushButtonIconAdd,
            ui.pushButtonFullAdd,
            ui.pushButtonIconClose,
            ui.pushButtonFullClose,
            ui.pushButtonIconTask,
            ui.pushButtonFullTask,
            ui.pushButtonToggleMenu,
            ui.pushButtonFullLayout,
            ui.pushButtonSort
        ]
        return buttons

    def get_stylesheet_content(self, style_dict):
        font_id = QFontDatabase.addApplicationFont(u":fonts/fonts/Poppins-Regular.ttf")
        font = QFontDatabase.applicationFontFamilies(font_id)[0] if not font_id == -1 else "Consolas"

        font_id_bold = QFontDatabase.addApplicationFont(u":fonts/fonts/Poppins-SemiBold.ttf")
        font_bold = QFontDatabase.applicationFontFamilies(font_id_bold)[0] if not font_id_bold == -1 else "Consolas"

        stylesheet_content = f"""
            #MainWindow {{
            background-color: {style_dict["main_background"]};
            }}

            * {{
                font-family: {font};
            }}

            #TopBarQWidget QPushButton{{
                height: 30px;
                width: 30px;
                border: none;
            }}

            #TopBarQWidget QPushButton:hover {{
                background-color: {style_dict["button_hover"]};
            }}

            #TopBarQWidget QPushButton:pressed {{
                background-color: {style_dict["button_pressed"]};
            }}

            #IconSidebarQWidget {{
                background-color: {style_dict["sidebar"]};
                width: 50px;
            }}

            #IconSidebarQWidget QPushButton{{
                height: 30px;
                width: 30px;
                border: none;
                background-color: {style_dict["button"]};
                border-radius: 4px;
            }}

            #IconSidebarQWidget QPushButton:hover{{
                background-color: {style_dict["button_hover"]};
                border-radius: 4px;
            }}

            #IconSidebarQWidget QPushButton:pressed{{
                background-color: {style_dict["button_pressed"]};
                border-radius: 4px;
            }}

            #IconSidebarQWidget QFrame {{
                color: {style_dict["sidebar_divider"]};
            }}

            #FullSidebarQWidget #labelVersion {{
                color: {style_dict["sidebar_label"]};
                font-size: 11px;
            }}

            #FullSidebarQWidget {{
                background-color: {style_dict["sidebar"]};
                width: 250px;
            }}

            #FullSidebarQWidget QPushButton{{
                height: 30px;
                width: 30px;
                border: none;
                color: {style_dict["sidebar_label"]};
                background-color: {style_dict["button"]};
                border-radius: 4px;
            }}

            #FullSidebarQWidget QPushButton:hover{{
                background-color: {style_dict["button_hover"]};
                border-radius: 4px;
            }}

            #FullSidebarQWidget QPushButton:pressed{{
                background-color: {style_dict["button_pressed"]};
                border-radius: 4px;
            }}

            #FullSidebarQWidget QFrame{{
                color: {style_dict["sidebar_divider"]};
            }}

            #FullSidebarQWidget #label_light{{
                color: {style_dict["label_light"]};
                font-weight: {style_dict["label_light_weight"]};
            }}

            #FullSidebarQWidget #label_dark{{
                color: {style_dict["label_dark"]};
                font-weight: {style_dict["label_dark_weight"]};
            }}

            #labelWelcome {{
                font-size: 24px;
                color: {style_dict["label_welcome"]};
            }}

            #labelWelcomeDrop {{
                font-size: 14px;
                color: {style_dict["label_view"]};
            }}

            #TaskPage QScrollArea {{
                background-color: {style_dict["task_area"]};
                border: none;
            }}

            #labelOpenOutOf {{
                color: {style_dict["sidebar_label"]};
            }}

            #labelInProgressOutOf {{
                color: {style_dict["sidebar_label"]};
            }}

            #labelStuckTestOutOf {{
                color: {style_dict["sidebar_label"]};
            }}

            #labelDoneOutOf {{
                color: {style_dict["sidebar_label"]};
            }}

            #labelOpen {{
                color: {style_dict["sidebar_label"]};
            }}

            #labelInProgress {{
                color: {style_dict["sidebar_label"]};
            }}

            #labelStuckTest {{
                color: {style_dict["sidebar_label"]};
            }}

            #labelDone {{
                color: {style_dict["sidebar_label"]};
            }}

            #EditDialog {{
                background-color: {style_dict["popup_background"]};
            }}

            #EditDialog QLineEdit {{
                border: 1px;
                background-color: {style_dict["popup_fields"]};
                color: {style_dict["popup_fields_font"]};
            }}

            #EditDialog QPlainTextEdit {{
                border-radius: 5px;
                background-color: {style_dict["popup_fields"]};
                color: {style_dict["popup_fields_font"]};
            }}

            #EditDialog QLabel {{
                color: {style_dict["popup_fields_font"]};
            }}

            #AddDialog {{
                background-color: {style_dict["popup_background"]};
            }}

            #AddDialog QLineEdit {{
                border: 1px;
                background-color: {style_dict["popup_fields"]};
                color: {style_dict["popup_fields_font"]};
            }}

            #AddDialog QPlainTextEdit {{
                border-radius: 5px;
                background-color: {style_dict["popup_fields"]};
                color: {style_dict["popup_fields_font"]};
            }}

            #AddDialog QLabel {{
                color: {style_dict["popup_fields_font"]};
            }}

            #TaskWidget {{
                border-radius: 9px;
            }}

            #ProjectWidget {{
                border-radius: 9px;
            }}

            #labelProjectTitle {{
                font-family: {font_bold};
                color: #000000;
            }}

            #labelTask {{
                font-family: {font_bold};
                color: #000000;
            }}

            #labelDelTask {{
                font-family: {font_bold};
                color: #000000;
            }}

            #labelTaskCreated {{
                font-size: 11px;
                color: #ffffff;
            }}

            #TaskWidget QPushButton{{
                height: 30px;
                width: 30px;
                border: none;
            }}        
            
            #comboBoxProjects {{
                background-color: {style_dict["combobox"]};
                border: 1px solid {style_dict["combobox_border"]};
                padding-left: 10px;
                color: {style_dict["combobox_font"]};
            }}

            #comboBoxProjects::drop-down {{
                border: 0px;
            }}
            
            #comboBoxProjects::down-arrow {{
                image: url(:/icons/icons/chevron-down-light.svg);
                width: 16px;
            }}
            
            #comboBoxProjects QListView {{
                border: 1px solid {style_dict["combobox_border"]};
                padding: 5px;
                background-color: {style_dict["combobox"]}; 
                outline: 0px;
                color: {style_dict["combobox_font"]};
            }}
            
            #comboBoxProjects QListView::item {{
                padding-left: 10px;
                background-color: {style_dict["combobox"]};
                color: {style_dict["sidebar_label"]};
            }}
            
            #comboBoxProjects QListView::item::hover {{
                background-color: {style_dict["button_hover"]}; 
                color: {style_dict["sidebar_label"]};
            }}
            
            #comboBoxProjects QListView::item::pressed{{
                background-color: {style_dict["button_pressed"]};
            }}

            #scrollAreaWidgetContentsOpen {{
                background-color: {style_dict["task_area"]};
            }}

            #scrollAreaWidgetContentsInProgress {{
                background-color: {style_dict["task_area"]};
            }}

            #scrollAreaWidgetContentsStuckTest {{
                background-color: {style_dict["task_area"]};
            }}

            #scrollAreaWidgetContentsDone {{
                background-color: {style_dict["task_area"]};
            }}

            #scrollAreaProjectsList {{
                background-color: {style_dict["project_area"]}
            }}

            #scrollAreaWidgetContentsProjectsList {{
                background-color: {style_dict["project_area"]}
            }}

            #ProjectPage QLabel {{
                color: {style_dict["label_projects_header"]};
            }}

            #ProjectPage QToolButton{{
                height: 30px;
                width: 30px;
                border: none;
            }}

            #ProjectPage QToolButton:hover {{
                background-color: {style_dict["button_hover"]};
                border-radius: 4px;
            }}

            #ProjectPage QToolButton:pressed {{
                background-color: {style_dict["button_pressed"]};
                border-radius: 4px;
            }}

            #ProjectPage QPushButton{{
                height: 30px;
                width: 30px;
                border: none;
            }}

            #ProjectPage QPushButton:hover {{
                background-color: {style_dict["button_hover"]};
                border-radius: 4px;
            }}

            #ProjectPage QPushButton:pressed {{
                background-color: {style_dict["button_pressed"]};
                border-radius: 4px;
            }}

            #ProjectPage QScrollArea {{
                border: none;
            }}
        """
        return stylesheet_content
