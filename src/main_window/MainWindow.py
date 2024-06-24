import pickle
from enum import Enum

from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from main_window.main_ui import Ui_MainWindow
from style.stylesheets import get_stylesheet_dark, get_stylesheet_light
from style.StyleHandler import StyleSettingsHandler

from form_window.AddEditWindow import AddEditWindow
from project.ProjectHandler import ProjectHandler
from base.CustomTitleBar import CustomTitleBar


EMPTY_PROJECT = " "


class StackedWidgetState(Enum):
    WELCOME = 0
    TASK_VIEW = 1
    PROJECT_VIEW = 2


class MainWindow(QMainWindow):
    def __init__(self, app, version, settings, style_settings):
        super(MainWindow, self).__init__()

        self.counter = 1
        self.app = app
        self.version = version

        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.scrollAreaOpen.drop_signal.connect(self.task_gets_dropped)
        self.ui.scrollAreaInProgress.drop_signal.connect(self.task_gets_dropped)
        self.ui.scrollAreaStuckTest.drop_signal.connect(self.task_gets_dropped)
        self.ui.scrollAreaDone.drop_signal.connect(self.task_gets_dropped)

        self.add_edit_window = AddEditWindow()
        self.project_handler = ProjectHandler()
        self.file_name = None
        self.is_unsaved_changes = None

        self.stacked_widget_state = None
        self.project_sort_member = None

        self.setup_for_clean_start()
        self.setup_signals()
        self.is_start_up_finished = True

        self.settings = settings
        self.apply_settings()

        self.style_settings = style_settings
        self.style_handler = StyleSettingsHandler(self.style_settings, settings.get_value_for("layout"), self.ui)
        self.style_handler.set_layout(self.app)

        self.update_title()
    
    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.task_dropped_outside_of_a_scroll_area()
        event.accept()

    def apply_settings(self):
        width = int(self.settings.get_value_for("width"))
        height = int(self.settings.get_value_for("height"))
        self.resize(width, height)

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

    def closeEvent(self, event):
        if not self.window().isMaximized():
            self.settings.set_value_to("width", self.width())
            self.settings.set_value_to("height", self.height())
        self.settings.set_value_to("layout", self.style_handler.get_layout())
        super().closeEvent(event)

    def on_add_project_pushed(self):
        self.add_edit_window.clear_edits()
        self.add_edit_window.setWindowTitle("Add Project")
        result = self.add_edit_window.exec_add()
        if result == QDialog.Accepted:
            project = self.add_edit_window.get_project_from_user_input()
            self.project_handler.add_project(project)
            self.project_handler.set_current_project(project.get_title())
            self.ui.comboBoxProjects.update_combo_box(
                project.get_title()
            )
            self.update_task_view()
            self.mark_unsaved_changes()

    def on_close_project_pushed(self):
        self.project_handler.set_current_project(None)
        self.update_project_view()
        self.show_project_screen()

    def on_edit_project_pushed(self, project):
        old_title = project.get_title()
        old_description = project.get_description()
        old_color_string = project.get_color_string()

        self.add_edit_window.clear_edits()
        self.add_edit_window.setWindowTitle("Edit Project")
        self.add_edit_window.set_title(old_title)
        self.add_edit_window.set_description(old_description)
        self.add_edit_window.set_color_checked_box(old_color_string)

        result = self.add_edit_window.exec_edit(project)
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
                self.ui.comboBoxProjects.add_string_to_combo_box(
                    new_title
                )
                self.ui.comboBoxProjects.delete_string_from_combo_box(
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
        project_title_in_combo_box = self.ui.comboBoxProjects.get_current_project()
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
        self.ui.comboBoxProjects.delete_whitespace_string_from_combo_box()
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
        self.ui.comboBoxProjects.add_whitespace_string_to_combo_box()
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
            self.task_edit_in_scroll_area,
            self.task_deleted_in_scroll_area,
            self.task_gets_dragged
        ]

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

    def task_gets_dragged(self, dragged_tasks_hash):
        self.dragged_tasks_hash = dragged_tasks_hash
        current_project = self.project_handler.get_current_project()
        self.dragged_task_creator = current_project.get_task_by_hash(dragged_tasks_hash)

    def task_gets_dropped(self, bin_name):
        if self.dragged_tasks_hash is not None:
            if self.dragged_task_creator.task_bin != bin_name:
                current_project = self.project_handler.get_current_project()
                current_project.remove_task_by_hash(self.dragged_tasks_hash)

                self.dragged_task_creator.task_bin = bin_name
                current_project.add_task(self.dragged_task_creator)

                self.dragged_tasks_hash = None
                self.dragged_task_creator = None

                self.mark_unsaved_changes()
        self.update_task_view()

    def task_dropped_outside_of_a_scroll_area(self):
        if self.dragged_tasks_hash is not None:
            self.dragged_tasks_hash = None
            self.dragged_task = None

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

        self.ui.scrollAreaWidgetContentsOpen.clear_scroll_area()
        self.ui.scrollAreaWidgetContentsInProgress.clear_scroll_area()
        self.ui.scrollAreaWidgetContentsStuckTest.clear_scroll_area()
        self.ui.scrollAreaWidgetContentsDone.clear_scroll_area()
        

        self.ui.scrollAreaWidgetContentsOpen.fill_scroll_area(
            current_project.get_tasks_in("open"),
            self.get_task_signal_functions()
        )
        self.ui.scrollAreaWidgetContentsInProgress.fill_scroll_area(
            current_project.get_tasks_in("in progress"),
            self.get_task_signal_functions()
        )
        self.ui.scrollAreaWidgetContentsStuckTest.fill_scroll_area(
            current_project.get_tasks_in("stuck/test"),
            self.get_task_signal_functions()
        )
        self.ui.scrollAreaWidgetContentsDone.fill_scroll_area(
            current_project.get_tasks_in("done"),
            self.get_task_signal_functions()
        )
        self.update_task_counter()

    def on_toggle_layout(self):
        self.style_handler.toggle_layout(self.app)

    def get_project_signal_functions(self):
        return [
            self.selected_project_in_project_view,
            self.deleted_pushed_in_project_view,
            self.edit_pushed_in_project_view
        ]

    def selected_project_in_project_view(self, selected_project_hash):
        project = self.project_handler.get_project_by_hash(
            selected_project_hash)
        self.ui.comboBoxProjects.set_index_to_string(
            project.get_title()
        )

    def deleted_pushed_in_project_view(self, deleted_project_hash):
        project = self.project_handler.get_project_by_hash(
            deleted_project_hash)
        title = project.get_title()
        self.ui.comboBoxProjects.delete_string_from_combo_box(
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
        self.ui.scrollAreaWidgetContentsProjectsList.clear_scroll_area()

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

        self.ui.scrollAreaWidgetContentsProjectsList.fill_project_scroll_area(
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