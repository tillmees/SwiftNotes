from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget, QSpacerItem,
    QLineEdit, QPlainTextEdit, QDialogButtonBox, QGridLayout,
    QFrame, QCheckBox, QButtonGroup
)


class Ui_EditDialog(object):
    def setupUi(self, EditDialog):
        self.set_object_name(EditDialog)
        self.set_size_policy(EditDialog)
        self.set_window_icon(EditDialog)

        self.addEditWindowMainLayout = QVBoxLayout(EditDialog)
        self.addEditWindowMainLayout.setSpacing(10)
        self.addEditWindowMainLayout.setContentsMargins(10, 10, 10, 10)

        # Add edit section for title
        self.lineEditTaskname = QLineEdit(EditDialog)
        self.lineEditTaskname.setObjectName(u"lineEditTaskname")
        self.addEditWindowMainLayout.addWidget(self.lineEditTaskname)

        # Add edit section for description
        self.plainTextEditDescription = QPlainTextEdit(EditDialog)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")
        self.addEditWindowMainLayout.addWidget(self.plainTextEditDescription)

        # Add created timestamp
        horizontalLayout = QHBoxLayout()
        self.label_DateCreatedText = QLabel(EditDialog)
        self.label_DateCreatedText.setObjectName(u"label_DateCreatedText")
        self.label_DateCreatedText.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_DateCreated = QLabel(EditDialog)
        self.label_DateCreated.setObjectName(u"label_DateCreated")
        horizontalLayout.addWidget(self.label_DateCreatedText)
        horizontalLayout.addWidget(self.label_DateCreated, 0, Qt.AlignRight)
        horizontalLayout.setStretch(1, 1)

        self.addEditWindowMainLayout.addLayout(horizontalLayout)

        # Add changed timestamp
        horizontalLayout = QHBoxLayout()
        self.label_DateChangedText = QLabel(EditDialog)
        self.label_DateChangedText.setObjectName(u"label_DateChangedText")
        self.label_DateChangedText.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_DateChanged = QLabel(EditDialog)
        self.label_DateChanged.setObjectName(u"label_DateCreated")
        horizontalLayout.addWidget(self.label_DateChangedText)
        horizontalLayout.addWidget(self.label_DateChanged, 0, Qt.AlignRight)
        horizontalLayout.setStretch(1, 1)

        self.addEditWindowMainLayout.addLayout(horizontalLayout)

        # Add task count
        horizontalLayout = QHBoxLayout()
        self.label_NoTasksText = QLabel(EditDialog)
        self.label_NoTasksText.setObjectName(u"label_NoTasksText")
        self.label_NoTasksText.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_NoTasks = QLabel(EditDialog)
        self.label_NoTasks.setObjectName(u"label_NoTasks")
        horizontalLayout.addWidget(self.label_NoTasksText)
        horizontalLayout.addWidget(self.label_NoTasks, 0, Qt.AlignRight)
        horizontalLayout.setStretch(1, 1)

        self.addEditWindowMainLayout.addLayout(horizontalLayout)

        # Add open count
        horizontalLayout = QHBoxLayout()
        self.label_NoOpenText = QLabel(EditDialog)
        self.label_NoOpenText.setObjectName(u"label_NoOpenText")
        self.label_NoOpenText.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_NoOpen = QLabel(EditDialog)
        self.label_NoOpen.setObjectName(u"label_NoOpen")
        horizontalLayout.addWidget(self.label_NoOpenText)
        horizontalLayout.addWidget(self.label_NoOpen, 0, Qt.AlignRight)
        horizontalLayout.setStretch(1, 1)

        self.addEditWindowMainLayout.addLayout(horizontalLayout)

        # Add in progress count
        horizontalLayout = QHBoxLayout()
        self.label_NoInProgressText = QLabel(EditDialog)
        self.label_NoInProgressText.setObjectName(u"label_NoInProgressText")
        self.label_NoInProgressText.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_NoInProgress = QLabel(EditDialog)
        self.label_NoInProgress.setObjectName(u"label_NoInProgress")
        horizontalLayout.addWidget(self.label_NoInProgressText)
        horizontalLayout.addWidget(self.label_NoInProgress, 0, Qt.AlignRight)
        horizontalLayout.setStretch(1, 1)

        self.addEditWindowMainLayout.addLayout(horizontalLayout)

        # Add in stuck test count
        horizontalLayout = QHBoxLayout()
        self.label_NoStuckTestText = QLabel(EditDialog)
        self.label_NoStuckTestText.setObjectName(u"label_NoStuckTestText")
        self.label_NoStuckTestText.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_NoStuckTest = QLabel(EditDialog)
        self.label_NoStuckTest.setObjectName(u"label_NoStuckTest")
        horizontalLayout.addWidget(self.label_NoStuckTestText)
        horizontalLayout.addWidget(self.label_NoStuckTest, 0, Qt.AlignRight)
        horizontalLayout.setStretch(1, 1)

        self.addEditWindowMainLayout.addLayout(horizontalLayout)

        # Add in done count
        horizontalLayout = QHBoxLayout()
        self.label_NoDoneText = QLabel(EditDialog)
        self.label_NoDoneText.setObjectName(u"label_NoDoneText")
        self.label_NoDoneText.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_NoDone = QLabel(EditDialog)
        self.label_NoDone.setObjectName(u"label_NoDone")
        horizontalLayout.addWidget(self.label_NoDoneText)
        horizontalLayout.addWidget(self.label_NoDone, 0, Qt.AlignRight)
        horizontalLayout.setStretch(1, 1)

        self.addEditWindowMainLayout.addLayout(horizontalLayout)

    # >>> begin of color selection

        # Add color selection
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setSpacing(0)
        horizontalLayout.setObjectName(u"horizontalLayout")

        self.widget = QWidget(EditDialog)
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
        self.buttonGroup = QButtonGroup(EditDialog)
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

        # Add dialog button section
        self.dialogWidget = QWidget(EditDialog)
        self.dialogWidgetLayout = QHBoxLayout(self.dialogWidget)

        self.label_okDisabledExplanation = QLabel(self.dialogWidget)
        self.label_okDisabledExplanation.setObjectName(u"label_okDisabledExplanation")
        self.dialogWidgetLayout.addWidget(self.label_okDisabledExplanation, 0, Qt.AlignVCenter | Qt.AlignLeft)

        # Add dialog buttons
        self.buttonBoxAddCancelTask = QDialogButtonBox(EditDialog)
        self.buttonBoxAddCancelTask.setObjectName(u"buttonBoxAddCancelTask")
        self.buttonBoxAddCancelTask.setOrientation(Qt.Horizontal)
        self.buttonBoxAddCancelTask.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBoxAddCancelTask.accepted.connect(EditDialog.accept)
        self.buttonBoxAddCancelTask.rejected.connect(EditDialog.reject)

        self.dialogWidgetLayout.addWidget(self.buttonBoxAddCancelTask, 0, Qt.AlignVCenter | Qt.AlignRight)

        self.addEditWindowMainLayout.addWidget(self.dialogWidget) 
        self.set_text_of_buttons_and_labels(EditDialog)

        QMetaObject.connectSlotsByName(EditDialog)

    def set_object_name(self, EditDialog):
        if not EditDialog.objectName():
            EditDialog.setObjectName(u"EditDialog")

    def set_size_policy(self, EditDialog):
        EditDialog.resize(430, 525)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditDialog.sizePolicy().hasHeightForWidth())
        EditDialog.setSizePolicy(sizePolicy)
        EditDialog.setMinimumSize(QSize(430, 525))

    def set_window_icon(self, EditDialog):
        icon = QIcon()
        icon.addFile(u":/icons/icons/swift-notes.svg", QSize(), QIcon.Normal, QIcon.Off)
        EditDialog.setWindowIcon(icon)

    def get_color(self, widget, object_name):
        color = QFrame(widget)
        color.setObjectName(object_name)
        color.setMinimumSize(QSize(20, 20))
        color.setMaximumSize(QSize(20, 20))
        color.setFrameShape(QFrame.NoFrame)
        color.setFrameShadow(QFrame.Plain)
        return color

    def set_text_of_buttons_and_labels(self, EditDialog):
        EditDialog.setWindowTitle(QCoreApplication.translate("EditDialog", u"Add Task", None))
        self.lineEditTaskname.setText("")
        self.lineEditTaskname.setPlaceholderText(QCoreApplication.translate("EditDialog", u"Title", None))
        self.plainTextEditDescription.setPlainText("")
        self.plainTextEditDescription.setPlaceholderText(QCoreApplication.translate("EditDialog", u"Description (optional)", None))
       
        self.label_DateCreatedText.setText(QCoreApplication.translate("EditDialog", u"Created:", None))
        self.label_DateCreated.setText(QCoreApplication.translate("EditDialog", u"...Date...", None))
        self.label_DateChangedText.setText(QCoreApplication.translate("EditDialog", u"Last changed:", None))
        self.label_DateChanged.setText(QCoreApplication.translate("EditDialog", u"...Date...", None))
        
        self.label_NoTasksText.setText(QCoreApplication.translate("EditDialog", u"No. of tasks created:", None))
        self.label_NoTasks.setText(QCoreApplication.translate("EditDialog", u"...Number...", None))
        self.label_NoOpenText.setText(QCoreApplication.translate("EditDialog", u"No. of tasks in 'Open':", None))
        self.label_NoOpen.setText(QCoreApplication.translate("EditDialog", u"...Number...Percentage...", None))
        self.label_NoInProgressText.setText(QCoreApplication.translate("EditDialog", u"No. of tasks in 'In Progress':", None))
        self.label_NoInProgress.setText(QCoreApplication.translate("EditDialog", u"...Number...Percentage...", None))
        self.label_NoStuckTestText.setText(QCoreApplication.translate("EditDialog", u"No. of tasks in 'Stuck/Test':", None))
        self.label_NoStuckTest.setText(QCoreApplication.translate("EditDialog", u"...Number...Percentage...", None))
        self.label_NoDoneText.setText(QCoreApplication.translate("EditDialog", u"No. of tasks 'Done':", None))
        self.label_NoDone.setText(QCoreApplication.translate("EditDialog", u"...Number...Percentage...", None))

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

        self.label_okDisabledExplanation.setText(QCoreApplication.translate("AddDialog", u"", None))