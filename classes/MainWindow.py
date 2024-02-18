import os
import pickle
from enum import Enum

from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from ui_windows.main_ui import Ui_MainWindow

from classes.AddProject import AddProject
from classes.AddTask import AddTask
from classes.InfoProject import InfoProject
from classes.InfoTask import InfoTask
from classes.ProjectHandler import ProjectHandler

from functions import ComboBoxFunctions
from functions import ScrollAreaFunctions


EMPTY_PROJECT = " "


class StackedWidgetState(Enum):
    WELCOME = 0
    TASK_VIEW = 1
    PROJECT_VIEW = 2


class MainWindow(QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_project_window = AddProject()
        self.add_task_window = AddTask()
        self.info_project_window = InfoProject()
        self.info_task_window = InfoTask()
        self.project_handler = ProjectHandler()
        self.file_name = None

        self.stacked_widget_state = None

        self.setup_for_clean_start()
        self.setup_signals()
        self.layout = None
        self.use_light_mode()

    def on_add_project_pushed(self):
        self.add_project_window.clear_edits()
        self.add_project_window.setWindowTitle("Add Project")
        result = self.add_project_window.exec()
        if result == QDialog.Accepted:
            project = self.add_project_window.get_project_from_user_input()
            self.project_handler.add_project(project)
            ComboBoxFunctions.update_combo_box(
                self.ui.comboBoxProjects,
                project.get_title()
            )
            self.update_task_view()

    def on_close_project_pushed(self):
        self.project_handler.set_current_project(None)
        self.show_project_screen()

    def on_info_project_pushed(self):
        self.info_project_window.execute(
            self.project_handler.get_current_project()
        )

    def on_edit_project_pushed(self):
        current_project = self.project_handler.get_current_project()
        old_title = current_project.get_title()
        old_description = current_project.get_description()

        self.add_project_window.clear_edits()
        self.add_project_window.setWindowTitle("Edit Project")
        self.add_project_window.set_title(old_title)
        self.add_project_window.set_description(old_description)

        result = self.add_project_window.exec()
        if result == QDialog.Accepted:
            new_title = self.add_project_window.get_title()
            new_description = self.add_project_window.get_description()
            current_project.set_title(new_title)
            current_project.set_description(new_description)
            self.project_handler.project_edited(
                old_title,
                new_title,
                new_description
            )
            ComboBoxFunctions.update_combo_box(
                self.ui.comboBoxProjects,
                new_title
            )
            ComboBoxFunctions.delete_string_from_combo_box(
                self.ui.comboBoxProjects,
                old_title
            )
            self.update_task_view()

    def on_add_task_pushed(self):
        result = self.add_task_window.exec()
        if result == QDialog.Accepted:
            current_project = self.project_handler.get_current_project()
            task_creator = \
                self.add_task_window.get_task_creator_from_user_input()
            current_project.add_task(task_creator)
            self.update_task_view()

    def on_project_changed_in_combo_box(self):
        project_title_in_combo_box = ComboBoxFunctions.get_current_project(
            self.ui.comboBoxProjects
        )
        if project_title_in_combo_box == "":
            return
        selected_project = project_title_in_combo_box if \
            project_title_in_combo_box != " " else None
        self.project_handler.set_current_project(selected_project)
        self.on_selected_project_changed()

    def on_selected_project_changed(self):
        current_project = self.project_handler.get_current_project()
        if current_project is None:
            self.show_welcome_screen()
        elif current_project is not EMPTY_PROJECT:
            self.show_task_screen()
            self.update_task_view()

    def show_welcome_screen(self):
        self.stacked_widget_state = StackedWidgetState.WELCOME.value
        self.ui.TaskWindowstackedWidget.setCurrentIndex(
            self.stacked_widget_state
        )
        self.ui.comboBoxProjects.hide()
        self.ui.pushButtonIconClose.hide()
        self.ui.pushButtonIconInfo.hide()
        self.ui.pushButtonIconEdit.hide()
        self.ui.pushButtonFullClose.hide()
        self.ui.pushButtonFullInfo.hide()
        self.ui.pushButtonFullEdit.hide()
        self.ui.pushButtonIconTask.hide()
        self.ui.pushButtonFullTask.hide()

    def show_task_screen(self):
        ComboBoxFunctions.delete_whitespace_string_from_combo_box(
            self.ui.comboBoxProjects
        )
        self.stacked_widget_state = StackedWidgetState.TASK_VIEW.value
        self.ui.TaskWindowstackedWidget.setCurrentIndex(
            self.stacked_widget_state
        )
        self.ui.comboBoxProjects.show()
        self.ui.pushButtonIconClose.show()
        self.ui.pushButtonIconInfo.show()
        self.ui.pushButtonIconEdit.show()
        self.ui.pushButtonFullClose.show()
        self.ui.pushButtonFullInfo.show()
        self.ui.pushButtonFullEdit.show()
        self.ui.pushButtonIconTask.show()
        self.ui.pushButtonFullTask.show()

    def show_project_screen(self):
        ComboBoxFunctions.add_whitespace_string_to_combo_box(
            self.ui.comboBoxProjects
        )
        self.stacked_widget_state = StackedWidgetState.PROJECT_VIEW.value
        self.ui.TaskWindowstackedWidget.setCurrentIndex(
            self.stacked_widget_state
        )
        self.ui.comboBoxProjects.show()
        self.ui.pushButtonIconClose.hide()
        self.ui.pushButtonIconInfo.hide()
        self.ui.pushButtonIconEdit.hide()
        self.ui.pushButtonFullClose.hide()
        self.ui.pushButtonFullInfo.hide()
        self.ui.pushButtonFullEdit.hide()
        self.ui.pushButtonIconTask.hide()
        self.ui.pushButtonFullTask.hide()

    def setup_for_clean_start(self):
        self.file_name = None
        self.ui.FullSidebarQWidget.hide()
        self.ui.pushButtonFullTask.hide()
        self.ui.pushButtonIconTask.hide()

        self.ui.TaskWindowstackedWidget.setCurrentIndex(0)
        self.ui.comboBoxProjects.hide()
        self.ui.pushButtonIconClose.hide()
        self.ui.pushButtonIconInfo.hide()
        self.ui.pushButtonIconEdit.hide()
        self.ui.pushButtonFullClose.hide()
        self.ui.pushButtonFullInfo.hide()
        self.ui.pushButtonFullEdit.hide()

        self.ui.scrollAreaWidgetContentsOpen.layout().setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContentsInProgress.layout().setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContentsStuckTest.layout().setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContentsDone.layout().setAlignment(Qt.AlignTop)

        self.stacked_widget_state = StackedWidgetState.WELCOME.value

    def setup_signals(self):
        self.ui.pushButtonIconNew.clicked.connect(
            self.on_new_pushed
        )
        self.ui.pushButtonFullNew.clicked.connect(
            self.on_new_pushed
        )
        self.ui.pushButtonIconOpen.clicked.connect(
            self.on_open_pushed
        )
        self.ui.pushButtonFullOpen.clicked.connect(
            self.on_open_pushed
        )
        self.ui.pushButtonIconSave.clicked.connect(
            self.on_save_pushed
        )
        self.ui.pushButtonFullSave.clicked.connect(
            self.on_save_pushed
        )
        self.ui.pushButtonIconSaveAs.clicked.connect(
            self.on_save_as_pushed
        )
        self.ui.pushButtonFullSaveAs.clicked.connect(
            self.on_save_as_pushed
        )

        ###
        self.ui.pushButtonIconAdd.clicked.connect(
            self.on_add_project_pushed
        )
        self.ui.pushButtonFullAdd.clicked.connect(
            self.on_add_project_pushed
        )

        self.ui.pushButtonIconInfo.clicked.connect(
            self.on_info_project_pushed
        )
        self.ui.pushButtonFullInfo.clicked.connect(
            self.on_info_project_pushed
        )

        self.ui.pushButtonIconEdit.clicked.connect(
            self.on_edit_project_pushed
        )
        self.ui.pushButtonFullEdit.clicked.connect(
            self.on_edit_project_pushed
        )

        self.ui.pushButtonIconClose.clicked.connect(
            self.on_close_project_pushed
        )
        self.ui.pushButtonFullClose.clicked.connect(
            self.on_close_project_pushed
        )

        self.ui.pushButtonIconTask.clicked.connect(
            self.on_add_task_pushed
        )
        self.ui.pushButtonFullTask.clicked.connect(
            self.on_add_task_pushed
        )

        self.ui.comboBoxProjects.currentIndexChanged.connect(
            self.on_project_changed_in_combo_box
        )

        self.ui.pushButtonFullLayout.clicked.connect(
            self.on_toggle_layout
        )

    def on_new_pushed(self):
        self.project_handler = ProjectHandler()
        self.ui.comboBoxProjects.clear()
        self.setup_for_clean_start()

    def on_open_pushed(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        self.file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "",
            "Swift Note Files (" "*.todo);;All Files (*)",
            options=options
        )

        if not self.file_name:
            return

        with open(self.file_name, "rb") as file:
            self.project_handler = pickle.load(file)

        self.project_handler.set_current_project(None)
        self.ui.comboBoxProjects.clear()
        if len(self.project_handler.projects):
            projects = [project for project in
                        self.project_handler.projects.keys()]
            self.on_close_project_pushed()
            self.ui.comboBoxProjects.addItems(projects)

    def on_save_pushed(self):
        if self.file_name is None:
            self.on_save_as_pushed()

        else:
            with open(self.file_name, "wb") as file:
                pickle.dump(self.project_handler, file)

    def on_save_as_pushed(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        self.file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "",
            "Swift Note Files (" "*.todo);;All Files (*)",
            options=options
        )

        if not self.file_name:
            return

        with open(self.file_name, "wb") as file:
            pickle.dump(self.project_handler, file)

    def get_task_signal_functions(self):
        return [
            self.task_info_in_scroll_area,
            self.task_move_in_scroll_area,
            self.task_edit_in_scroll_area,
            self.task_deleted_in_scroll_area
        ]

    def task_info_in_scroll_area(self, info_tasks_hash):
        current_project = self.project_handler.get_current_project()
        task = current_project.get_task_by_hash(info_tasks_hash)
        self.info_task_window.execute(task)

    def task_move_in_scroll_area(self, move_tasks_hash, new_task_bin):
        current_project = self.project_handler.get_current_project()
        current_project.move_task_by_hash_in_bin(move_tasks_hash, new_task_bin)
        self.update_task_view()

    def task_edit_in_scroll_area(self, edit_tasks_hash, edit_fields):
        current_project = self.project_handler.get_current_project()
        task = current_project.get_task_by_hash(edit_tasks_hash)
        new_title, new_description, new_color_string = edit_fields
        task.set_title(new_title)
        task.set_description(new_description)
        task.set_color_string(new_color_string)
        self.update_task_view()

    def task_deleted_in_scroll_area(self, deleted_tasks_hash):
        current_project = self.project_handler.get_current_project()
        current_project.remove_task_by_hash(deleted_tasks_hash)

    def update_task_counter(self):
        current_project = self.project_handler.get_current_project()
        task_count = current_project.get_task_count()
        open_count = current_project.get_task_count_in("open")
        in_progress_count = current_project.get_task_count_in("in progress")
        stuck_test_count = current_project.get_task_count_in("stuck/test")
        done_count = current_project.get_task_count_in("done")

        self.ui.labelOpenOutOf.setText(
            f"{open_count}/{task_count}")
        self.ui.labelInProgressOutOf.setText(
            f"{in_progress_count}/{task_count}")
        self.ui.labelStuckTestOutOf.setText(
            f"{stuck_test_count}/{task_count}")
        self.ui.labelDoneOutOf.setText(
            f"{done_count}/{task_count}")

    def update_task_view(self):
        current_project = self.project_handler.get_current_project()

        ScrollAreaFunctions.clear_scroll_area(
            self.ui.scrollAreaWidgetContentsOpen
        )
        ScrollAreaFunctions.clear_scroll_area(
            self.ui.scrollAreaWidgetContentsInProgress
        )
        ScrollAreaFunctions.clear_scroll_area(
            self.ui.scrollAreaWidgetContentsStuckTest
        )
        ScrollAreaFunctions.clear_scroll_area(
            self.ui.scrollAreaWidgetContentsDone
        )

        ScrollAreaFunctions.fill_scroll_area(
            self.ui.scrollAreaWidgetContentsOpen,
            current_project.get_tasks_in("open"),
            self.get_task_signal_functions()
        )
        ScrollAreaFunctions.fill_scroll_area(
            self.ui.scrollAreaWidgetContentsInProgress,
            current_project.get_tasks_in("in progress"),
            self.get_task_signal_functions()
        )
        ScrollAreaFunctions.fill_scroll_area(
            self.ui.scrollAreaWidgetContentsStuckTest,
            current_project.get_tasks_in("stuck/test"),
            self.get_task_signal_functions()
        )
        ScrollAreaFunctions.fill_scroll_area(
            self.ui.scrollAreaWidgetContentsDone,
            current_project.get_tasks_in("done"),
            self.get_task_signal_functions()
        )
        self.update_task_counter()

    def use_dark_mode(self):
        with open(os.path.join("ui_windows", "style_dark.qss")) as style_file:
            style_sheet = style_file.read()
        self.app.setStyleSheet(style_sheet)
        icon_paths = [
            u"file-plus-light.svg",
            u"file-plus-light.svg",
            u"file-light.svg",
            u"file-light.svg",
            u"save-light.svg",
            u"save-light.svg",
            u"save-as-light.svg",
            u"save-as-light.svg",
            u"plus-circle-light.svg",
            u"plus-circle-light.svg",
            u"info-light.svg",
            u"info-light.svg",
            u"edit-3-light.svg",
            u"edit-3-light.svg",
            u"minimize-2-light.svg",
            u"minimize-2-light.svg",
            u"plus-square-light.svg",
            u"plus-square-light.svg",
            u"menu-light.svg",
            u"toggle-right-light.svg",
        ]

        self.change_layout_mode(icon_paths)
        self.layout = "dark"

    def use_light_mode(self):
        with open(os.path.join("ui_windows", "style.qss")) as style_file:
            style_sheet = style_file.read()
        self.app.setStyleSheet(style_sheet)
        icon_paths = [
            u"file-plus.svg",
            u"file-plus.svg",
            u"file.svg",
            u"file.svg",
            u"save.svg",
            u"save.svg",
            u"save-as.svg",
            u"save-as.svg",
            u"plus-circle.svg",
            u"plus-circle.svg",
            u"info.svg",
            u"info.svg",
            u"edit-3.svg",
            u"edit-3.svg",
            u"minimize-2.svg",
            u"minimize-2.svg",
            u"plus-square.svg",
            u"plus-square.svg",
            u"menu.svg",
            u"toggle-left.svg",
        ]

        self.change_layout_mode(icon_paths)
        self.layout = "light"

    def change_layout_mode(self, icon_paths):
        buttons = [
            self.ui.pushButtonIconNew,
            self.ui.pushButtonFullNew,
            self.ui.pushButtonIconOpen,
            self.ui.pushButtonFullOpen,
            self.ui.pushButtonIconSave,
            self.ui.pushButtonFullSave,
            self.ui.pushButtonIconSaveAs,
            self.ui.pushButtonFullSaveAs,
            self.ui.pushButtonIconAdd,
            self.ui.pushButtonFullAdd,
            self.ui.pushButtonIconInfo,
            self.ui.pushButtonFullInfo,
            self.ui.pushButtonIconEdit,
            self.ui.pushButtonFullEdit,
            self.ui.pushButtonIconClose,
            self.ui.pushButtonFullClose,
            self.ui.pushButtonIconTask,
            self.ui.pushButtonFullTask,
            self.ui.pushButtonToggleMenu,
            self.ui.pushButtonFullLayout
        ]
        for button, icon_path in zip(buttons, icon_paths):
            icon = QIcon()
            icon.addFile(u":/icons/icons/" + icon_path,
                         QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon)

    def on_toggle_layout(self):
        if self.layout == "dark":
            self.use_light_mode()
        elif self.layout == "light":
            self.use_dark_mode()
