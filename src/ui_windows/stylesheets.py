from PySide6.QtGui import QFontDatabase


def get_stylesheet_dark():
    style_content = get_stylesheet(
        main_background="#1e1f22",
        popup_background="#2b2d30",
        popup_fields="#43454a",
        popup_fields_font="#ffffff",
        combobox="#2b2d30",
        combobox_border="#1e1f22",
        combobox_font="#acacac",
        sidebar="#2b2d30",
        sidebar_divider="#1e1f22",
        sidebar_label="#acacac",
        task_area="#2b2d30",
        project_area="#2b2d30",
        button="rgba(0, 0, 0, 0.0)",
        button_hover="rgba(86, 101, 115, 0.5)",
        button_pressed="rgba(46, 61, 75, 0.5)",
        label_view="#acacac",
        label_projects_header="#acacac",
        label_light="#acacac",
        label_dark="#ffffff",
        label_welcome="rgb(200, 200, 200)",
    )
    return style_content


def get_stylesheet_light():
    style_content = get_stylesheet(
        main_background="#eeeeee",
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
        label_light="#ffffff",
        label_dark="#8a8a8a",
        label_welcome="rgb(200, 200, 200)",
    )
    return style_content


def get_stylesheet(
        main_background,
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
        label_dark,
        label_welcome
):
    
    font_id_medium = QFontDatabase.addApplicationFont("ui/fonts/Poppins-Medium.ttf")
    font_medium = QFontDatabase.applicationFontFamilies(font_id_medium)[0] if not font_id_medium == -1 else "Roboto"

    font_id_bold = QFontDatabase.addApplicationFont("ui/fonts/Poppins-SemiBold.ttf")
    font_bold = QFontDatabase.applicationFontFamilies(font_id_bold)[0] if not font_id_bold == -1 else "Roboto"

    style_content = f"""
        #MainWindow {{
        background-color: {main_background};
        }}

        * {{
            font-family: {font_medium};
            letter-spacing: 0px;
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
        }}

        #FullSidebarQWidget #label_dark{{
            color: {label_dark};
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
            color: {label_view};
        }}

        #labelInProgressOutOf {{
            color: {label_view};
        }}

        #labelStuckTestOutOf {{
            color: {label_view};
        }}

        #labelDoneOutOf {{
            color: {label_view};
        }}

        #labelOpen {{
            color: {label_view};
        }}

        #labelInProgress {{
            color: {label_view};
        }}

        #labelStuckTest {{
            color: {label_view};
        }}

        #labelDone {{
            color: {label_view};
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
