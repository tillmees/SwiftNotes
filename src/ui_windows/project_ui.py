# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)
import resources_rc

class Ui_ProjectWidget(object):
    def setupUi(self, ProjectWidget):
        if not ProjectWidget.objectName():
            ProjectWidget.setObjectName(u"ProjectWidget")
        ProjectWidget.resize(687, 60)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectWidget.sizePolicy().hasHeightForWidth())
        ProjectWidget.setSizePolicy(sizePolicy)
        ProjectWidget.setMinimumSize(QSize(0, 40))
        ProjectWidget.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_3 = QHBoxLayout(ProjectWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(ProjectWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.Project = QWidget()
        self.Project.setObjectName(u"Project")
        self.horizontalLayout = QHBoxLayout(self.Project)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.labelProjectTitle = QLabel(self.Project)
        self.labelProjectTitle.setObjectName(u"labelProjectTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelProjectTitle.sizePolicy().hasHeightForWidth())
        self.labelProjectTitle.setSizePolicy(sizePolicy2)
        font = QFont()
        self.labelProjectTitle.setFont(font)

        self.horizontalLayout.addWidget(self.labelProjectTitle, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.labelProjectOpenTasks = QLabel(self.Project)
        self.labelProjectOpenTasks.setObjectName(u"labelProjectOpenTasks")
        font1 = QFont()
        font1.setPointSize(9)
        self.labelProjectOpenTasks.setFont(font1)
        self.labelProjectOpenTasks.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.labelProjectOpenTasks, 0, Qt.AlignLeft)

        self.labelProjectChanged = QLabel(self.Project)
        self.labelProjectChanged.setObjectName(u"labelProjectChanged")
        self.labelProjectChanged.setFont(font1)
        self.labelProjectChanged.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.labelProjectChanged, 0, Qt.AlignLeft)

        self.labelProjectCreated = QLabel(self.Project)
        self.labelProjectCreated.setObjectName(u"labelProjectCreated")
        self.labelProjectCreated.setFont(font1)
        self.labelProjectCreated.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.labelProjectCreated, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.Project)
        self.DeletePromptProject = QWidget()
        self.DeletePromptProject.setObjectName(u"DeletePromptProject")
        self.horizontalLayout_2 = QHBoxLayout(self.DeletePromptProject)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.labelDelProject = QLabel(self.DeletePromptProject)
        self.labelDelProject.setObjectName(u"labelDelProject")

        self.horizontalLayout_2.addWidget(self.labelDelProject, 0, Qt.AlignLeft)

        self.pushButton_YesDelProject = QPushButton(self.DeletePromptProject)
        self.pushButton_YesDelProject.setObjectName(u"pushButton_YesDelProject")

        self.horizontalLayout_2.addWidget(self.pushButton_YesDelProject, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton_NoDelProject = QPushButton(self.DeletePromptProject)
        self.pushButton_NoDelProject.setObjectName(u"pushButton_NoDelProject")

        self.horizontalLayout_2.addWidget(self.pushButton_NoDelProject, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.setStretch(2, 1)
        self.stackedWidget.addWidget(self.DeletePromptProject)

        self.horizontalLayout_3.addWidget(self.stackedWidget, 0, Qt.AlignVCenter)

        self.pushButtonInfoProject = QPushButton(ProjectWidget)
        self.pushButtonInfoProject.setObjectName(u"pushButtonInfoProject")
        icon = QIcon()
        icon.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonInfoProject.setIcon(icon)
        self.pushButtonInfoProject.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.pushButtonInfoProject, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.pushButtonEditProject = QPushButton(ProjectWidget)
        self.pushButtonEditProject.setObjectName(u"pushButtonEditProject")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonEditProject.setIcon(icon1)
        self.pushButtonEditProject.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.pushButtonEditProject, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.pushButtonDeleteProject = QPushButton(ProjectWidget)
        self.pushButtonDeleteProject.setObjectName(u"pushButtonDeleteProject")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonDeleteProject.setIcon(icon2)
        self.pushButtonDeleteProject.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.pushButtonDeleteProject)

        self.horizontalLayout_3.setStretch(0, 1)

        self.retranslateUi(ProjectWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ProjectWidget)
    # setupUi

    def retranslateUi(self, ProjectWidget):
        ProjectWidget.setWindowTitle(QCoreApplication.translate("ProjectWidget", u"Form", None))
        self.labelProjectTitle.setText(QCoreApplication.translate("ProjectWidget", u"Title", None))
        self.labelProjectOpenTasks.setText(QCoreApplication.translate("ProjectWidget", u"Open Tasks", None))
        self.labelProjectChanged.setText(QCoreApplication.translate("ProjectWidget", u"Changed Date", None))
        self.labelProjectCreated.setText(QCoreApplication.translate("ProjectWidget", u"Created Date", None))
        self.labelDelProject.setText(QCoreApplication.translate("ProjectWidget", u"Delete this project?", None))
        self.pushButton_YesDelProject.setText(QCoreApplication.translate("ProjectWidget", u"Yes", None))
        self.pushButton_NoDelProject.setText(QCoreApplication.translate("ProjectWidget", u"No", None))
        self.pushButtonInfoProject.setText("")
        self.pushButtonEditProject.setText("")
        self.pushButtonDeleteProject.setText("")
    # retranslateUi

