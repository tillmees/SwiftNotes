from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Signal, QMimeData
from PySide6.QtGui import QMouseEvent, QDrag, QPixmap, QPainter, QColor

from task.TaskUi import Ui_TaskWidget

from base.CustomBaseWidget import CustomBaseWidget
from base.UtilityFunctions import transparent_color
from windows.edit_window.EditTaskWindow import EditTaskWindow
from task.Task import Task


class TaskWidget(CustomBaseWidget):
    drag_signal = Signal(str)
    delete_signal = Signal(str)
    edit_signal = Signal(str, tuple)

    def __init__(self, task_creator):
        super(TaskWidget, self).__init__(
            task_creator.title,
            task_creator.created_string,
            task_creator.last_changed_string,
            task_creator.color_id,
            task_creator.hash_value
        )

        self.ui = Ui_TaskWidget()
        self.ui.setupUi(self)

        self.description = task_creator.description
        self.task_bin = task_creator.task_bin

        self.setup_widget()
        self.setup_stylesheets()
        self.setup_connections()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.on_edit_clicked()
        super().mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            
            self.drag_signal.emit(self.get_hash())

            drag = QDrag(self)
            drag.setMimeData(QMimeData())

            pixmap = self.grab()
            # the divison by pixmap.devicePixelRatio() is to compensate for different window scaling modes in the operating system
            rounded_pixmap = QPixmap(pixmap.size() / pixmap.devicePixelRatio())
            rounded_pixmap.fill(Qt.transparent)

            painter = QPainter(rounded_pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            rounded_rect = rounded_pixmap.rect()
            painter.setBrush(QColor(255, 255, 255))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(rounded_rect, 9, 9)  # Adjust the radius for rounded corners
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            drag.setPixmap(rounded_pixmap)

            self.is_transparent = True
            self.setStyleSheet(
                f"background-color: {transparent_color(self.color_handler.color_mapping[self.color_id])};\n "
            )

            hot_spot = event.pos()
            drag.setHotSpot(hot_spot)
            drag.setObjectName(self.hash_value)

            drag.exec_(Qt.MoveAction)

            self.setStyleSheet(
                f"background-color: {self.color_handler.color_mapping[self.color_id]};\n "
            )

    @classmethod
    def get_deepcopy(cls, class_instance):
        return cls(
            class_instance.get_task
        )

    def get_task(self):
        return Task(
            title=self.title,
            description=self.description,
            color_id=self.color_id,
            created_string=self.created_string,
            last_changed_string=self.last_changed_string,
            hash_value=self.hash_value,
            task_bin=self.task_bin
        )

    def setup_widget(self):
        self.ui.labelTaskTitle.setText(self.title)
        self.ui.plainTextEditDescription.setPlainText(self.description)
        self.ui.labelTaskCreated.setText(self.created_string)
        self.ui.verticalLayoutButtons.setAlignment(Qt.AlignTop)
        self.ui.stackedWidget.setCurrentIndex(0)

    def setup_connections(self):
        self.ui.pushButtonDeleteTask.clicked.connect(self.on_delete_clicked)
        self.ui.pushButton_YesDelTask.clicked.connect(self.on_delete_accepted)
        self.ui.pushButton_NoDelTask.clicked.connect(self.on_delete_canceled)

    def on_edit_clicked(self):
        edit_task_window = EditTaskWindow(self.color_id)
        edit_task_window.setup_window(self.get_task())

        result = edit_task_window.exec()
        if result == QDialog.Accepted:
            new_title, new_description, new_color_id, new_project = edit_task_window.get_attributes_from_user_input()
            self.edit_signal.emit(
                self.get_hash(),
                (new_title, new_description, new_color_id, new_project)
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
        self.ui.pushButtonDeleteTask.setEnabled(bool_val)

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

    def setup_stylesheets(self):
        self.setStyleSheet(
            f"background-color: {self.color_handler.color_mapping[self.color_id]};\n "
        )

        self.ui.stackedWidget.setStyleSheet(
            "background-color: transparent;\n"
        )

        self.ui.plainTextEditDescription.setStyleSheet(
            "background-color: transparent;\n"
            "border: none;\n"
        )

        self.ui.pushButtonDeleteTask.setStyleSheet(
            "QPushButton{background-color: transparent;}\n"
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButton_YesDelTask.setStyleSheet(
            "QPushButton{background-color: rgba(0, 0, 0, 0.15); width: 60px; "
            "border-radius: 4px;}\n "
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )

        self.ui.pushButton_NoDelTask.setStyleSheet(
            "QPushButton{background-color: rgba(0, 0, 0, 0.15); width: 60px; "
            "border-radius: 4px;}\n "
            "QPushButton::hover{background-color: rgba(0, 0, 0, 0.25); "
            "border-radius: 4px;}\n "
            "QPushButton::pressed{background-color: rgba(0, 0, 0, 0.5); "
            "border-radius: 4px;}\n "
        )
