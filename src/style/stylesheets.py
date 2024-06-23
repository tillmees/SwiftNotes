import os
import json

from PySide6.QtGui import QFontDatabase

import resources_rc

def get_default_style_dict():
    default_style_dict = {
        "main_background": "#eeeeee",
        "title_bar_background": "#eeeeee",
        "popup_background": "#eeeeee",
        "popup_fields": "#eeeeee",
        "popup_fields_font": "#000000",
        "combobox": "#eeeeee",
        "combobox_border": "#000000",
        "combobox_font": "#000000",
        "sidebar": "#aaaaaa",
        "sidebar_divider": "#000000",
        "sidebar_label": "#000000",
        "task_area": "#eeeeee",
        "project_area": "#eeeeee",
        "button": "#aaaaaa",
        "button_hover": "#aaaaaa",
        "button_pressed": "#aaaaaa",
        "label_view": "#000000",
        "label_projects_header": "#000000",
        "label_light": "#000000",
        "label_light_weight": "regular",
        "label_dark": "#000000",
        "label_dark_weight": "regular",
        "label_welcome": "#000000",
        "button_titlebar_hover": "#aaaaaa",
        "button_titlebar_pressed": "#aaaaaa",
    }
    return default_style_dict

def parse_style_json(
          style_file_name="swiftnotes_style.json",
          layout_style="light",
    ):

        if not os.path.exists(style_file_name):
            return get_default_style_dict()
        
        with open(style_file_name, "r") as file:
            data = json.load(file)
        
        style_dict = get_default_style_dict()

        if layout_style in data:
            for key, value in data[layout_style].items():
                style_dict[key] = value

        return style_dict

def get_stylesheet_dark():
    style_dict = parse_style_json(
            style_file_name="swiftnotes_style.json",
            layout_style="dark"
        )
    style_content = get_stylesheet(style_dict)
    return style_content


def get_stylesheet_light():
    style_dict = parse_style_json(
            style_file_name="swiftnotes_style.json",
            layout_style="light"
        )
    style_content = get_stylesheet(style_dict)
    return style_content


def get_stylesheet(style_dict):
    
    font_id = QFontDatabase.addApplicationFont(u":fonts/fonts/Poppins-Regular.ttf")
    font = QFontDatabase.applicationFontFamilies(font_id)[0] if not font_id == -1 else "Consolas"

    font_id_bold = QFontDatabase.addApplicationFont(u":fonts/fonts/Poppins-SemiBold.ttf")
    font_bold = QFontDatabase.applicationFontFamilies(font_id_bold)[0] if not font_id_bold == -1 else "Consolas"

    style_content = f"""
        #MainWindow {{
        background-color: {style_dict["main_background"]};
        }}

        * {{
            font-family: {font};
            letter-spacing: 0px;
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

        #AddEditDialog {{
            background-color: {style_dict["popup_background"]};
        }}

        #AddEditDialog QLineEdit {{
            border: 1px;
            background-color: {style_dict["popup_fields"]};
            color: {style_dict["popup_fields_font"]};
        }}

        #AddEditDialog QPlainTextEdit {{
            border-radius: 5px;
            background-color: {style_dict["popup_fields"]};
            color: {style_dict["popup_fields_font"]};
        }}

        #AddEditDialog QLabel {{
            color: {style_dict["popup_fields_font"]};
        }}

        #TaskWidget {{
            border-radius: 9px;
        }}
        #TaskWidget QPushButton{{
            background-color: "transparent";
        }} 
        #TaskWidget QLabel{{
            background-color: "transparent";
        }} 
        #TaskWidget QPlainTextEdit{{
            background-color: "transparent";
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

        #scrollAreaWidgetContentsProjectsList {{
            background-color: {style_dict["project_area"]}
        }}

        #ProjectPage QScrollArea {{
            border: none;
        }}
-       """
    return style_content
