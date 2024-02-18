from classes.TaskWidget import TaskWidget


def clear_scroll_area(scroll_area):
    tasks_to_remove = scroll_area.findChildren(
        TaskWidget)
    for task in tasks_to_remove:
        task.setParent(None)
        task.deleteLater()


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
