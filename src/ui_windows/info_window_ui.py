# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        if not InfoDialog.objectName():
            InfoDialog.setObjectName(u"InfoDialog")
        InfoDialog.resize(325, 375)
        icon = QIcon()
        icon.addFile(u":/icons/icons/swift-notes.svg", QSize(), QIcon.Normal, QIcon.Off)
        InfoDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(InfoDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(InfoDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout_8.addWidget(self.label)

        self.label_Name = QLabel(InfoDialog)
        self.label_Name.setObjectName(u"label_Name")

        self.horizontalLayout_8.addWidget(self.label_Name, 0, Qt.AlignRight)

        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.label_3 = QLabel(InfoDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.verticalLayout.addWidget(self.label_3)

        self.plainTextEditDescription = QPlainTextEdit(InfoDialog)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")
        self.plainTextEditDescription.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.plainTextEditDescription)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(InfoDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_DateCreated = QLabel(InfoDialog)
        self.label_DateCreated.setObjectName(u"label_DateCreated")

        self.horizontalLayout.addWidget(self.label_DateCreated, 0, Qt.AlignRight)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(InfoDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_DateChanged = QLabel(InfoDialog)
        self.label_DateChanged.setObjectName(u"label_DateChanged")

        self.horizontalLayout_2.addWidget(self.label_DateChanged, 0, Qt.AlignRight)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(InfoDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_NoTasks = QLabel(InfoDialog)
        self.label_NoTasks.setObjectName(u"label_NoTasks")

        self.horizontalLayout_3.addWidget(self.label_NoTasks, 0, Qt.AlignRight)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(InfoDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_NoOpen = QLabel(InfoDialog)
        self.label_NoOpen.setObjectName(u"label_NoOpen")

        self.horizontalLayout_4.addWidget(self.label_NoOpen, 0, Qt.AlignRight)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(InfoDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_NoInProgress = QLabel(InfoDialog)
        self.label_NoInProgress.setObjectName(u"label_NoInProgress")

        self.horizontalLayout_5.addWidget(self.label_NoInProgress, 0, Qt.AlignRight)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(InfoDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_NoStuckTest = QLabel(InfoDialog)
        self.label_NoStuckTest.setObjectName(u"label_NoStuckTest")

        self.horizontalLayout_6.addWidget(self.label_NoStuckTest, 0, Qt.AlignRight)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(InfoDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(150, 150, 150);")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_NoDone = QLabel(InfoDialog)
        self.label_NoDone.setObjectName(u"label_NoDone")

        self.horizontalLayout_7.addWidget(self.label_NoDone, 0, Qt.AlignRight)

        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.buttonBoxAddCancelProject = QDialogButtonBox(InfoDialog)
        self.buttonBoxAddCancelProject.setObjectName(u"buttonBoxAddCancelProject")
        self.buttonBoxAddCancelProject.setOrientation(Qt.Horizontal)
        self.buttonBoxAddCancelProject.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBoxAddCancelProject)


        self.retranslateUi(InfoDialog)
        self.buttonBoxAddCancelProject.accepted.connect(InfoDialog.accept)
        self.buttonBoxAddCancelProject.rejected.connect(InfoDialog.reject)

        QMetaObject.connectSlotsByName(InfoDialog)
    # setupUi

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(QCoreApplication.translate("InfoDialog", u"Project Info", None))
        self.label.setText(QCoreApplication.translate("InfoDialog", u"Title:", None))
        self.label_Name.setText(QCoreApplication.translate("InfoDialog", u"...Projectname...", None))
        self.label_3.setText(QCoreApplication.translate("InfoDialog", u"Description:", None))
        self.plainTextEditDescription.setPlainText("")
        self.plainTextEditDescription.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("InfoDialog", u"Created:", None))
        self.label_DateCreated.setText(QCoreApplication.translate("InfoDialog", u"...Date...", None))
        self.label_5.setText(QCoreApplication.translate("InfoDialog", u"Last changed:", None))
        self.label_DateChanged.setText(QCoreApplication.translate("InfoDialog", u"...Date...", None))
        self.label_6.setText(QCoreApplication.translate("InfoDialog", u"No. of tasks created:", None))
        self.label_NoTasks.setText(QCoreApplication.translate("InfoDialog", u"...Number...", None))
        self.label_7.setText(QCoreApplication.translate("InfoDialog", u"No. of tasks in 'Open':", None))
        self.label_NoOpen.setText(QCoreApplication.translate("InfoDialog", u"...Number...Percentage...", None))
        self.label_8.setText(QCoreApplication.translate("InfoDialog", u"No. of tasks in 'In Progress':", None))
        self.label_NoInProgress.setText(QCoreApplication.translate("InfoDialog", u"...Number...Percentage...", None))
        self.label_9.setText(QCoreApplication.translate("InfoDialog", u"No. of tasks in 'Stuck/Test':", None))
        self.label_NoStuckTest.setText(QCoreApplication.translate("InfoDialog", u"...Number...Percentage...", None))
        self.label_10.setText(QCoreApplication.translate("InfoDialog", u"No. of tasks 'Done':", None))
        self.label_NoDone.setText(QCoreApplication.translate("InfoDialog", u"...Number...Percentage...", None))
    # retranslateUi

