from PySide6.QtWidgets import QScrollArea, QDialog, QWidget
from PySide6.QtCore import Signal

from task.TaskWidget import TaskWidget
from project.ProjectWidget import ProjectWidget


class CustomScrollArea(QScrollArea):

    drop_signal = Signal(str)

    def __init__(self, name, parent=None):
        super(CustomScrollArea, self).__init__(parent)
        self.name = name
        self.setAcceptDrops(True)

    def get_name(self):
        return self.name
        
    def dragEnterEvent(self, event):
        event.accept()
    
    def dropEvent(self, event):
        self.drop_signal.emit(self.name)
        event.accept()


class CustomScrollAreaWidget(QWidget):

    def __init__(self, parent=None):
        super(CustomScrollAreaWidget, self).__init__(parent)

    def clear_scroll_area(self):
        widget_to_remove = self.findChildren(QDialog)
        for widget in widget_to_remove:
            widget.setParent(None)
            widget.deleteLater()


    def fill_scroll_area(self, tasks, signal_functions):
        for task_creator in tasks:
            scroll_area_widget = TaskWidget(task_creator)
            self.layout().addWidget(
                scroll_area_widget
            )

        tasks_to_put_signal_on = self.findChildren(TaskWidget)
        edit_func, del_func, drag_func = \
            signal_functions
        for task in tasks_to_put_signal_on:
            task.edit_signal.connect(edit_func)
            task.delete_signal.connect(del_func)
            task.drag_signal.connect(drag_func)


    def fill_project_scroll_area(self, projects_list, signal_functions):
        for project in projects_list:
            scroll_area_widget = ProjectWidget(
                project.get_title(),
                project.get_task_count() - project.get_task_count_in("done"),
                project.get_last_changed_string(),
                project.get_created_string(),
                project.get_hash(),
                project.get_color_id()
            )
            self.layout().addWidget(
                scroll_area_widget
            )

        project_to_put_signal_on = self.findChildren(QDialog)
        sel_func, del_func, edit_func = signal_functions
        for project in project_to_put_signal_on:
            project.select_signal.connect(sel_func)
            project.delete_signal.connect(del_func)
            project.edit_signal.connect(edit_func)

