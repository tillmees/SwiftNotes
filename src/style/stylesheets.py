from PySide6.QtGui import QFontDatabase

import resources_rc


def get_stylesheet_dark():
    style_content = get_stylesheet(
        main_background="#1e1f22",
        title_bar_background="#1e1f22",
        popup_background="#2b2d30",
        popup_fields="#43454a",
        popup_fields_font="#ffffff",
        combobox="#2b2d30",
        combobox_border="#1e1f22",
        combobox_font="#ffffff",
        sidebar="#2b2d30",
        sidebar_divider="#1e1f22",
        sidebar_label="#ffffff",
        task_area="#2b2d30",
        project_area="#2b2d30",
        button="rgba(0, 0, 0, 0.0)",
        button_hover="rgba(86, 101, 115, 0.5)",
        button_pressed="rgba(46, 61, 75, 0.5)",
        label_view="#acacac",
        label_projects_header="#acacac",
        label_light="#ffffff",
        label_light_weight="regular",
        label_dark="#ffffff",
        label_dark_weight="bold",
        label_welcome="rgb(200, 200, 200)",
        button_titlebar_hover="rgba(255, 255, 255, 0.125)",
        button_titlebar_pressed="rgba(255, 255, 255, 0.25)"
    )
    return style_content


def get_stylesheet_light():
    style_content = get_stylesheet(
        main_background="#eeeeee",
        title_bar_background="#eeeeee",
        popup_background="rgb(245, 245, 245)",
        popup_fields="#ffffff",
        popup_fields_font="#000000",
        combobox="#f5f5f5",
        combobox_border="rgb(200, 200, 200)",
        combobox_font="#111111",
        sidebar="rgb(200, 200, 200)",
        sidebar_divider="rgb(180, 180, 180)",
        sidebar_label="#000000",
        task_area="#f5f5f5",
        project_area="#f5f5f5",
        button="rgba(0, 0, 0, 0.0)",
        button_hover="rgba(86, 101, 115, 0.5)",
        button_pressed="rgba(46, 61, 75, 0.5)",
        label_view="rgba(86, 101, 115, 0.5)",
        label_projects_header="#000000",
        label_light="#000000",
        label_light_weight="bold",
        label_dark="#000000",
        label_dark_weight="regular",
        label_welcome="rgb(200, 200, 200)",
        button_titlebar_hover="rgba(0, 0, 0, 0.125)",
        button_titlebar_pressed="rgba(0, 0, 0, 0.25)"
    )
    return style_content


def get_stylesheet(
        main_background,
        title_bar_background,
        popup_background,
        popup_fields,
        popup_fields_font,
        combobox,
        combobox_border,
        combobox_font,
        sidebar,
        sidebar_divider,
        sidebar_label,
        task_area,
        project_area,
        button,
        button_hover,
        button_pressed,
        label_view,
        label_projects_header,
        label_light,
        label_light_weight,
        label_dark,
        label_dark_weight,
        label_welcome,
        button_titlebar_hover,
        button_titlebar_pressed
):
    
    font_id = QFontDatabase.addApplicationFont(u":fonts/fonts/Poppins-Regular.ttf")
    font = QFontDatabase.applicationFontFamilies(font_id)[0] if not font_id == -1 else "Consolas"

    font_id_bold = QFontDatabase.addApplicationFont(u":fonts/fonts/Poppins-SemiBold.ttf")
    font_bold = QFontDatabase.applicationFontFamilies(font_id_bold)[0] if not font_id_bold == -1 else "Consolas"

    style_content = f"""
        #MainWindow {{
        background-color: {main_background};
        }}

        #MainWindow::title {{background-color: #3498db;}}

        * {{
            font-family: {font};
            letter-spacing: 0px;
        }}

        #backgroundTitleBar {{
            background-color: {title_bar_background};
        }}

        #buttonWindowResize {{
            background-color: transparent;
            border: none;
        }}
        #buttonWindowResize:hover {{
            background-color: {button_titlebar_hover};
        }}
        #buttonWindowResize:pressed {{
            background-color: {button_titlebar_pressed};
        }}

        #buttonCloseWindow {{
            background-color: transparent;
            border: none;
        }}
        #buttonCloseWindow:hover {{
            background-color: rgba(235, 30, 20, 1.0);
        }}
        #buttonCloseWindow:pressed {{
            background-color: rgba(235, 30, 20, 0.5);
        }}

        #windowTitle {{
            color: {sidebar_label};
            font-size: 12px;
            font-family: Segoe UI;
        }}

        #TopBarQWidget QPushButton{{
            height: 30px;
            width: 30px;
            border: none;
        }}

        #TopBarQWidget QPushButton:hover {{
            background-color: {button_hover};
        }}

        #TopBarQWidget QPushButton:pressed {{
            background-color: {button_pressed};
        }}

        #IconSidebarQWidget {{
            background-color: {sidebar};
            width: 50px;
        }}

        #IconSidebarQWidget QPushButton{{
            height: 30px;
            width: 30px;
            border: none;
            background-color: {button};
            border-radius: 4px;
        }}

        #IconSidebarQWidget QPushButton:hover{{
            background-color: {button_hover};
            border-radius: 4px;
        }}

        #IconSidebarQWidget QPushButton:pressed{{
            background-color: {button_pressed};
            border-radius: 4px;
        }}

        #IconSidebarQWidget QFrame {{
            color: {sidebar_divider};
        }}

        #FullSidebarQWidget #labelVersion {{
            color: {sidebar_label};
            font-size: 11px;
        }}

        #FullSidebarQWidget {{
            background-color: {sidebar};
            width: 250px;
        }}

        #FullSidebarQWidget QPushButton{{
            height: 30px;
            width: 30px;
            border: none;
            color: {sidebar_label};
            background-color: {button};
            border-radius: 4px;
        }}

        #FullSidebarQWidget QPushButton:hover{{
            background-color: {button_hover};
            border-radius: 4px;
        }}

        #FullSidebarQWidget QPushButton:pressed{{
            background-color: {button_pressed};
            border-radius: 4px;
        }}

        #FullSidebarQWidget QFrame{{
            color: {sidebar_divider};
        }}

        #FullSidebarQWidget #label_light{{
            color: {label_light};
            font-weight: {label_light_weight};
        }}

        #FullSidebarQWidget #label_dark{{
            color: {label_dark};
            font-weight: {label_dark_weight};
        }}

        #labelWelcome {{
            font-size: 24px;
            color: {label_welcome};
        }}

        #labelWelcomeDrop {{
            font-size: 14px;
            color: {label_view};
        }}

        #TaskPage QScrollArea {{
            background-color: {task_area};
            border: none;
        }}

        #labelOpenOutOf {{
            color: {sidebar_label};
        }}

        #labelInProgressOutOf {{
            color: {sidebar_label};
        }}

        #labelStuckTestOutOf {{
            color: {sidebar_label};
        }}

        #labelDoneOutOf {{
            color: {sidebar_label};
        }}

        #labelOpen {{
            color: {sidebar_label};
        }}

        #labelInProgress {{
            color: {sidebar_label};
        }}

        #labelStuckTest {{
            color: {sidebar_label};
        }}

        #labelDone {{
            color: {sidebar_label};
        }}

        #AddEditDialog {{
            background-color: {popup_background};
        }}

        #AddEditDialog QLineEdit {{
            border: 1px;
            background-color: {popup_fields};
            color: {popup_fields_font};
        }}

        #AddEditDialog QPlainTextEdit {{
            border-radius: 5px;
            background-color: {popup_fields};
            color: {popup_fields_font};
        }}

        #AddEditDialog QLabel {{
            color: {popup_fields_font};
        }}

        #InfoDialog {{
            background-color: {popup_background};
        }}

        #InfoDialog QLabel {{
            color: {popup_fields_font};
        }}

        #InfoDialog QPlainTextEdit {{
            border-radius: 5px;
            background-color: {popup_fields};
            color: {popup_fields_font};
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
            background-color: {combobox}; 
            border: 1px solid {combobox_border};
            padding-left: 10px;
            color: {combobox_font};
        }}
        
        #comboBoxProjects::drop-down {{
            border: 0px;
        }}

        #comboBoxProjects::down-arrow {{
            image: url(:/icons/icons/chevron-down-light.svg);
            width: 16px;
        }}
        
        #comboBoxProjects QListView {{
            border: 1px solid {combobox_border};
            padding: 5px;
            background-color: {combobox}; 
            outline: 0px;
            color: {combobox_font};
        }}
        
        #comboBoxProjects QListView::item {{
            padding-left: 10px;
            background-color: {combobox};
            color: {sidebar_label};
        }}
        
        #comboBoxProjects QListView::item::hover {{
            background-color: {button_hover}; 
            color: {sidebar_label};
        }}
        
        #comboBoxProjects QListView::item::pressed{{
            background-color: {button_pressed};
        }}

        #scrollAreaWidgetContentsOpen {{
            background-color: {task_area};
        }}

        #scrollAreaWidgetContentsInProgress {{
            background-color: {task_area};
        }}

        #scrollAreaWidgetContentsStuckTest {{
            background-color: {task_area};
        }}

        #scrollAreaWidgetContentsDone {{
            background-color: {task_area};
        }}

        #ProjectPage QLabel {{
            color: {label_projects_header};
        }}

        #ProjectPage QToolButton{{
            height: 30px;
            width: 30px;
            border: none;
        }}

        #ProjectPage QToolButton:hover {{
            background-color: {button_hover};
            border-radius: 4px;
        }}

        #ProjectPage QToolButton:pressed {{
            background-color: {button_pressed};
            border-radius: 4px;
        }}

        #ProjectPage QPushButton{{
            height: 30px;
            width: 30px;
            border: none;
        }}

        #ProjectPage QPushButton:hover {{
            background-color: {button_hover};
            border-radius: 4px;
        }}

        #ProjectPage QPushButton:pressed {{
            background-color: {button_pressed};
            border-radius: 4px;
        }}

        #scrollAreaWidgetContentsProjectsList {{
            background-color: {project_area}
        }}

        #ProjectPage QScrollArea {{
            border: none;
        }}
        """
    return style_content
