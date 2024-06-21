from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget, QSpacerItem
)


class Ui_TaskWidget(object):
    def setupUi(self, TaskWidget):
        self.set_object_name(TaskWidget)
        self.set_size_policy(TaskWidget)

        # horizontal layout for the project widget
        self.taskWidgetMainLayout = QHBoxLayout(TaskWidget)
        self.taskWidgetMainLayout.setObjectName(u"horizontalLayout")
        self.taskWidgetMainLayout.setContentsMargins(10, 10, 10, 10)

        self.stackedWidget = self.configure_stacked_widget(TaskWidget)

        self.labelTaskTitle = None
        self.labelTaskCreated = None
        self.taskOverviewWidget = self.configure_task_overview_widget(TaskWidget)
        self.stackedWidget.addWidget(self.taskOverviewWidget)

        self.labelDelTask = None
        self.pushButton_YesDelTask = None
        self.pushButton_NoDelTask = None
        self.taskDeleteWidget = self.configure_task_delete_widget(TaskWidget)
        self.stackedWidget.addWidget(self.taskDeleteWidget)

        self.stackedWidget.setCurrentIndex(0)
        self.taskWidgetMainLayout.addWidget(self.stackedWidget)

        self.verticalLayoutButtons = QVBoxLayout()
        self.verticalLayoutButtons.setSpacing(0)
        self.verticalLayoutButtons.setObjectName(u"verticalLayoutButtons")
        self.verticalLayoutButtons.setSizeConstraint(QLayout.SetMinimumSize)

        verticalSpacer = QSpacerItem(20, 40000, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.verticalLayoutButtons.addItem(verticalSpacer)

        self.pushButtonInfoTask = self.configure_info_button(TaskWidget)
        self.verticalLayoutButtons.addWidget(self.pushButtonInfoTask, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pushButtonDeleteTask = self.configure_delete_button(TaskWidget)
        self.verticalLayoutButtons.addWidget(self.pushButtonDeleteTask, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.taskWidgetMainLayout.addLayout(self.verticalLayoutButtons)

        self.set_text_of_buttons_and_labels(TaskWidget)

        QMetaObject.connectSlotsByName(TaskWidget)

    def set_object_name(self, TaskWidget):
        if not TaskWidget.objectName():
            TaskWidget.setObjectName(u"TaskWidget")

    def set_size_policy(self, TaskWidget):
        TaskWidget.resize(316, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskWidget.sizePolicy().hasHeightForWidth())
        TaskWidget.setSizePolicy(sizePolicy)
        TaskWidget.setMinimumSize(QSize(0, 40))
        TaskWidget.setMaximumSize(QSize(16777215, 150))

    def configure_stacked_widget(self, TaskWidget):
        stackedWidget = QStackedWidget(TaskWidget)
        stackedWidget.setObjectName(u"stackedWidget")
        return stackedWidget
    
    def configure_task_overview_widget(self, TaskWidget):
        taskOverviewWidget = QWidget(TaskWidget)
        taskOverviewWidget.setObjectName(u"taskOverviewWidget")
        verticalLayout = QVBoxLayout(taskOverviewWidget)
        verticalLayout.setObjectName(u"verticalLayout")
        self.labelTaskTitle = QLabel(taskOverviewWidget)
        self.labelTaskTitle.setObjectName(u"labelTask")
        font = QFont()
        self.labelTaskTitle.setFont(font)
        self.labelTaskTitle.setWordWrap(True)

        verticalLayout.addWidget(self.labelTaskTitle, 0, Qt.AlignTop)

        self.labelTaskCreated = QLabel(taskOverviewWidget)
        self.labelTaskCreated.setObjectName(u"labelTaskCreated")
        font = QFont()
        self.labelTaskCreated.setFont(font)

        verticalLayout.addWidget(self.labelTaskCreated, 0, Qt.AlignBottom)

        return taskOverviewWidget
    
    def configure_task_delete_widget(self, TaskWidget):
        taskDeleteWidget = QWidget(TaskWidget)
        taskDeleteWidget.setObjectName(u"taskDeleteWidget")
        verticalLayout = QVBoxLayout(taskDeleteWidget)
        verticalLayout.setSpacing(10)
        verticalLayout.setObjectName(u"verticalLayout")
        verticalLayout.setContentsMargins(10, 0, 10, 0)

        self.labelDelTask = QLabel(taskDeleteWidget)
        self.labelDelTask.setObjectName(u"labelDelTask")
        verticalLayout.addWidget(self.labelDelTask, 0, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_YesDelTask = QPushButton(taskDeleteWidget)
        self.pushButton_YesDelTask.setObjectName(u"pushButton_YesDelTask")
        verticalLayout.addWidget(self.pushButton_YesDelTask, 0, Qt.AlignLeft)

        self.pushButton_NoDelTask = QPushButton(taskDeleteWidget)
        self.pushButton_NoDelTask.setObjectName(u"pushButton_NoDelTask")
        verticalLayout.addWidget(self.pushButton_NoDelTask, 0, Qt.AlignLeft)

        return taskDeleteWidget

    def configure_info_button(self, TaskWidget):
        pushButtonInfoTask = QPushButton(TaskWidget)
        pushButtonInfoTask.setObjectName(u"pushButtonInfoTask")
        icon = QIcon()
        icon.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        pushButtonInfoTask.setIcon(icon)
        pushButtonInfoTask.setIconSize(QSize(14, 14))
        return pushButtonInfoTask

    def configure_delete_button(self, TaskWidget):
        pushButtonDeleteTask = QPushButton(TaskWidget)
        pushButtonDeleteTask.setObjectName(u"pushButtonDeleteTask")
        icon = QIcon()
        icon.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        pushButtonDeleteTask.setIcon(icon)
        pushButtonDeleteTask.setIconSize(QSize(14, 14))
        return pushButtonDeleteTask

    def set_text_of_buttons_and_labels(self, TaskWidget):
        TaskWidget.setWindowTitle(QCoreApplication.translate("TaskWidget", u"Form", None))
        self.labelTaskTitle.setText(QCoreApplication.translate("TaskWidget", u"Title", None))
        self.labelTaskCreated.setText(QCoreApplication.translate("TaskWidget", u"Created Date", None))
        self.labelDelTask.setText(QCoreApplication.translate("TaskWidget", u"Delete this task?", None))
        self.pushButton_YesDelTask.setText(QCoreApplication.translate("TaskWidget", u"Yes", None))
        self.pushButton_NoDelTask.setText(QCoreApplication.translate("TaskWidget", u"No", None))
        self.pushButtonInfoTask.setText("")
        self.pushButtonDeleteTask.setText("")