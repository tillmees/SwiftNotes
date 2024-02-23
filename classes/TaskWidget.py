from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Signal

from ui_windows.task_ui import Ui_TaskWidget
from classes.EditWindow import AddEditWindow
from classes.TaskCreator import TaskCreator
from functions.UtilityFunctions import get_current_time_string


class TaskWidget(QDialog):
    delete_signal = Signal(str)
    info_signal = Signal(str)
    edit_signal = Signal(str, tuple)
    move_signal = Signal(str, str)

    def __init__(self, task_creator):
        super(TaskWidget, self).__init__()

        self.ui = Ui_TaskWidget()
        self.ui.setupUi(self)
        self.edit_task_window = AddEditWindow()

        self.title = task_creator.title
        self.description = task_creator.description
        self.color_string = task_creator.color

        self.created_string = task_creator.created_string
        self.last_changed_string = task_creator.last_changed_string
        self.hash_value = task_creator.hash_value

        self.task_bin = task_creator.task_bin

        self.setup_widget()
        self.setup_stylesheets()
        self.setup_connections()

    @classmethod
    def get_deepcopy(cls, class_instance):
        return cls(
            class_instance.get_task_creator
        )

    def get_task_creator(self):
        return TaskCreator(
            title=self.title,
            description=self.description,
            color=self.color_string,
            created_string=self.created_string,
            last_changed_string=self.last_changed_string,
            hash_value=self.hash_value,
            task_bin=self.task_bin
        )

    def setup_widget(self):
        self.ui.labelTask.setText(self.title)
        self.ui.labelTaskCreated.setText(self.created_string)
        self.ui.verticalLayoutButtons.setAlignment(Qt.AlignTop)
        self.ui.stackedWidget.setCurrentIndex(0)

    def setup_connections(self):
        self.ui.pushButtonInfoTask.clicked.connect(self.on_info_clicked)
        self.ui.pushButtonMoveRightTask.clicked.connect(
            self.on_move_right_clicked)
        self.ui.pushButtonMoveLeftTask.clicked.connect(
            self.on_move_left_clicked)
        self.ui.pushButtonEditTask.clicked.connect(self.on_edit_clicked)
        self.ui.pushButtonDeleteTask.clicked.connect(self.on_delete_clicked)
        self.ui.pushButton_Yes.clicked.connect(self.on_delete_accepted)
        self.ui.pushButton_No.clicked.connect(self.on_delete_canceled)

    def setup_stylesheets(self):
        self.setStyleSheet(
            f"background-color: {self.color_string};\n "
        )

        self.ui.pushButtonInfoTask.setStyleSheet(
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButtonMoveRightTask.setStyleSheet(
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButtonMoveLeftTask.setStyleSheet(
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButtonEditTask.setStyleSheet(
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButtonDeleteTask.setStyleSheet(
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButton_Yes.setStyleSheet(
            "QPushButton{background-color: rgba(0, 0, 0, 0.15); width: 60px;}"
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButton_No.setStyleSheet(
            "QPushButton{background-color: rgba(0, 0, 0, 0.15); width: 60px;}"
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

    def on_info_clicked(self):
        self.info_signal.emit(self.get_hash())

    def on_move_right_clicked(self):
        if self.task_bin == "open":
            self.task_bin = "in progress"

        elif self.task_bin == "in progress":
            self.task_bin = "stuck/test"

        elif self.task_bin == "stuck/test":
            self.task_bin = "done"

        self.move_signal.emit(self.get_hash(), self.task_bin)

    def on_move_left_clicked(self):
        if self.task_bin == "done":
            self.task_bin = "stuck/test"

        elif self.task_bin == "stuck/test":
            self.task_bin = "in progress"

        elif self.task_bin == "in progress":
            self.task_bin = "open"

        self.move_signal.emit(self.get_hash(), self.task_bin)

    def on_edit_clicked(self):
        old_title = self.title
        old_description = self.description
        old_color_string = self.color_string

        self.edit_task_window.clear_edits()
        self.edit_task_window.setWindowTitle("Edit Task")
        self.edit_task_window.set_title(old_title)
        self.edit_task_window.set_description(old_description)
        self.edit_task_window.set_color_checked_box(old_color_string)

        result = self.edit_task_window.exec_edit()
        if result == QDialog.Accepted:
            new_title = self.edit_task_window.get_title()
            new_description = self.edit_task_window.get_description()
            new_color_string = self.edit_task_window.get_color_string()

            self.edit_signal.emit(
                self.get_hash(),
                (new_title, new_description, new_color_string)
            )

    def on_delete_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.side_buttons_are_enabled(False)

    def on_delete_accepted(self):
        self.delete_signal.emit(self.get_hash())
        self.deleteLater()

    def on_delete_canceled(self):
        self.side_buttons_are_enabled(True)
        self.ui.stackedWidget.setCurrentIndex(0)

    def side_buttons_are_enabled(self, bool_val):
        self.ui.pushButtonInfoTask.setEnabled(bool_val)
        self.ui.pushButtonMoveRightTask.setEnabled(bool_val)
        self.ui.pushButtonMoveLeftTask.setEnabled(bool_val)
        self.ui.pushButtonEditTask.setEnabled(bool_val)
        self.ui.pushButtonDeleteTask.setEnabled(bool_val)

    def get_hash(self):
        return self.hash_value

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title
        self.update_last_changed_string()

    def get_created_string(self):
        return self.created_string

    def get_last_changed_string(self):
        return self.last_changed_string

    def update_last_changed_string(self):
        self.last_changed_string = get_current_time_string()

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description
        self.update_last_changed_string()

    def get_task_bin(self):
        return self.task_bin

    def set_task_bin(self, new_task_bin):
        self.task_bin = new_task_bin
        self.update_last_changed_string()

    def set_color_string(self, color_string):
        self.color_string = color_string
        self.update_last_changed_string()

    def get_color_string(self):
        return self.color_string


