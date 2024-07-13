from PySide6.QtCore import Qt
from windows.edit_window.EditWindow import EditWindow
from project_manager.ProjectManager import ProjectManager


class EditTaskWindow(EditWindow):
    def __init__(self, color_id=0):
        super(EditTaskWindow, self).__init__(color_id)
        self.hide_project_info_elements()
        self.setWindowTitle("Edit Task")
        
        self.setup_comboBoxProjects()

    def setup_comboBoxProjects(self):
        project_manager = ProjectManager()
        if len(project_manager.projects):
            project_titles = project_manager.get_list_of_all_titles()
            self.ui.comboBoxProjects.addItems(project_titles)
            project = project_manager.get_project_by_hash(project_manager.current_project_hash_value)
            index = self.ui.comboBoxProjects.findText(project.get_title())
            self.ui.comboBoxProjects.setCurrentIndex(index)

            # make the items in the drop-down menu align right
            for i in range(self.ui.comboBoxProjects.count()):
                self.ui.comboBoxProjects.setItemData(i, Qt.AlignRight, Qt.TextAlignmentRole)


            self.ui.comboBoxProjects.setEditable(True)
            line_edit = self.ui.comboBoxProjects.lineEdit()
            line_edit.setAlignment(Qt.AlignRight)
            line_edit.setReadOnly(True)

