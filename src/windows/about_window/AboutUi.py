from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget, QSpacerItem,
    QLineEdit, QPlainTextEdit, QDialogButtonBox, QGridLayout,
    QFrame, QCheckBox, QButtonGroup
)


class Ui_About(object):
    def setupUi(self, AboutWidget):
        self.set_object_name(AboutWidget)

        self.background = QLabel(AboutWidget)
        self.pixmap = QPixmap(u":/graphics/graphics/about.png")
        self.background.setPixmap(self.pixmap)
        self.background.setScaledContents(True)

        self.layout = QVBoxLayout(self.background)

        self.vertical_top_spacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout.addItem(self.vertical_top_spacer)

        self.version_label = QLabel(AboutWidget)
        self.version_label.setText("")
        self.version_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.version_label, 0, Qt.AlignVCenter | Qt.AlignHCenter)

        self.copyright_label = QLabel(AboutWidget)
        self.copyright_label.setText("")
        self.copyright_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.copyright_label, 0, Qt.AlignVCenter | Qt.AlignHCenter)

        self.url_label = QLabel(AboutWidget)
        self.url_label.setText("")
        self.url_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.url_label, 0, Qt.AlignVCenter | Qt.AlignHCenter)

        self.vertical_bot_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(self.vertical_bot_spacer)

        self.set_size_policy(AboutWidget)
        self.set_window_icon(AboutWidget)
        AboutWidget.setWindowTitle(QCoreApplication.translate("AboutWidget", u"About", None))

    def set_object_name(self, AboutWidget):
        if not AboutWidget.objectName():
            AboutWidget.setObjectName(u"AboutWidget")

    def set_size_policy(self, AboutWidget):
        width = self.pixmap.width()
        height = self.pixmap.height()
        AboutWidget.resize(width, height)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutWidget.sizePolicy().hasHeightForWidth())
        AboutWidget.setSizePolicy(sizePolicy)
        AboutWidget.setMinimumSize(QSize(width, height))
        AboutWidget.setMaximumSize(QSize(width, height))

    def set_window_icon(self, AboutWidget):
        icon = QIcon()
        icon.addFile(u":/icons/icons/swift-notes.svg", QSize(), QIcon.Normal, QIcon.Off)
        AboutWidget.setWindowIcon(icon)

    def set_text(self, version):
        self.version_label.setText(f"SwiftNotes v{version}") 
        self.copyright_label.setText("Copyright © 2024 Till Meeske")
        self.url_label.setText("<a href='https://github.com/tillmees/swift-notes'>https://github.com/tillmees/swift-notes</a>")
        self.url_label.setOpenExternalLinks(True)
