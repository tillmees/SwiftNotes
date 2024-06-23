from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QHBoxLayout, QLabel, QPushButton, QSizePolicy, QStackedWidget, QWidget
)


class Ui_ProjectWidget(object):
    def setupUi(self, ProjectWidget):
        self.set_object_name(ProjectWidget)
        self.set_size_policy(ProjectWidget)

        # horizontal layout for the project widget
        self.projectWidgetMainLayout = QHBoxLayout(ProjectWidget)
        self.projectWidgetMainLayout.setObjectName(u"horizontalLayout")

        self.stackedWidget = self.configure_stacked_widget(ProjectWidget)

        self.labelProjectTitle = None
        self.labelProjectOpenTasks = None
        self.labelProjectChanged = None
        self.labelProjectCreated = None
        self.projectDescriptionWidget = self.configure_project_description_widget(ProjectWidget)
        self.stackedWidget.addWidget(self.projectDescriptionWidget)

        self.labelDelProject = None
        self.pushButton_YesDelProject = None
        self.pushButton_NoDelProject = None
        self.projectDeleteWidget = self.configure_project_delete_widget(ProjectWidget)
        self.stackedWidget.addWidget(self.projectDeleteWidget)

        self.stackedWidget.setCurrentIndex(0)
        self.projectWidgetMainLayout.addWidget(self.stackedWidget, 0, Qt.AlignVCenter)

        self.pushButtonEditProject = self.configure_edit_button(ProjectWidget)
        self.projectWidgetMainLayout.addWidget(self.pushButtonEditProject, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.pushButtonDeleteProject = self.configure_delete_button(ProjectWidget)
        self.projectWidgetMainLayout.addWidget(self.pushButtonDeleteProject, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.projectWidgetMainLayout.setStretch(0, 1)

        self.set_text_of_buttons_and_labels(ProjectWidget)

        QMetaObject.connectSlotsByName(ProjectWidget)

    def set_object_name(self, ProjectWidget):
        if not ProjectWidget.objectName():
            ProjectWidget.setObjectName(u"ProjectWidget")

    def set_size_policy(self, ProjectWidget):
        ProjectWidget.resize(687, 60)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectWidget.sizePolicy().hasHeightForWidth())
        ProjectWidget.setSizePolicy(sizePolicy)
        ProjectWidget.setMinimumSize(QSize(0, 40))
        ProjectWidget.setMaximumSize(QSize(16777215, 60))

    def configure_stacked_widget(self, ProjectWidget):
        stackedWidget = QStackedWidget(ProjectWidget)
        stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(stackedWidget.sizePolicy().hasHeightForWidth())
        stackedWidget.setSizePolicy(sizePolicy)
        return stackedWidget
    
    def configure_project_description_widget(self, ProjectWidget):
        projectDescriptionWidget = QWidget(ProjectWidget)
        projectDescriptionWidget.setObjectName(u"projectDescriptionWidget")
        horizontalLayout = QHBoxLayout(projectDescriptionWidget)
        horizontalLayout.setSpacing(10)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(10, 0, 10, 0)

        self.labelProjectTitle = QLabel(projectDescriptionWidget)
        self.labelProjectTitle.setObjectName(u"labelProjectTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelProjectTitle.sizePolicy().hasHeightForWidth())
        self.labelProjectTitle.setSizePolicy(sizePolicy2)
        font = QFont()
        self.labelProjectTitle.setFont(font)
        horizontalLayout.addWidget(self.labelProjectTitle, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.labelProjectOpenTasks = QLabel(projectDescriptionWidget)
        self.labelProjectOpenTasks.setObjectName(u"labelProjectOpenTasks")
        font1 = QFont()
        font1.setPointSize(9)
        self.labelProjectOpenTasks.setFont(font1)
        self.labelProjectOpenTasks.setStyleSheet(u"")

        horizontalLayout.addWidget(self.labelProjectOpenTasks, 0, Qt.AlignLeft)

        self.labelProjectChanged = QLabel(projectDescriptionWidget)
        self.labelProjectChanged.setObjectName(u"labelProjectChanged")
        self.labelProjectChanged.setFont(font1)
        self.labelProjectChanged.setStyleSheet(u"")

        horizontalLayout.addWidget(self.labelProjectChanged, 0, Qt.AlignLeft)

        self.labelProjectCreated = QLabel(projectDescriptionWidget)
        self.labelProjectCreated.setObjectName(u"labelProjectCreated")
        self.labelProjectCreated.setFont(font1)
        self.labelProjectCreated.setStyleSheet(u"")

        horizontalLayout.addWidget(self.labelProjectCreated, 0, Qt.AlignLeft)

        return projectDescriptionWidget
    
    def configure_project_delete_widget(self, ProjectWidget):
        projectDeleteWidget = QWidget(ProjectWidget)
        projectDeleteWidget.setObjectName(u"projectDeleteWidget")
        horizontalLayout = QHBoxLayout(projectDeleteWidget)
        horizontalLayout.setSpacing(10)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(10, 0, 10, 0)

        self.labelDelProject = QLabel(projectDeleteWidget)
        self.labelDelProject.setObjectName(u"labelDelProject")
        horizontalLayout.addWidget(self.labelDelProject, 0, Qt.AlignLeft)

        self.pushButton_YesDelProject = QPushButton(projectDeleteWidget)
        self.pushButton_YesDelProject.setObjectName(u"pushButton_YesDelProject")
        horizontalLayout.addWidget(self.pushButton_YesDelProject, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton_NoDelProject = QPushButton(projectDeleteWidget)
        self.pushButton_NoDelProject.setObjectName(u"pushButton_NoDelProject")
        horizontalLayout.addWidget(self.pushButton_NoDelProject, 0, Qt.AlignLeft|Qt.AlignVCenter)

        horizontalLayout.setStretch(2, 1)

        return projectDeleteWidget

    def configure_edit_button(self, ProjectWidget):
        pushButtonEditProject = QPushButton(ProjectWidget)
        pushButtonEditProject.setObjectName(u"pushButtonEditProject")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        pushButtonEditProject.setIcon(icon2)
        pushButtonEditProject.setIconSize(QSize(14, 14))
        return pushButtonEditProject

    def configure_delete_button(self, ProjectWidget):
        pushButtonDeleteProject = QPushButton(ProjectWidget)
        pushButtonDeleteProject.setObjectName(u"pushButtonDeleteProject")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        pushButtonDeleteProject.setIcon(icon2)
        pushButtonDeleteProject.setIconSize(QSize(14, 14))
        return pushButtonDeleteProject

    def set_text_of_buttons_and_labels(self, ProjectWidget):
        ProjectWidget.setWindowTitle(QCoreApplication.translate("ProjectWidget", u"Form", None))
        self.labelProjectTitle.setText(QCoreApplication.translate("ProjectWidget", u"Title", None))
        self.labelProjectOpenTasks.setText(QCoreApplication.translate("ProjectWidget", u"Open Tasks", None))
        self.labelProjectChanged.setText(QCoreApplication.translate("ProjectWidget", u"Changed Date", None))
        self.labelProjectCreated.setText(QCoreApplication.translate("ProjectWidget", u"Created Date", None))
        self.labelDelProject.setText(QCoreApplication.translate("ProjectWidget", u"Delete this project?", None))
        self.pushButton_YesDelProject.setText(QCoreApplication.translate("ProjectWidget", u"Yes", None))
        self.pushButton_NoDelProject.setText(QCoreApplication.translate("ProjectWidget", u"No", None))
        self.pushButtonEditProject.setText("")
        self.pushButtonDeleteProject.setText("")