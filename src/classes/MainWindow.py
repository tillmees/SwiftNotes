import pickle
from enum import Enum

from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from ui_windows.main_ui import Ui_MainWindow
from ui_windows.stylesheets import get_stylesheet_dark, get_stylesheet_light

from classes.EditWindow import AddEditWindow
from classes.InfoWindow import InfoWindow
from classes.ProjectHandler import ProjectHandler

from functions import ComboBoxFunctions
from functions import ScrollAreaFunctions


EMPTY_PROJECT = " "


class StackedWidgetState(Enum):
    WELCOME = 0
    TASK_VIEW = 1
    PROJECT_VIEW = 2


class MainWindow(QMainWindow):
    def __init__(self, app, version):
        super(MainWindow, self).__init__()

        self.app = app
        self.version = version

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_edit_window = AddEditWindow()
        self.info_window = InfoWindow()
        self.project_handler = ProjectHandler()
        self.file_name = None
        self.is_unsaved_changes = None

        self.stacked_widget_state = None
        self.project_sort_member = None

        self.setup_for_clean_start()
        self.setup_signals()
        self.layout = None
        self.use_light_mode()
        self.update_title()

    def update_title(self):
        title = "SwiftNotes"

        if self.file_name is not None and self.is_unsaved_changes:
            title += f" - *{self.file_name}"
        elif self.file_name is not None and not self.is_unsaved_changes:
            title += f" - {self.file_name}"
        elif self.file_name is None and self.is_unsaved_changes:
            title += f" - *New File"
        elif self.file_name is None and not self.is_unsaved_changes:
            title += f" - New File"

        self.setWindowTitle(title)

    def mark_unsaved_changes(self):
        self.is_unsaved_changes = True
        self.update_title()

    def on_add_project_pushed(self):
        self.add_edit_window.clear_edits()
        self.add_edit_window.setWindowTitle("Add Project")
        result = self.add_edit_window.exec_add()
        if result == QDialog.Accepted:
            project = self.add_edit_window.get_project_from_user_input()
            self.project_handler.add_project(project)
            ComboBoxFunctions.update_combo_box(
                self.ui.comboBoxProjects,
                project.get_title()
            )
            self.update_task_view()
            self.mark_unsaved_changes()

    def on_close_project_pushed(self):
        self.project_handler.set_current_project(None)
        self.update_project_view()
        self.show_project_screen()

    def on_info_project_pushed(self, project):
        self.info_window.setWindowTitle("Info Project")
        self.info_window.execute(
            project
        )

    def on_edit_project_pushed(self, project):
        old_title = project.get_title()
        old_description = project.get_description()
        old_color_string = project.get_color_string()

        self.add_edit_window.clear_edits()
        self.add_edit_window.setWindowTitle("Edit Project")
        self.add_edit_window.set_title(old_title)
        self.add_edit_window.set_description(old_description)
        self.add_edit_window.set_color_checked_box(old_color_string)

        result = self.add_edit_window.exec_edit()
        if result == QDialog.Accepted:
            new_title = self.add_edit_window.get_title()
            new_description = self.add_edit_window.get_description()
            new_color_string = self.add_edit_window.get_color_string()
            project.set_title(new_title)
            project.set_description(new_description)
            project.set_color_string(new_color_string)
            self.project_handler.project_edited(
                old_title,
                new_title,
                new_description
            )
            if new_title != old_title:
                ComboBoxFunctions.add_string_to_combo_box(
                    self.ui.comboBoxProjects,
                    new_title
                )
                ComboBoxFunctions.delete_string_from_combo_box(
                    self.ui.comboBoxProjects,
                    old_title
                )
            self.update_project_view()
            self.mark_unsaved_changes()

    def on_add_task_pushed(self):
        self.add_edit_window.setWindowTitle("Add Task")
        result = self.add_edit_window.exec_add()
        if result == QDialog.Accepted:
            current_project = self.project_handler.get_current_project()
            task_creator = \
                self.add_edit_window.get_task_creator_from_user_input()
            current_project.add_task(task_creator)
            self.update_task_view()
            self.mark_unsaved_changes()

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
            self.update_task_view()
            self.show_task_screen()

    def show_welcome_screen(self):
        self.stacked_widget_state = StackedWidgetState.WELCOME.value
        self.ui.TaskWindowstackedWidget.setCurrentIndex(
            self.stacked_widget_state
        )
        self.ui.comboBoxProjects.hide()
        self.ui.pushButtonIconClose.hide()
        self.ui.pushButtonFullClose.hide()
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
        self.ui.pushButtonFullClose.show()
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
        self.ui.comboBoxProjects.hide()
        self.ui.pushButtonIconClose.hide()
        self.ui.pushButtonFullClose.hide()
        self.ui.pushButtonIconTask.hide()
        self.ui.pushButtonFullTask.hide()

    def setup_for_clean_start(self):
        self.file_name = None

        self.ui.labelVersion.setText(f"{self.version}")

        self.ui.FullSidebarQWidget.hide()
        self.ui.pushButtonFullTask.hide()
        self.ui.pushButtonIconTask.hide()

        self.ui.TaskWindowstackedWidget.setCurrentIndex(0)
        self.ui.ProjectPagestackedWidget.setCurrentIndex(0)

        self.ui.comboBoxProjects.hide()
        self.ui.pushButtonIconClose.hide()
        self.ui.pushButtonFullClose.hide()

        self.ui.scrollAreaWidgetContentsOpen.layout().setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContentsInProgress.layout().setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContentsStuckTest.layout().setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContentsDone.layout().setAlignment(Qt.AlignTop)

        self.ui.scrollAreaWidgetContentsProjectsList.layout().setAlignment(Qt.AlignTop)

        self.stacked_widget_state = StackedWidgetState.WELCOME.value
        self.project_sort_member = "title"

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

        self.ui.pushButtonSort.clicked.connect(
            self.on_sort_projects_pushed
        )

    def on_new_pushed(self):
        self.project_handler = ProjectHandler()
        self.ui.comboBoxProjects.clear()
        self.setup_for_clean_start()
        self.is_unsaved_changes = False
        self.update_title()

    def on_open_pushed(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        open_file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "",
            "Swift Note Files (" "*.todo);;All Files (*)",
            options=options
        )

        if not open_file_name:
            return

        self.file_name = open_file_name
        self.is_unsaved_changes = False
        self.update_title()

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
            self.is_unsaved_changes = False
            self.update_title()

    def on_save_as_pushed(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        save_as_file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "",
            "Swift Note Files (" "*.todo);;All Files (*)",
            options=options
        )

        if not save_as_file_name:
            return

        self.file_name = save_as_file_name

        with open(self.file_name, "wb") as file:
            pickle.dump(self.project_handler, file)

        self.is_unsaved_changes = False
        self.update_title()

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
        self.info_window.setWindowTitle("Info Task")
        self.info_window.execute(task)

    def task_move_in_scroll_area(self, move_tasks_hash, new_task_bin):
        current_project = self.project_handler.get_current_project()
        current_project.move_task_by_hash_in_bin(move_tasks_hash, new_task_bin)
        self.update_task_view()
        self.mark_unsaved_changes()

    def task_edit_in_scroll_area(self, edit_tasks_hash, edit_fields):
        current_project = self.project_handler.get_current_project()
        task = current_project.get_task_by_hash(edit_tasks_hash)
        new_title, new_description, new_color_string = edit_fields
        task.set_title(new_title)
        task.set_description(new_description)
        task.set_color_string(new_color_string)
        self.update_task_view()
        self.mark_unsaved_changes()

    def task_deleted_in_scroll_area(self, deleted_tasks_hash):
        current_project = self.project_handler.get_current_project()
        current_project.remove_task_by_hash(deleted_tasks_hash)
        self.mark_unsaved_changes()

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
        style_sheet = get_stylesheet_dark()
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
            u"minimize-2-light.svg",
            u"minimize-2-light.svg",
            u"plus-square-light.svg",
            u"plus-square-light.svg",
            u"menu-light.svg",
            u"toggle-right-light.svg",
            u"sliders-light.svg",
        ]

        self.change_layout_mode(icon_paths)
        self.layout = "dark"

    def use_light_mode(self):
        style_sheet = get_stylesheet_light()
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
            u"minimize-2.svg",
            u"minimize-2.svg",
            u"plus-square.svg",
            u"plus-square.svg",
            u"menu.svg",
            u"toggle-left.svg",
            u"sliders.svg",
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
            self.ui.pushButtonIconClose,
            self.ui.pushButtonFullClose,
            self.ui.pushButtonIconTask,
            self.ui.pushButtonFullTask,
            self.ui.pushButtonToggleMenu,
            self.ui.pushButtonFullLayout,
            self.ui.pushButtonSort,
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

    def get_project_signal_functions(self):
        return [
            self.selected_project_in_project_view,
            self.deleted_pushed_in_project_view,
            self.info_pushed_in_project_view,
            self.edit_pushed_in_project_view
        ]

    def selected_project_in_project_view(self, selected_project_hash):
        project = self.project_handler.get_project_by_hash(
            selected_project_hash)
        ComboBoxFunctions.set_index_to_string(
            self.ui.comboBoxProjects,
            project.get_title()
        )

    def deleted_pushed_in_project_view(self, deleted_project_hash):
        project = self.project_handler.get_project_by_hash(
            deleted_project_hash)
        title = project.get_title()
        ComboBoxFunctions.delete_string_from_combo_box(
            self.ui.comboBoxProjects,
            title
        )
        self.project_handler.remove_project_by_hash(deleted_project_hash)
        self.mark_unsaved_changes()

    def info_pushed_in_project_view(self, info_project_hash):
        project = self.project_handler.get_project_by_hash(info_project_hash)
        self.on_info_project_pushed(project)

    def edit_pushed_in_project_view(self, edit_project_hash):
        project = self.project_handler.get_project_by_hash(edit_project_hash)
        self.on_edit_project_pushed(project)

    def update_project_view(self):
        ScrollAreaFunctions.clear_scroll_area(
            self.ui.scrollAreaWidgetContentsProjectsList
        )

        sort_text = "sorted by: "
        if self.project_sort_member == "title":
            sort_text = sort_text + "Title"
        elif self.project_sort_member == "last_changed_string":
            sort_text = sort_text + "Last changed"
        elif self.project_sort_member == "created_string":
            sort_text = sort_text + "Created"
        elif self.project_sort_member == "open_task_count":
            sort_text = sort_text + "Open tasks"
        else:
            sort_text = sort_text + self.project_sort_member

        self.ui.labelSort.setText(sort_text)

        projects = self.project_handler.get_list_of_projects(
            sort_member=self.project_sort_member
        )

        ScrollAreaFunctions.fill_project_scroll_area(
            self.ui.scrollAreaWidgetContentsProjectsList,
            projects,
            self.get_project_signal_functions()
        )

    def on_sort_projects_pushed(self):
        current_sort_member = self.project_sort_member
        if current_sort_member == "title":
            self.project_sort_member = "last_changed_string"
        elif current_sort_member == "last_changed_string":
            self.project_sort_member = "created_string"
        elif current_sort_member == "created_string":
            self.project_sort_member = "open_task_count"
        elif current_sort_member == "open_task_count":
            self.project_sort_member = "title"
        else:
            assert False
        self.update_project_view()
