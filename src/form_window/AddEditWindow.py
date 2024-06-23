from PySide6.QtWidgets import QDialogButtonBox, QDialog

from task.TaskCreator import TaskCreator
from style.Colors import Colors
from project.ProjectClass import ProjectClass
from form_window.AddEditUi import Ui_AddEditDialog


class AddEditWindow(QDialog):
    def __init__(self):
        super(AddEditWindow, self).__init__()

        self.ui = Ui_AddEditDialog()
        self.ui.setupUi(self)

        self.ui.buttonBoxAddCancelTask.button(
            QDialogButtonBox.Ok).setEnabled(False)

        self.ui.lineEditTaskname.textChanged.connect(self.on_task_name_changed)

        self.max_chars = 100

        self.colors = Colors()
        self.checkBoxes = []
        self.setup_checkbox_ids()
        self.setup_stylesheets()

    def exec_add(self):
        self.hide_common_info_elements()
        self.hide_project_info_elements()
        self.clear_edits()
        self.ui.lineEditTaskname.setFocus()
        return super(AddEditWindow, self).exec()

    def exec_edit(self, obj):
        if isinstance(obj, ProjectClass):
            self.setup_for_project(obj)
        else:
            self.setup_for_task(obj)
        return super(AddEditWindow, self).exec()
    
    def setup_for_project(self, project):
        self.ui.lineEditTaskname.setText(project.get_title())
        self.ui.plainTextEditDescription.setPlainText(
            project.get_description()
        )
        self.ui.label_DateCreated.setText(
            project.get_created_string()
        )
        self.ui.label_DateChanged.setText(
            project.get_last_changed_string()
        )
        self.ui.label_NoTasks.setText(
            f"{project.get_task_count()}"
        )
        self.ui.label_NoOpen.setText(
            f"{project.get_task_count_in('open')}"
        )
        self.ui.label_NoInProgress.setText(
            f"{project.get_task_count_in('in progress')}"
        )
        self.ui.label_NoStuckTest.setText(
            f"{project.get_task_count_in('stuck/test')}"
        )
        self.ui.label_NoDone.setText(
            f"{project.get_task_count_in('done')}"
        )

        self.show_common_info_elements()
        self.show_project_info_elements()

    def setup_for_task(self, task):
        self.ui.lineEditTaskname.setText(
            task.title
        )
        self.ui.plainTextEditDescription.setPlainText(
            task.description
        )
        self.ui.label_DateCreated.setText(
            task.created_string
        )
        self.ui.label_DateChanged.setText(
            task.last_changed_string
        )

        self.show_common_info_elements()
        self.hide_project_info_elements()

    def hide_common_info_elements(self):
        self.ui.label_DateCreatedText.hide()
        self.ui.label_DateCreated.hide()

        self.ui.label_DateChangedText.hide()
        self.ui.label_DateChanged.hide()

    def show_common_info_elements(self):
        self.ui.label_DateCreatedText.show()
        self.ui.label_DateCreated.show()

        self.ui.label_DateChangedText.show()
        self.ui.label_DateChanged.show()

    def hide_project_info_elements(self):
        self.ui.label_NoTasksText.hide()
        self.ui.label_NoOpenText.hide()
        self.ui.label_NoInProgressText.hide()
        self.ui.label_NoStuckTestText.hide()
        self.ui.label_NoDoneText.hide()

        self.ui.label_NoTasks.hide()
        self.ui.label_NoOpen.hide()
        self.ui.label_NoInProgress.hide()
        self.ui.label_NoStuckTest.hide()
        self.ui.label_NoDone.hide()

    def show_project_info_elements(self):
        self.ui.label_NoTasksText.show()
        self.ui.label_NoOpenText.show()
        self.ui.label_NoInProgressText.show()
        self.ui.label_NoStuckTestText.show()
        self.ui.label_NoDoneText.show()

        self.ui.label_NoTasks.show()
        self.ui.label_NoOpen.show()
        self.ui.label_NoInProgress.show()
        self.ui.label_NoStuckTest.show()
        self.ui.label_NoDone.show()

    def clear_edits(self):
        self.ui.lineEditTaskname.clear()
        self.ui.plainTextEditDescription.clear()

    def get_task_creator_from_user_input(self):
        task_creator = TaskCreator(
            self.get_title(),
            self.get_description(),
            self.get_color_string()
        )
        return task_creator

    def get_project_from_user_input(self):
        project = ProjectClass(
            self.get_title(),
            self.get_description(),
            color_string=self.get_color_string()
        )
        return project

    def on_task_name_changed(self):
        self.enable_ok_button()
        self.check_text_length()

    def enable_ok_button(self):
        if self.ui.lineEditTaskname.text() == "":
            self.ui.buttonBoxAddCancelTask.button(
                QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.ui.buttonBoxAddCancelTask.button(
                QDialogButtonBox.Ok).setEnabled(True)

    def check_text_length(self):
        current_text = self.ui.lineEditTaskname.text()

        # Truncate the text if it exceeds the maximum character count
        if len(current_text) > self.max_chars:
            self.ui.lineEditTaskname.setText(current_text[:self.max_chars])

    def get_title(self):
        return self.ui.lineEditTaskname.text()

    def set_title(self, string):
        return self.ui.lineEditTaskname.setText(string)

    def get_description(self):
        return self.ui.plainTextEditDescription.toPlainText()

    def set_description(self, string):
        return self.ui.plainTextEditDescription.setPlainText(string)

    def get_color_string(self):
        checked_id = self.ui.buttonGroup.checkedId()
        return self.colors.color_mapping[checked_id]

    def set_color_checked_box(self, color_string):
        id = self.colors.get_color_id_by_string(color_string)
        self.checkBoxes[id - 1].setChecked(True)


    def setup_stylesheets(self):
        self.ui.color_1.setStyleSheet(
            f"background-color: {self.colors.Color1};\n "
            "border-radius: 10px;")
        self.ui.color_2.setStyleSheet(
            f"background-color: {self.colors.Color2};\n "
            "border-radius: 10px;")
        self.ui.color_3.setStyleSheet(
            f"background-color: {self.colors.Color3};\n "
            "border-radius: 10px;")
        self.ui.color_4.setStyleSheet(
            f"background-color: {self.colors.Color4};\n "
            "border-radius: 10px;")
        self.ui.color_5.setStyleSheet(
            f"background-color: {self.colors.Color5};\n "
            "border-radius: 10px;")
        self.ui.color_6.setStyleSheet(
            f"background-color: {self.colors.Color6};\n "
            "border-radius: 10px;")
        self.ui.color_7.setStyleSheet(
            f"background-color: {self.colors.Color7};\n "
            "border-radius: 10px;")
        self.ui.color_8.setStyleSheet(
            f"background-color: {self.colors.Color8};\n "
            "border-radius: 10px;")
        self.ui.color_9.setStyleSheet(
            f"background-color: {self.colors.Color9};\n "
            "border-radius: 10px;")
        self.ui.color_10.setStyleSheet(
            f"background-color: {self.colors.Color10};\n "
            "border-radius: 10px;")

    def setup_checkbox_ids(self):
        self.checkBoxes = [
            self.ui.checkBox_1,
            self.ui.checkBox_2,
            self.ui.checkBox_3,
            self.ui.checkBox_4,
            self.ui.checkBox_5,
            self.ui.checkBox_6,
            self.ui.checkBox_7,
            self.ui.checkBox_8,
            self.ui.checkBox_9,
            self.ui.checkBox_10,
        ]

        for id, checkBox in enumerate(self.checkBoxes):
            self.ui.buttonGroup.setId(
                checkBox,
                id + 1
            )