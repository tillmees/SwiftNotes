from windows.edit_window.EditWindow import EditWindow


class EditTaskWindow(EditWindow):
    def __init__(self):
        super(EditTaskWindow, self).__init__()
        self.hide_project_info_elements()
        self.setWindowTitle("Edit Task")
