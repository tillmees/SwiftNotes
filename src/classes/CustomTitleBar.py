import sys
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QSpacerItem, QLayout
from PySide6.QtGui import QIcon, QPixmap

from classes.TaskColors import darken_color 

import resources_rc


class CustomWindowButton(QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.icon = QIcon()
        self.icon.addFile(icon_path, QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(self.icon)
        self.setIconSize(QSize(11, 11))
        self.setFixedSize(QSize(46, 30))


class CustomWindowBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.window_icon = QLabel()
        self.window_icon.setFixedSize(QSize(22, 17))
        self.window_icon.setPixmap(QPixmap(u":/icons/icons/swift-notes.svg").scaled(17, 17, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        self.window_title = QLabel("SwiftNotes")
        self.window_title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.window_title.setObjectName(u"windowTitle")

        self.horizontalSpacer = QSpacerItem(200000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addWidget(self.window_icon, 0, Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.window_title, 0, Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout.addItem(self.horizontalSpacer)

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_pos)
        self.window().move(self.window().pos() + delta)
        self.old_pos = event.globalPos()


class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(30)

        self.isMaximized = False

        self.centralLayout = QHBoxLayout(self)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.setSpacing(0)

        self.backgroundWidget = QWidget()
        self.backgroundWidget.setObjectName(u"backgroundTitleBar")

        self.horizontalLayout = QHBoxLayout(self.backgroundWidget)
        self.horizontalLayout.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.windowBar = CustomWindowBar()
        self.windowBar.setObjectName(u"windowBar")

        self.btn_minimize = CustomWindowButton(u":/icons/icons/minimize-window.svg")
        self.btn_minimize.clicked.connect(parent.showMinimized)
        self.btn_minimize.setObjectName(u"buttonWindowResize")
        self.btn_minimize.setText("")

        self.btn_maximize = CustomWindowButton(u":/icons/icons/maximize-window.svg")
        self.btn_maximize.clicked.connect(self.toggleMaximizeButton)
        self.btn_maximize.clicked.connect(parent.toggleMaximizeRestore)
        self.btn_maximize.setObjectName(u"buttonWindowResize")
        self.btn_maximize.setText("")

        self.btn_restore = CustomWindowButton(u":/icons/icons/restore-window.svg")
        self.btn_restore.clicked.connect(self.toggleMaximizeButton)
        self.btn_restore.clicked.connect(parent.toggleMaximizeRestore)
        self.btn_restore.setObjectName(u"buttonWindowResize")
        self.btn_restore.setText("")
        self.btn_restore.hide()

        self.btn_close = CustomWindowButton(u":/icons/icons/close-window.svg")
        self.btn_close.clicked.connect(parent.close)
        self.btn_close.setObjectName(u"buttonCloseWindow")
        self.btn_close.setText("")

        self.horizontalSpacer = QSpacerItem(200000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addWidget(self.windowBar, 0, Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.btn_minimize, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.btn_maximize, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.btn_restore, 0, Qt.AlignRight|Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.btn_close, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.centralLayout.addWidget(self.backgroundWidget)

    def toggleMaximizeButton(self, parent):
        if self.isMaximized:
            self.isMaximized = False
            self.btn_restore.hide()
            self.btn_maximize.show()
        else:
            self.isMaximized = True
            self.btn_restore.show()
            self.btn_maximize.hide()
        
    def set_window_title(self, title):
        self.windowBar.window_title.setText(title)