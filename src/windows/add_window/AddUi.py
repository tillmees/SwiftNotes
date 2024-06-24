from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget, QSpacerItem,
    QLineEdit, QPlainTextEdit, QDialogButtonBox, QGridLayout,
    QFrame, QCheckBox, QButtonGroup
)


class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        self.set_object_name(AddDialog)
        self.set_size_policy(AddDialog)
        self.set_window_icon(AddDialog)

        self.addEditWindowMainLayout = QVBoxLayout(AddDialog)
        self.addEditWindowMainLayout.setSpacing(10)
        self.addEditWindowMainLayout.setContentsMargins(10, 10, 10, 10)

        # Add edit section for title
        self.lineEditTaskname = QLineEdit(AddDialog)
        self.lineEditTaskname.setObjectName(u"lineEditTaskname")
        self.addEditWindowMainLayout.addWidget(self.lineEditTaskname)

        # Add edit section for description
        self.plainTextEditDescription = QPlainTextEdit(AddDialog)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")
        self.addEditWindowMainLayout.addWidget(self.plainTextEditDescription)

    # >>> begin of color selection

        # Add color selection
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setSpacing(0)
        horizontalLayout.setObjectName(u"horizontalLayout")

        self.widget = QWidget(AddDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)

        # Add colors
        self.color_1 = self.get_color(self.widget, u"color_1")
        self.gridLayout.addWidget(self.color_1, 0, 0, 1, 1)

        self.color_2 = self.get_color(self.widget, u"color_2")
        self.gridLayout.addWidget(self.color_2, 0, 1, 1, 1)

        self.color_3 = self.get_color(self.widget, u"color_3")
        self.gridLayout.addWidget(self.color_3, 0, 2, 1, 1)

        self.color_4 = self.get_color(self.widget, u"color_4")
        self.gridLayout.addWidget(self.color_4, 0, 3, 1, 1)

        self.color_5 = self.get_color(self.widget, u"color_5")
        self.gridLayout.addWidget(self.color_5, 0, 4, 1, 1)

        self.color_6 = self.get_color(self.widget, u"color_6")
        self.gridLayout.addWidget(self.color_6, 0, 5, 1, 1)

        self.color_7 = self.get_color(self.widget, u"color_7")
        self.gridLayout.addWidget(self.color_7, 0, 6, 1, 1)

        self.color_8 = self.get_color(self.widget, u"color_8")
        self.gridLayout.addWidget(self.color_8, 0, 7, 1, 1)

        self.color_9 = self.get_color(self.widget, u"color_9")
        self.gridLayout.addWidget(self.color_9, 0, 8, 1, 1)

        self.color_10 = self.get_color(self.widget, u"color_10")
        self.gridLayout.addWidget(self.color_10, 0, 9, 1, 1)

        # Add selection
        self.buttonGroup = QButtonGroup(AddDialog)
        self.buttonGroup.setObjectName(u"buttonGroup")

        self.checkBox_1 = QCheckBox(self.widget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setAutoFillBackground(False)
        self.checkBox_1.setStyleSheet(u"")
        self.checkBox_1.setChecked(True)
        self.buttonGroup.addButton(self.checkBox_1)
        self.gridLayout.addWidget(self.checkBox_1, 1, 0, 1, 1, Qt.AlignHCenter)

        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.buttonGroup.addButton(self.checkBox_2)
        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1, Qt.AlignHCenter)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.buttonGroup.addButton(self.checkBox_3)
        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1, Qt.AlignHCenter)

        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.buttonGroup.addButton(self.checkBox_4)
        self.gridLayout.addWidget(self.checkBox_4, 1, 3, 1, 1, Qt.AlignHCenter)

        self.checkBox_5 = QCheckBox(self.widget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.buttonGroup.addButton(self.checkBox_5)
        self.gridLayout.addWidget(self.checkBox_5, 1, 4, 1, 1, Qt.AlignHCenter)

        self.checkBox_6 = QCheckBox(self.widget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.buttonGroup.addButton(self.checkBox_6)
        self.gridLayout.addWidget(self.checkBox_6, 1, 5, 1, 1, Qt.AlignHCenter)

        self.checkBox_7 = QCheckBox(self.widget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.buttonGroup.addButton(self.checkBox_7)
        self.gridLayout.addWidget(self.checkBox_7, 1, 6, 1, 1, Qt.AlignHCenter)

        self.checkBox_8 = QCheckBox(self.widget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.buttonGroup.addButton(self.checkBox_8)
        self.gridLayout.addWidget(self.checkBox_8, 1, 7, 1, 1, Qt.AlignHCenter)

        self.checkBox_9 = QCheckBox(self.widget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.buttonGroup.addButton(self.checkBox_9)
        self.gridLayout.addWidget(self.checkBox_9, 1, 8, 1, 1, Qt.AlignHCenter)

        self.checkBox_10 = QCheckBox(self.widget)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.buttonGroup.addButton(self.checkBox_10)
        self.gridLayout.addWidget(self.checkBox_10, 1, 9, 1, 1, Qt.AlignHCenter)

        horizontalLayout.addWidget(self.widget)
        self.addEditWindowMainLayout.addLayout(horizontalLayout)

    # <<< end of color selection

        # Add dialog buttons
        self.buttonBoxAddCancelTask = QDialogButtonBox(AddDialog)
        self.buttonBoxAddCancelTask.setObjectName(u"buttonBoxAddCancelTask")
        self.buttonBoxAddCancelTask.setOrientation(Qt.Horizontal)
        self.buttonBoxAddCancelTask.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBoxAddCancelTask.accepted.connect(AddDialog.accept)
        self.buttonBoxAddCancelTask.rejected.connect(AddDialog.reject)

        self.addEditWindowMainLayout.addWidget(self.buttonBoxAddCancelTask) 

        self.set_text_of_buttons_and_labels(AddDialog)

        QMetaObject.connectSlotsByName(AddDialog)

    def set_object_name(self, AddDialog):
        if not AddDialog.objectName():
            AddDialog.setObjectName(u"AddDialog")

    def set_size_policy(self, AddDialog):
        AddDialog.resize(430, 525)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddDialog.sizePolicy().hasHeightForWidth())
        AddDialog.setSizePolicy(sizePolicy)
        AddDialog.setMinimumSize(QSize(430, 525))

    def set_window_icon(self, AddDialog):
        icon = QIcon()
        icon.addFile(u":/icons/icons/swift-notes.svg", QSize(), QIcon.Normal, QIcon.Off)
        AddDialog.setWindowIcon(icon)

    def get_color(self, widget, object_name):
        color = QFrame(widget)
        color.setObjectName(object_name)
        color.setMinimumSize(QSize(20, 20))
        color.setMaximumSize(QSize(20, 20))
        color.setFrameShape(QFrame.NoFrame)
        color.setFrameShadow(QFrame.Plain)
        return color

    def set_text_of_buttons_and_labels(self, AddDialog):
        AddDialog.setWindowTitle(QCoreApplication.translate("AddDialog", u"Add", None))
        self.lineEditTaskname.setText("")
        self.lineEditTaskname.setPlaceholderText(QCoreApplication.translate("AddDialog", u"Title", None))
        self.plainTextEditDescription.setPlainText("")
        self.plainTextEditDescription.setPlaceholderText(QCoreApplication.translate("AddDialog", u"Description (optional)", None))

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