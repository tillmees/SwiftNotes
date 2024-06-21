from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent

from ui_windows.ProjectUi import Ui_ProjectWidget

from classes.BaseWidget import BaseWidget


class ProjectWidget(BaseWidget):
    select_signal = Signal(str)
    delete_signal = Signal(str)
    edit_signal = Signal(str)

    def __init__(
            self,
            title,
            open_tasks_count,
            last_changed_string,
            created_string,
            hash_value,
            color_string
    ):
        super(ProjectWidget, self).__init__(color_string)

        self.ui = Ui_ProjectWidget()
        self.ui.setupUi(self)

        self.title = title
        self.open_tasks_count = open_tasks_count
        self.created_string = created_string
        self.last_changed_string = last_changed_string
        self.hash_value = hash_value
        self.color_string = color_string
        
        self.setup_widget()
        self.setup_stylesheets()
        self.setup_connections()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.on_project_selected_clicked()
        super().mouseDoubleClickEvent(event)

    def setup_widget(self):
        self.ui.labelProjectTitle.setText(f" {self.title}")
        self.ui.labelProjectOpenTasks.setText(f"{self.open_tasks_count}")
        self.ui.labelProjectCreated.setText(self.created_string)
        self.ui.labelProjectChanged.setText(self.last_changed_string)
        self.ui.stackedWidget.setCurrentIndex(0)

    def setup_connections(self):
        self.ui.pushButtonEditProject.clicked.connect(
            self.on_edit_clicked)
        self.ui.pushButtonDeleteProject.clicked.connect(
            self.on_delete_clicked)
        self.ui.pushButton_NoDelProject.clicked.connect(
            self.on_delete_canceled)
        self.ui.pushButton_YesDelProject.clicked.connect(
            self.on_delete_accepted)

    def on_project_selected_clicked(self):
        self.select_signal.emit(self.get_hash())

    def on_delete_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_delete_accepted(self):
        self.delete_signal.emit(self.get_hash())
        self.deleteLater()

    def on_delete_canceled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_edit_clicked(self):
        self.edit_signal.emit(self.get_hash())

    def get_hash(self):
        return self.hash_value

    def setup_stylesheets(self):
        self.setStyleSheet(
            f"background-color: {self.color_string};\n "
        )

        self.ui.labelProjectTitle.setStyleSheet(
            "color: #000000;\n "
        )

        self.ui.labelDelProject.setStyleSheet(
            "color: #000000;\n "
        )
        self.ui.labelProjectOpenTasks.setStyleSheet(
            "color: #000000;\n "
        )
        self.ui.labelProjectCreated.setStyleSheet(
            "color: #000000;\n "
        )
        self.ui.labelProjectChanged.setStyleSheet(
            "color: #000000;\n "
        )

        self.ui.pushButtonEditProject.setStyleSheet(
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButtonDeleteProject.setStyleSheet(
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButton_YesDelProject.setStyleSheet(
            "QPushButton{background-color: rgba(0, 0, 0, 0.15); width: 60px; border-radius: 4px;}"
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButton_NoDelProject.setStyleSheet(
            "QPushButton{background-color: rgba(0, 0, 0, 0.15); width: 60px; border-radius: 4px;}"
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )
