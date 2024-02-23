# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QCheckBox,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QLineEdit, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_AddEditDialog(object):
    def setupUi(self, AddEditDialog):
        if not AddEditDialog.objectName():
            AddEditDialog.setObjectName(u"AddEditDialog")
        AddEditDialog.resize(330, 325)
        icon = QIcon()
        icon.addFile(u":/icons/icons/swift-notes.svg", QSize(), QIcon.Normal, QIcon.Off)
        AddEditDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(AddEditDialog)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lineEditTaskname = QLineEdit(AddEditDialog)
        self.lineEditTaskname.setObjectName(u"lineEditTaskname")

        self.verticalLayout.addWidget(self.lineEditTaskname)

        self.plainTextEditDescription = QPlainTextEdit(AddEditDialog)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")

        self.verticalLayout.addWidget(self.plainTextEditDescription)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(AddEditDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.color_1 = QFrame(self.widget)
        self.color_1.setObjectName(u"color_1")
        self.color_1.setMinimumSize(QSize(20, 20))
        self.color_1.setMaximumSize(QSize(20, 20))
        self.color_1.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(100, 200, 200);\n"
"	border-radius: 10px;\n"
"}")
        self.color_1.setFrameShape(QFrame.NoFrame)
        self.color_1.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_1, 0, 0, 1, 1)

        self.color_2 = QFrame(self.widget)
        self.color_2.setObjectName(u"color_2")
        self.color_2.setMinimumSize(QSize(20, 20))
        self.color_2.setMaximumSize(QSize(20, 20))
        self.color_2.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_2.setFrameShape(QFrame.NoFrame)
        self.color_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_2, 0, 1, 1, 1)

        self.color_3 = QFrame(self.widget)
        self.color_3.setObjectName(u"color_3")
        self.color_3.setMinimumSize(QSize(20, 20))
        self.color_3.setMaximumSize(QSize(20, 20))
        self.color_3.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_3.setFrameShape(QFrame.NoFrame)
        self.color_3.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_3, 0, 2, 1, 1)

        self.color_4 = QFrame(self.widget)
        self.color_4.setObjectName(u"color_4")
        self.color_4.setMinimumSize(QSize(20, 20))
        self.color_4.setMaximumSize(QSize(20, 20))
        self.color_4.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_4.setFrameShape(QFrame.NoFrame)
        self.color_4.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_4, 0, 3, 1, 1)

        self.color_5 = QFrame(self.widget)
        self.color_5.setObjectName(u"color_5")
        self.color_5.setMinimumSize(QSize(20, 20))
        self.color_5.setMaximumSize(QSize(20, 20))
        self.color_5.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_5.setFrameShape(QFrame.NoFrame)
        self.color_5.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_5, 0, 4, 1, 1)

        self.color_6 = QFrame(self.widget)
        self.color_6.setObjectName(u"color_6")
        self.color_6.setMinimumSize(QSize(20, 20))
        self.color_6.setMaximumSize(QSize(20, 20))
        self.color_6.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_6.setFrameShape(QFrame.NoFrame)
        self.color_6.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_6, 0, 5, 1, 1)

        self.color_7 = QFrame(self.widget)
        self.color_7.setObjectName(u"color_7")
        self.color_7.setMinimumSize(QSize(20, 20))
        self.color_7.setMaximumSize(QSize(20, 20))
        self.color_7.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_7.setFrameShape(QFrame.NoFrame)
        self.color_7.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_7, 0, 6, 1, 1)

        self.color_8 = QFrame(self.widget)
        self.color_8.setObjectName(u"color_8")
        self.color_8.setMinimumSize(QSize(20, 20))
        self.color_8.setMaximumSize(QSize(20, 20))
        self.color_8.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_8.setFrameShape(QFrame.NoFrame)
        self.color_8.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_8, 0, 7, 1, 1)

        self.color_9 = QFrame(self.widget)
        self.color_9.setObjectName(u"color_9")
        self.color_9.setMinimumSize(QSize(20, 20))
        self.color_9.setMaximumSize(QSize(20, 20))
        self.color_9.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_9.setFrameShape(QFrame.NoFrame)
        self.color_9.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_9, 0, 8, 1, 1)

        self.color_10 = QFrame(self.widget)
        self.color_10.setObjectName(u"color_10")
        self.color_10.setMinimumSize(QSize(20, 20))
        self.color_10.setMaximumSize(QSize(20, 20))
        self.color_10.setStyleSheet(u"background-color: rgb(100, 200, 200);\n"
"border-radius: 10px;\n"
"")
        self.color_10.setFrameShape(QFrame.NoFrame)
        self.color_10.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.color_10, 0, 9, 1, 1)

        self.checkBox_1 = QCheckBox(self.widget)
        self.buttonGroup = QButtonGroup(AddEditDialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.checkBox_1)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setAutoFillBackground(False)
        self.checkBox_1.setStyleSheet(u"")
        self.checkBox_1.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_1, 1, 0, 1, 1, Qt.AlignHCenter)

        self.checkBox_2 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1, Qt.AlignHCenter)

        self.checkBox_3 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_4 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 1, 3, 1, 1, Qt.AlignHCenter)

        self.checkBox_5 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 1, 4, 1, 1, Qt.AlignHCenter)

        self.checkBox_6 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_6)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 1, 5, 1, 1, Qt.AlignHCenter)

        self.checkBox_7 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_7)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 1, 6, 1, 1, Qt.AlignHCenter)

        self.checkBox_8 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_8)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout.addWidget(self.checkBox_8, 1, 7, 1, 1, Qt.AlignHCenter)

        self.checkBox_9 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_9)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 1, 8, 1, 1, Qt.AlignHCenter)

        self.checkBox_10 = QCheckBox(self.widget)
        self.buttonGroup.addButton(self.checkBox_10)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout.addWidget(self.checkBox_10, 1, 9, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBoxAddCancelTask = QDialogButtonBox(AddEditDialog)
        self.buttonBoxAddCancelTask.setObjectName(u"buttonBoxAddCancelTask")
        self.buttonBoxAddCancelTask.setOrientation(Qt.Horizontal)
        self.buttonBoxAddCancelTask.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBoxAddCancelTask)


        self.retranslateUi(AddEditDialog)
        self.buttonBoxAddCancelTask.accepted.connect(AddEditDialog.accept)
        self.buttonBoxAddCancelTask.rejected.connect(AddEditDialog.reject)

        QMetaObject.connectSlotsByName(AddEditDialog)
    # setupUi

    def retranslateUi(self, AddEditDialog):
        AddEditDialog.setWindowTitle(QCoreApplication.translate("AddEditDialog", u"Add Task", None))
        self.lineEditTaskname.setText("")
        self.lineEditTaskname.setPlaceholderText(QCoreApplication.translate("AddEditDialog", u"Title", None))
        self.plainTextEditDescription.setPlainText("")
        self.plainTextEditDescription.setPlaceholderText(QCoreApplication.translate("AddEditDialog", u"Description (optional)", None))
        self.checkBox_1.setText("")
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.checkBox_7.setText("")
        self.checkBox_8.setText("")
        self.checkBox_9.setText("")
        self.checkBox_10.setText("")
    # retranslateUi

