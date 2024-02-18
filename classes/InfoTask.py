from PySide6.QtWidgets import QDialog

from ui_windows.info_task_ui import Ui_InfoTaskDialog


class InfoTask(QDialog):
    def __init__(self):
        super(InfoTask, self).__init__()

        self.ui = Ui_InfoTaskDialog()
        self.ui.setupUi(self)

    def execute(self, task):
        self.ui.label_Name.setText(
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

        self.exec()
