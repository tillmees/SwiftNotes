from PySide6.QtWidgets import QDialog

from classes.TaskWidget import TaskWidget
from classes.ProjectWidget import ProjectWidget


def clear_scroll_area(scroll_area):
    widget_to_remove = scroll_area.findChildren(QDialog)
    for widget in widget_to_remove:
        widget.setParent(None)
        widget.deleteLater()


def fill_scroll_area(scroll_area, tasks, signal_functions):
    for task_creator in tasks:
        scroll_area_widget = TaskWidget(task_creator)
        scroll_area.layout().addWidget(
            scroll_area_widget
        )

    tasks_to_put_signal_on = scroll_area.findChildren(TaskWidget)
    info_func, move_func, edit_func, del_func = \
        signal_functions
    for task in tasks_to_put_signal_on:
        task.info_signal.connect(info_func)
        task.move_signal.connect(move_func)
        task.edit_signal.connect(edit_func)
        task.delete_signal.connect(del_func)


def fill_project_scroll_area(scroll_area, projects, signal_functions):
    for project in projects.values():
        scroll_area_widget = ProjectWidget(
            project.get_title(),
            project.get_task_count() - project.get_task_count_in("done"),
            project.get_last_changed_string(),
            project.get_created_string(),
            project.get_hash(),
            project.get_color_string()
        )
        scroll_area.layout().addWidget(
            scroll_area_widget
        )

    project_to_put_signal_on = scroll_area.findChildren(QDialog)
    sel_func, del_func, info_func, edit_func = signal_functions
    for project in project_to_put_signal_on:
        project.select_signal.connect(sel_func)
        project.delete_signal.connect(del_func)
        project.info_signal.connect(info_func)
        project.edit_signal.connect(edit_func)