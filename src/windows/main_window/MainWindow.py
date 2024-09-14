import xml.etree.ElementTree as ET
from enum import Enum

from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QAction

from settings.WindowSettingsHandler import WindowSettingsHandler
from settings.RecentFilesSettingsHandler import RecentFilesSettingsHandler
from windows.main_window.MainUi import Ui_MainWindow
from windows.edit_window.EditProjectWindow import EditProjectWindow
from windows.add_window.AddProjectWindow import AddProjectWindow
from windows.add_window.AddTaskWindow import AddTaskWindow
from windows.about_window.AboutWindow import AboutWindow
from project_manager.ProjectManager import ProjectManager
from style.LayoutHandler import LayoutHandler


class StackedWidgetState(Enum):
    WELCOME = 0
    TASK_VIEW = 1
    PROJECT_VIEW = 2


class MainWindow(QMainWindow):
    def __init__(self, app, version, filename=None):
        super(MainWindow, self).__init__()

        self.app = app
        self.version = version

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_name = filename
        self.is_unsaved_changes = None
        self.stacked_widget_state = None
        self.project_sort_member = None
        self.project_manager = ProjectManager()

        self.style_handler = LayoutHandler(self.ui)
        self.window_handler = WindowSettingsHandler()
        self.recent_files_handler = RecentFilesSettingsHandler()

        self.add_project_window = AddProjectWindow()
        self.add_task_window = AddTaskWindow()
        self.about_window = AboutWindow(version=version)

        self.startup()
        if filename is not None:
            self.open_existing_file(filename)

    def startup(self):
        self.setup_for_clean_start()
        self.create_actions()
        self.setup_signals()
        self.apply_window_settings()
        self.style_handler.set_layout(self.app)
        self.update_title()

    def create_actions(self):
        self.open_action = QAction("&Open", self)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.triggered.connect(self.on_open_pushed)
        self.addAction(self.open_action)

        self.new_action = QAction("&New", self)
        self.new_action.setShortcut(QKeySequence("Ctrl+N"))
        self.new_action.triggered.connect(self.on_new_pushed)
        self.addAction(self.new_action)

        self.save_action = QAction("&Save", self)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.triggered.connect(self.on_save_pushed)
        self.addAction(self.save_action)

        self.save_as_action = QAction("&New", self)
        self.save_as_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.save_as_action.triggered.connect(self.on_save_as_pushed)
        self.addAction(self.save_as_action)

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

    def apply_window_settings(self):
        width = int(self.window_handler.get_value_for("width"))
        height = int(self.window_handler.get_value_for("height"))
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
        if self.is_unsaved_changes:
            result = QMessageBox.question(
                self,
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save them?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                QMessageBox.Yes
            )
            if result == QMessageBox.Yes:
                self.on_save_pushed()
                if self.is_unsaved_changes:
                    # this second check is needed for the case when
                    # the user cancels the save dialog otherwise the
                    # application would close immediately without saving
                    event.ignore()
            elif result == QMessageBox.No:
                pass
            else:
                event.ignore()

        if not self.window().isMaximized():
            self.window_handler.set_value_to("width", self.width())
            self.window_handler.set_value_to("height", self.height())
        self.window_handler.set_value_to("layout", self.style_handler.get_layout())

    def on_add_project_pushed(self):
        already_existing_project_titles = self.project_manager.get_list_of_all_titles()
        result = self.add_project_window.exec(already_existing_project_titles)
        if result == QDialog.Accepted:
            project = self.add_project_window.get_project_from_user_input()
            success = self.project_manager.add_project(project)
            if success:
                self.ui.comboBoxProjects.update_combo_box(project.get_title())
                self.update_task_view()
                self.mark_unsaved_changes()

    def on_close_project_pushed(self):
        self.project_manager.set_current_project(None)
        self.update_project_view()
        self.show_project_screen()

    def on_edit_project_pushed(self, project):
        already_existing_project_titles = self.project_manager.get_list_of_all_titles()
        already_existing_project_titles.remove(project.get_title())
        edit_project_window = EditProjectWindow(project.get_color_id())
        edit_project_window.setup_window(project)
        result = edit_project_window.exec(already_existing_project_titles)
        if result == QDialog.Accepted:
            old_title = project.get_title()
            hash_value = project.get_hash()
            new_title, new_description, new_color_id = edit_project_window.get_attributes_from_user_input()
            self.project_manager.project_edited(
                hash_value,
                new_title,
                new_description,
                new_color_id
            )
            if new_title != old_title:
                self.ui.comboBoxProjects.add_string_to_combo_box(new_title)
                self.ui.comboBoxProjects.delete_string_from_combo_box(old_title)
            self.update_project_view()
            self.mark_unsaved_changes()

    def on_add_task_pushed(self):
        self.add_task_window.setWindowTitle("Add Task")
        result = self.add_task_window.exec()
        if result == QDialog.Accepted:
            current_project = self.project_manager.get_current_project()
            task = self.add_task_window.get_task_from_user_input()
            current_project.add_task(task)
            self.update_task_view()
            self.mark_unsaved_changes()

    def on_project_changed_in_combo_box(self):
        project_title_in_combo_box = self.ui.comboBoxProjects.get_current_project()
        if project_title_in_combo_box == "":
            return
        selected_project_title = project_title_in_combo_box if \
            project_title_in_combo_box != " " else None
        selected_project_hash = self.project_manager.get_project_hash_by_title(selected_project_title)
        self.project_manager.set_current_project(selected_project_hash)
        self.on_selected_project_changed()

    def on_selected_project_changed(self):
        empty_project = " "
        current_project = self.project_manager.get_current_project()
        if current_project is None:
            self.show_welcome_screen()
        elif current_project is not empty_project:
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

        self.update_recent_file_links()
        self.stacked_widget_state = StackedWidgetState.WELCOME.value
        self.project_sort_member = "title"

    def update_recent_file_links(self):
        for i in range(3):
            eval(f"self.ui.clickableLabelRecentFile{i+1}").setText(self.recent_files_handler.get_recent_file_name_by_index(i))
            path = self.recent_files_handler.get_recent_file_path_by_index(i)
            path_truncated = f"{path[:15]} ... {path[-15:]}" if len(path) > 33 else path
            eval(f"self.ui.labelRecentPath{i+1}").setText(path_truncated)
            eval(f"self.ui.labelRecentPath{i+1}").setToolTip(path)

    def setup_signals(self):
        self.ui.pushButtonIconNew.clicked.connect(self.new_action.trigger)
        self.ui.pushButtonFullNew.clicked.connect(self.new_action.trigger)

        self.ui.pushButtonIconOpen.clicked.connect(self.open_action.trigger)
        self.ui.pushButtonFullOpen.clicked.connect(self.open_action.trigger)

        self.ui.pushButtonIconSave.clicked.connect(self.save_action.trigger)
        self.ui.pushButtonFullSave.clicked.connect(self.save_action.trigger)

        self.ui.pushButtonIconSaveAs.clicked.connect(self.save_as_action.trigger)
        self.ui.pushButtonFullSaveAs.clicked.connect(self.save_as_action.trigger)

        ###
        self.ui.pushButtonIconAdd.clicked.connect(self.on_add_project_pushed)
        self.ui.pushButtonFullAdd.clicked.connect(self.on_add_project_pushed)

        self.ui.pushButtonIconClose.clicked.connect(self.on_close_project_pushed)
        self.ui.pushButtonFullClose.clicked.connect(self.on_close_project_pushed)

        self.ui.pushButtonIconTask.clicked.connect(self.on_add_task_pushed)
        self.ui.pushButtonFullTask.clicked.connect(self.on_add_task_pushed)

        self.ui.comboBoxProjects.currentIndexChanged.connect(self.on_project_changed_in_combo_box)

        self.ui.pushButtonAbout.clicked.connect(self.on_about_pushed)

        self.ui.pushButtonFullLayout.clicked.connect(self.on_toggle_layout)

        self.ui.pushButtonSort.clicked.connect(self.on_sort_projects_pushed)

        ###
        self.ui.scrollAreaOpen.drop_signal.connect(self.task_gets_dropped)
        self.ui.scrollAreaInProgress.drop_signal.connect(self.task_gets_dropped)
        self.ui.scrollAreaStuckTest.drop_signal.connect(self.task_gets_dropped)
        self.ui.scrollAreaDone.drop_signal.connect(self.task_gets_dropped)

        ###
        self.ui.clickableLabelRecentFile1.clicked.connect(self.on_recent_file_1_pushed)
        self.ui.clickableLabelRecentFile2.clicked.connect(self.on_recent_file_2_pushed)
        self.ui.clickableLabelRecentFile3.clicked.connect(self.on_recent_file_3_pushed) 

    def on_recent_file_1_pushed(self):
        self.open_existing_file(self.recent_files_handler.get_recent_file_path_by_index(0))

    def on_recent_file_2_pushed(self):
        self.open_existing_file(self.recent_files_handler.get_recent_file_path_by_index(1))

    def on_recent_file_3_pushed(self):
        self.open_existing_file(self.recent_files_handler.get_recent_file_path_by_index(2))

    def on_new_pushed(self):
        self.project_manager.reset_instance()
        self.project_manager = ProjectManager()
        self.ui.comboBoxProjects.clear()
        self.setup_for_clean_start()
        self.is_unsaved_changes = False
        self.update_title()

    def on_open_pushed(self):
        options = QFileDialog.Options()
        open_file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "",
            "Swift Note Files (" "*.todo);;All Files (*)",
            options=options
        )
        if not open_file_name:
            return
        self.open_existing_file(open_file_name)

    def open_existing_file(self, open_file_name):
        self.file_name = open_file_name
        self.is_unsaved_changes = False
        self.update_title()

        self.project_manager.reset_instance()
        tree = ET.parse(open_file_name)
        root = tree.getroot()
        self.project_manager = ProjectManager.from_xml(root)

        self.ui.comboBoxProjects.clear()
        if len(self.project_manager.projects):
            project_titles = self.project_manager.get_list_of_all_titles()
            self.on_close_project_pushed()
            self.ui.comboBoxProjects.addItems(project_titles)

        self.recent_files_handler.update_recent_files(open_file_name)

    def on_save_pushed(self):
        if self.file_name is None:
            self.on_save_as_pushed()

        else:
            root = self.project_manager.to_xml()
            tree = ET.ElementTree(root)
            tree.write(self.file_name)

            self.is_unsaved_changes = False
            self.update_title()

    def on_save_as_pushed(self):
        options = QFileDialog.Options()
        save_as_file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", "",
            "Swift Note Files (" "*.todo);;All Files (*)",
            options=options
        )

        if not save_as_file_name:
            return

        self.file_name = save_as_file_name

        self.recent_files_handler.update_recent_files(self.file_name)

        self.on_save_pushed()

    def get_task_signal_functions(self):
        return [
            self.task_edit_in_scroll_area,
            self.task_deleted_in_scroll_area,
            self.task_gets_dragged
        ]

    def task_edit_in_scroll_area(self, edit_tasks_hash, edit_fields):
        current_project = self.project_manager.get_current_project()
        new_title, new_description, new_color_id, new_project_title = edit_fields
        task = current_project.get_task_by_hash(edit_tasks_hash)

        task.set_title(new_title)
        task.set_description(new_description)
        task.set_color_id(new_color_id)
        if new_project_title != current_project.get_title():
            new_project = self.project_manager.get_project_by_title(new_project_title)
            new_project.add_task(task)
            current_project.remove_task_by_hash(edit_tasks_hash)

        self.update_task_view()
        self.mark_unsaved_changes()

    def task_deleted_in_scroll_area(self, deleted_tasks_hash):
        current_project = self.project_manager.get_current_project()
        current_project.remove_task_by_hash(deleted_tasks_hash)
        self.mark_unsaved_changes()

    def task_gets_dragged(self, dragged_tasks_hash):
        self.dragged_tasks_hash = dragged_tasks_hash
        current_project = self.project_manager.get_current_project()
        self.dragged_task_creator = current_project.get_task_by_hash(dragged_tasks_hash)

    def task_gets_dropped(self, bin_name):
        if self.dragged_tasks_hash is not None:
            if self.dragged_task_creator.task_bin != bin_name:
                current_project = self.project_manager.get_current_project()
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
        current_project = self.project_manager.get_current_project()
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
        current_project = self.project_manager.get_current_project()

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
        project = self.project_manager.get_project_by_hash(
            selected_project_hash)
        self.ui.comboBoxProjects.set_index_to_string(
            project.get_title()
        )

    def deleted_pushed_in_project_view(self, deleted_project_hash):
        project = self.project_manager.get_project_by_hash(
            deleted_project_hash)
        title = project.get_title()
        self.ui.comboBoxProjects.delete_string_from_combo_box(
            title
        )
        self.project_manager.remove_project_by_hash(deleted_project_hash)
        self.mark_unsaved_changes()

    def info_pushed_in_project_view(self, info_project_hash):
        project = self.project_manager.get_project_by_hash(info_project_hash)
        self.on_info_project_pushed(project)

    def edit_pushed_in_project_view(self, edit_project_hash):
        project = self.project_manager.get_project_by_hash(edit_project_hash)
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

        projects = self.project_manager.get_list_of_projects(
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

    def on_about_pushed(self):
        self.about_window.exec()
