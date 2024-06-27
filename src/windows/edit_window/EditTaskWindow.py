from windows.edit_window.EditWindow import EditWindow


class EditTaskWindow(EditWindow):
    def __init__(self, color_id=0):
        super(EditTaskWindow, self).__init__(color_id)
        self.hide_project_info_elements()
        self.setWindowTitle("Edit Task")
