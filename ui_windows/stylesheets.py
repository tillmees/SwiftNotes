def get_stylesheet_dark():
    style_content = get_stylesheet(
        main_background="#1e1f22",
        popup_background="#2b2d30",
        popup_fields="#43454a",
        popup_fields_font="#ffffff",
        sidebar="#2b2d30",
        sidebar_divider="#1e1f22",
        sidebar_label="#acacac",
        task_area="#2b2d30",
        project_area="#2b2d30",
        button_hover="rgba(86, 101, 115, 0.5)",
        button_pressed="rgba(46, 61, 75, 0.5)",
        label_view="#acacac",
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
        sidebar="rgb(200, 200, 200)",
        sidebar_divider="rgb(180, 180, 180)",
        sidebar_label="#000000",
        task_area="rgb(245, 245, 245)",
        project_area="rgb(245, 245, 245)",
        button_hover="rgba(86, 101, 115, 0.5)",
        button_pressed="rgba(46, 61, 75, 0.5)",
        label_view="rgba(86, 101, 115, 0.5)",
        label_light="#000000",
        label_dark="#8a8a8a",
        label_welcome="rgb(200, 200, 200)",
    )
    return style_content


def get_stylesheet(
        main_background,
        popup_background,
        popup_fields,
        popup_fields_font,
        sidebar,
        sidebar_divider,
        sidebar_label,
        task_area,
        project_area,
        button_hover,
        button_pressed,
        label_view,
        label_light,
        label_dark,
        label_welcome
):
    style_content = f"""
        #MainWindow {{
        background-color: {main_background};
        }}

        * {{
            font-family: Consolas;
            letter-spacing: 0px;
        }}

        #TopBarQWidget QPushButton{{
            height: 30px;
            width: 30px;
            border: none;
        }}

        #TopBarQWidget QPushButton:hover {{
            background-color: {button_hover};
            border-radius: 4px;
        }}

        #TopBarQWidget QPushButton:pressed {{
            background-color: {button_pressed};
            border-radius: 4px;
        }}

        #IconSidebarQWidget {{
            background-color: {sidebar};
            width: 50px;
        }}

        #IconSidebarQWidget QPushButton{{
            height: 30px;
            width: 30px;
            border: none;
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
            border-radius: 5px;
        }}

        #ProjectWidget {{
            border-radius: 5px;
        }}

        #labelTask {{
            color: #000000;
            font-size: 14px;
            font-weight: bold;
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
            color: {label_view};
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
