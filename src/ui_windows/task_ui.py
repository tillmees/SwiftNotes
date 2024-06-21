# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_TaskWidget(object):
    def setupUi(self, TaskWidget):
        if not TaskWidget.objectName():
            TaskWidget.setObjectName(u"TaskWidget")
        TaskWidget.resize(316, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskWidget.sizePolicy().hasHeightForWidth())
        TaskWidget.setSizePolicy(sizePolicy)
        TaskWidget.setMinimumSize(QSize(0, 40))
        TaskWidget.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout = QHBoxLayout(TaskWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(TaskWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Task = QWidget()
        self.Task.setObjectName(u"Task")
        self.verticalLayout = QVBoxLayout(self.Task)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTask = QLabel(self.Task)
        self.labelTask.setObjectName(u"labelTask")
        font = QFont()
        self.labelTask.setFont(font)
        self.labelTask.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelTask, 0, Qt.AlignTop)

        self.labelTaskCreated = QLabel(self.Task)
        self.labelTaskCreated.setObjectName(u"labelTaskCreated")
        font1 = QFont()
        font1.setPointSize(11)
        self.labelTaskCreated.setFont(font1)
        self.labelTaskCreated.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.labelTaskCreated, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.Task)
        self.DeletePrompt = QWidget()
        self.DeletePrompt.setObjectName(u"DeletePrompt")
        self.verticalLayout_2 = QVBoxLayout(self.DeletePrompt)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.DeletePrompt)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_Yes = QPushButton(self.DeletePrompt)
        self.pushButton_Yes.setObjectName(u"pushButton_Yes")

        self.verticalLayout_2.addWidget(self.pushButton_Yes, 0, Qt.AlignLeft)

        self.pushButton_No = QPushButton(self.DeletePrompt)
        self.pushButton_No.setObjectName(u"pushButton_No")

        self.verticalLayout_2.addWidget(self.pushButton_No, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.DeletePrompt)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.verticalLayoutButtons = QVBoxLayout()
        self.verticalLayoutButtons.setSpacing(0)
        self.verticalLayoutButtons.setObjectName(u"verticalLayoutButtons")
        self.verticalLayoutButtons.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButtonInfoTask = QPushButton(TaskWidget)
        self.pushButtonInfoTask.setObjectName(u"pushButtonInfoTask")
        icon = QIcon()
        icon.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonInfoTask.setIcon(icon)
        self.pushButtonInfoTask.setIconSize(QSize(14, 14))

        self.verticalLayoutButtons.addWidget(self.pushButtonInfoTask, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pushButtonMoveRightTask = QPushButton(TaskWidget)
        self.pushButtonMoveRightTask.setObjectName(u"pushButtonMoveRightTask")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMoveRightTask.setIcon(icon1)
        self.pushButtonMoveRightTask.setIconSize(QSize(14, 14))

        self.verticalLayoutButtons.addWidget(self.pushButtonMoveRightTask, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pushButtonMoveLeftTask = QPushButton(TaskWidget)
        self.pushButtonMoveLeftTask.setObjectName(u"pushButtonMoveLeftTask")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMoveLeftTask.setIcon(icon2)
        self.pushButtonMoveLeftTask.setIconSize(QSize(14, 14))

        self.verticalLayoutButtons.addWidget(self.pushButtonMoveLeftTask, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pushButtonEditTask = QPushButton(TaskWidget)
        self.pushButtonEditTask.setObjectName(u"pushButtonEditTask")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/edit-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonEditTask.setIcon(icon3)
        self.pushButtonEditTask.setIconSize(QSize(14, 14))

        self.verticalLayoutButtons.addWidget(self.pushButtonEditTask, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.pushButtonDeleteTask = QPushButton(TaskWidget)
        self.pushButtonDeleteTask.setObjectName(u"pushButtonDeleteTask")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonDeleteTask.setIcon(icon4)
        self.pushButtonDeleteTask.setIconSize(QSize(14, 14))

        self.verticalLayoutButtons.addWidget(self.pushButtonDeleteTask, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.verticalLayoutButtons)


        self.retranslateUi(TaskWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TaskWidget)
    # setupUi

    def retranslateUi(self, TaskWidget):
        TaskWidget.setWindowTitle(QCoreApplication.translate("TaskWidget", u"Form", None))
        self.labelTask.setText(QCoreApplication.translate("TaskWidget", u"Task Title", None))
        self.labelTaskCreated.setText(QCoreApplication.translate("TaskWidget", u"Created Date", None))
        self.label.setText(QCoreApplication.translate("TaskWidget", u"Delete this task?", None))
        self.pushButton_Yes.setText(QCoreApplication.translate("TaskWidget", u"Yes", None))
        self.pushButton_No.setText(QCoreApplication.translate("TaskWidget", u"No", None))
        self.pushButtonInfoTask.setText("")
        self.pushButtonMoveRightTask.setText("")
        self.pushButtonMoveLeftTask.setText("")
        self.pushButtonEditTask.setText("")
        self.pushButtonDeleteTask.setText("")
    # retranslateUi

