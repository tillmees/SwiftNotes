# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

from classes.CustomScrollArea import CustomScrollArea
from classes.CustomTitleBar import CustomTitleBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 510)
        icon = QIcon()
        icon.addFile(u":/icons/icons/swift-notes.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(55, 55))
        self.mainCentralwidget = QWidget(MainWindow)
        self.mainCentralwidget.setObjectName(u"centralwidget")

        self.mainVerticalLayout = QVBoxLayout(self.mainCentralwidget)
        self.mainVerticalLayout.setSpacing(0)
        self.mainVerticalLayout.setObjectName(u"mainVerticalLayout")
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)

        # self.title_bar = CustomTitleBar(MainWindow)
        # self.mainVerticalLayout.addWidget(self.title_bar)

        self.centralwidget = QWidget(self.mainCentralwidget)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.IconSidebarQWidget = QWidget(self.mainCentralwidget)
        self.IconSidebarQWidget.setObjectName(u"IconSidebarQWidget")
        self.IconSidebarQWidget.setMinimumSize(QSize(40, 0))
        self.IconSidebarQWidget.setMaximumSize(QSize(30, 16777215))
        self.IconSidebarQWidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.IconSidebarQWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.pushButtonIconNew = QPushButton(self.IconSidebarQWidget)
        self.pushButtonIconNew.setObjectName(u"pushButtonIconNew")
        self.pushButtonIconNew.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonIconNew.setIcon(icon1)
        self.pushButtonIconNew.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.pushButtonIconNew, 0, Qt.AlignHCenter)

        self.pushButtonIconOpen = QPushButton(self.IconSidebarQWidget)
        self.pushButtonIconOpen.setObjectName(u"pushButtonIconOpen")
        self.pushButtonIconOpen.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonIconOpen.setIcon(icon2)

        self.verticalLayout.addWidget(self.pushButtonIconOpen, 0, Qt.AlignHCenter)

        self.pushButtonIconSave = QPushButton(self.IconSidebarQWidget)
        self.pushButtonIconSave.setObjectName(u"pushButtonIconSave")
        self.pushButtonIconSave.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonIconSave.setIcon(icon3)

        self.verticalLayout.addWidget(self.pushButtonIconSave, 0, Qt.AlignHCenter)

        self.pushButtonIconSaveAs = QPushButton(self.IconSidebarQWidget)
        self.pushButtonIconSaveAs.setObjectName(u"pushButtonIconSaveAs")
        self.pushButtonIconSaveAs.setMaximumSize(QSize(16777215, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/save-as.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonIconSaveAs.setIcon(icon4)

        self.verticalLayout.addWidget(self.pushButtonIconSaveAs, 0, Qt.AlignHCenter)

        self.IconHorizontalLine = QFrame(self.IconSidebarQWidget)
        self.IconHorizontalLine.setObjectName(u"IconHorizontalLine")
        self.IconHorizontalLine.setFrameShape(QFrame.HLine)
        self.IconHorizontalLine.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.IconHorizontalLine)

        self.pushButtonIconAdd = QPushButton(self.IconSidebarQWidget)
        self.pushButtonIconAdd.setObjectName(u"pushButtonIconAdd")
        self.pushButtonIconAdd.setMaximumSize(QSize(16777215, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonIconAdd.setIcon(icon5)

        self.verticalLayout.addWidget(self.pushButtonIconAdd, 0, Qt.AlignHCenter)

        self.pushButtonIconClose = QPushButton(self.IconSidebarQWidget)
        self.pushButtonIconClose.setObjectName(u"pushButtonIconClose")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/minimize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonIconClose.setIcon(icon6)

        self.verticalLayout.addWidget(self.pushButtonIconClose, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 309, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButtonIconTask = QPushButton(self.IconSidebarQWidget)
        self.pushButtonIconTask.setObjectName(u"pushButtonIconTask")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonIconTask.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.pushButtonIconTask, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.horizontalLayout.addWidget(self.IconSidebarQWidget)

        self.FullSidebarQWidget = QWidget(self.mainCentralwidget)
        self.FullSidebarQWidget.setObjectName(u"FullSidebarQWidget")
        self.FullSidebarQWidget.setMinimumSize(QSize(200, 0))
        self.FullSidebarQWidget.setMaximumSize(QSize(200, 16777215))
        self.FullSidebarQWidget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.FullSidebarQWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelVersion = QLabel(self.FullSidebarQWidget)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.labelVersion, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.pushButtonFullNew = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullNew.setObjectName(u"pushButtonFullNew")
        self.pushButtonFullNew.setMinimumSize(QSize(190, 0))
        self.pushButtonFullNew.setIcon(icon1)
        self.pushButtonFullNew.setIconSize(QSize(14, 14))

        self.verticalLayout_2.addWidget(self.pushButtonFullNew, 0, Qt.AlignHCenter)

        self.pushButtonFullOpen = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullOpen.setObjectName(u"pushButtonFullOpen")
        self.pushButtonFullOpen.setMinimumSize(QSize(190, 0))
        self.pushButtonFullOpen.setIcon(icon2)
        self.pushButtonFullOpen.setIconSize(QSize(14, 14))

        self.verticalLayout_2.addWidget(self.pushButtonFullOpen, 0, Qt.AlignHCenter)

        self.pushButtonFullSave = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullSave.setObjectName(u"pushButtonFullSave")
        self.pushButtonFullSave.setMinimumSize(QSize(190, 0))
        self.pushButtonFullSave.setIcon(icon3)
        self.pushButtonFullSave.setIconSize(QSize(14, 14))

        self.verticalLayout_2.addWidget(self.pushButtonFullSave, 0, Qt.AlignHCenter)

        self.pushButtonFullSaveAs = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullSaveAs.setObjectName(u"pushButtonFullSaveAs")
        self.pushButtonFullSaveAs.setMinimumSize(QSize(190, 0))
        self.pushButtonFullSaveAs.setIcon(icon4)
        self.pushButtonFullSaveAs.setIconSize(QSize(14, 14))

        self.verticalLayout_2.addWidget(self.pushButtonFullSaveAs, 0, Qt.AlignHCenter)

        self.FullHorizontalLine = QFrame(self.FullSidebarQWidget)
        self.FullHorizontalLine.setObjectName(u"FullHorizontalLine")
        self.FullHorizontalLine.setFrameShape(QFrame.HLine)
        self.FullHorizontalLine.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.FullHorizontalLine)

        self.pushButtonFullAdd = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullAdd.setObjectName(u"pushButtonFullAdd")
        self.pushButtonFullAdd.setMinimumSize(QSize(190, 0))
        self.pushButtonFullAdd.setIcon(icon5)
        self.pushButtonFullAdd.setIconSize(QSize(14, 14))

        self.verticalLayout_2.addWidget(self.pushButtonFullAdd, 0, Qt.AlignHCenter)

        self.pushButtonFullClose = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullClose.setObjectName(u"pushButtonFullClose")
        self.pushButtonFullClose.setMinimumSize(QSize(190, 0))
        self.pushButtonFullClose.setIcon(icon6)
        self.pushButtonFullClose.setIconSize(QSize(14, 14))

        self.verticalLayout_2.addWidget(self.pushButtonFullClose, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 282, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_light = QLabel(self.FullSidebarQWidget)
        self.label_light.setObjectName(u"label_light")

        self.horizontalLayout_3.addWidget(self.label_light, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.pushButtonFullLayout = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullLayout.setObjectName(u"pushButtonFullLayout")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/toggle-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonFullLayout.setIcon(icon8)
        self.pushButtonFullLayout.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.pushButtonFullLayout, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_dark = QLabel(self.FullSidebarQWidget)
        self.label_dark.setObjectName(u"label_dark")

        self.horizontalLayout_3.addWidget(self.label_dark, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_9 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.pushButtonFullTask = QPushButton(self.FullSidebarQWidget)
        self.pushButtonFullTask.setObjectName(u"pushButtonFullTask")
        self.pushButtonFullTask.setMinimumSize(QSize(190, 0))
        self.pushButtonFullTask.setIcon(icon7)
        self.pushButtonFullTask.setIconSize(QSize(14, 14))

        self.verticalLayout_4.addWidget(self.pushButtonFullTask)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)


        self.horizontalLayout.addWidget(self.FullSidebarQWidget)

        self.MainViewQWidget = QWidget(self.mainCentralwidget)
        self.MainViewQWidget.setObjectName(u"MainViewQWidget")
        self.MainViewQWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_5 = QVBoxLayout(self.MainViewQWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.TopBarQWidget = QWidget(self.MainViewQWidget)
        self.TopBarQWidget.setObjectName(u"TopBarQWidget")
        self.TopBarQWidget.setMinimumSize(QSize(0, 0))
        self.TopBarQWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.TopBarQWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButtonToggleMenu = QPushButton(self.TopBarQWidget)
        self.pushButtonToggleMenu.setObjectName(u"pushButtonToggleMenu")
        self.pushButtonToggleMenu.setMaximumSize(QSize(30, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonToggleMenu.setIcon(icon9)
        self.pushButtonToggleMenu.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButtonToggleMenu, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.comboBoxProjects = QComboBox(self.TopBarQWidget)
        self.comboBoxProjects.setObjectName(u"comboBoxProjects")
        self.comboBoxProjects.setMinimumSize(QSize(250, 0))
        self.comboBoxProjects.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.comboBoxProjects)

        self.horizontalSpacer = QSpacerItem(497, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.TopBarQWidget, 0, Qt.AlignTop)

        self.TaskWindowstackedWidget = QStackedWidget(self.MainViewQWidget)
        self.TaskWindowstackedWidget.setObjectName(u"TaskWindowstackedWidget")
        self.WelcomePage = QWidget()
        self.WelcomePage.setObjectName(u"WelcomePage")
        self.verticalLayout_7 = QVBoxLayout(self.WelcomePage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_6 = QSpacerItem(20, 206, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.labelWelcome = QLabel(self.WelcomePage)
        self.labelWelcome.setObjectName(u"labelWelcome")
        self.labelWelcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.labelWelcome)

        self.labelWelcomeDrop = QLabel(self.WelcomePage)
        self.labelWelcomeDrop.setObjectName(u"labelWelcomeDrop")
        self.labelWelcomeDrop.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.labelWelcomeDrop)

        self.verticalSpacer_5 = QSpacerItem(20, 206, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.TaskWindowstackedWidget.addWidget(self.WelcomePage)
        self.TaskPage = QWidget()
        self.TaskPage.setObjectName(u"TaskPage")
        self.gridLayout = QGridLayout(self.TaskPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.labelOpen = QLabel(self.TaskPage)
        self.labelOpen.setObjectName(u"labelOpen")

        self.gridLayout.addWidget(self.labelOpen, 0, 0, 1, 1, Qt.AlignLeft)

        self.labelInProgress = QLabel(self.TaskPage)
        self.labelInProgress.setObjectName(u"labelInProgress")

        self.gridLayout.addWidget(self.labelInProgress, 0, 2, 1, 1, Qt.AlignLeft)

        self.labelStuckTest = QLabel(self.TaskPage)
        self.labelStuckTest.setObjectName(u"labelStuckTest")

        self.gridLayout.addWidget(self.labelStuckTest, 0, 4, 1, 1, Qt.AlignLeft)

        self.labelDone = QLabel(self.TaskPage)
        self.labelDone.setObjectName(u"labelDone")

        self.gridLayout.addWidget(self.labelDone, 0, 6, 1, 1, Qt.AlignLeft)

        self.scrollAreaOpen = CustomScrollArea("open", self.TaskPage)
        self.scrollAreaOpen.setObjectName(u"scrollAreaOpen")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaOpen.sizePolicy().hasHeightForWidth())
        self.scrollAreaOpen.setSizePolicy(sizePolicy)
        self.scrollAreaOpen.setAcceptDrops(True)
        self.scrollAreaOpen.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaOpen.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaOpen.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollAreaOpen.setWidgetResizable(True)
        self.scrollAreaWidgetContentsOpen = QWidget()
        self.scrollAreaWidgetContentsOpen.setObjectName(u"scrollAreaWidgetContentsOpen")
        self.scrollAreaWidgetContentsOpen.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContentsOpen)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollAreaOpen.setWidget(self.scrollAreaWidgetContentsOpen)

        self.gridLayout.addWidget(self.scrollAreaOpen, 1, 0, 1, 2)

        self.scrollAreaInProgress = CustomScrollArea("in progress", self.TaskPage)
        self.scrollAreaInProgress.setObjectName(u"scrollAreaInProgress")
        sizePolicy.setHeightForWidth(self.scrollAreaInProgress.sizePolicy().hasHeightForWidth())
        self.scrollAreaInProgress.setSizePolicy(sizePolicy)
        self.scrollAreaInProgress.setAcceptDrops(True)
        self.scrollAreaInProgress.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaInProgress.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaInProgress.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollAreaInProgress.setWidgetResizable(True)
        self.scrollAreaWidgetContentsInProgress = QWidget()
        self.scrollAreaWidgetContentsInProgress.setObjectName(u"scrollAreaWidgetContentsInProgress")
        self.scrollAreaWidgetContentsInProgress.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContentsInProgress)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollAreaInProgress.setWidget(self.scrollAreaWidgetContentsInProgress)

        self.gridLayout.addWidget(self.scrollAreaInProgress, 1, 2, 1, 2)

        self.scrollAreaStuckTest = CustomScrollArea("stuck/test", self.TaskPage)
        self.scrollAreaStuckTest.setObjectName(u"scrollAreaStuckTest")
        sizePolicy.setHeightForWidth(self.scrollAreaStuckTest.sizePolicy().hasHeightForWidth())
        self.scrollAreaStuckTest.setSizePolicy(sizePolicy)
        self.scrollAreaStuckTest.setAcceptDrops(True)
        self.scrollAreaStuckTest.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaStuckTest.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaStuckTest.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollAreaStuckTest.setWidgetResizable(True)
        self.scrollAreaWidgetContentsStuckTest = QWidget()
        self.scrollAreaWidgetContentsStuckTest.setObjectName(u"scrollAreaWidgetContentsStuckTest")
        self.scrollAreaWidgetContentsStuckTest.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContentsStuckTest)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollAreaStuckTest.setWidget(self.scrollAreaWidgetContentsStuckTest)

        self.gridLayout.addWidget(self.scrollAreaStuckTest, 1, 4, 1, 2)

        self.scrollAreaDone = CustomScrollArea("done", self.TaskPage)
        self.scrollAreaDone.setObjectName(u"scrollAreaDone")
        sizePolicy.setHeightForWidth(self.scrollAreaDone.sizePolicy().hasHeightForWidth())
        self.scrollAreaDone.setSizePolicy(sizePolicy)
        self.scrollAreaDone.setAcceptDrops(True)
        self.scrollAreaDone.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaDone.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaDone.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollAreaDone.setWidgetResizable(True)
        self.scrollAreaWidgetContentsDone = QWidget()
        self.scrollAreaWidgetContentsDone.setObjectName(u"scrollAreaWidgetContentsDone")
        self.scrollAreaWidgetContentsDone.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContentsDone)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollAreaDone.setWidget(self.scrollAreaWidgetContentsDone)

        self.gridLayout.addWidget(self.scrollAreaDone, 1, 6, 1, 2)

        self.labelOpenOutOf = QLabel(self.TaskPage)
        self.labelOpenOutOf.setObjectName(u"labelOpenOutOf")

        self.gridLayout.addWidget(self.labelOpenOutOf, 2, 1, 1, 1, Qt.AlignRight)

        self.labelInProgressOutOf = QLabel(self.TaskPage)
        self.labelInProgressOutOf.setObjectName(u"labelInProgressOutOf")

        self.gridLayout.addWidget(self.labelInProgressOutOf, 2, 3, 1, 1, Qt.AlignRight)

        self.labelStuckTestOutOf = QLabel(self.TaskPage)
        self.labelStuckTestOutOf.setObjectName(u"labelStuckTestOutOf")

        self.gridLayout.addWidget(self.labelStuckTestOutOf, 2, 5, 1, 1, Qt.AlignRight)

        self.labelDoneOutOf = QLabel(self.TaskPage)
        self.labelDoneOutOf.setObjectName(u"labelDoneOutOf")

        self.gridLayout.addWidget(self.labelDoneOutOf, 2, 7, 1, 1, Qt.AlignRight)

        self.TaskWindowstackedWidget.addWidget(self.TaskPage)
        self.ProjectPage = QWidget()
        self.ProjectPage.setObjectName(u"ProjectPage")
        self.verticalLayout_8 = QVBoxLayout(self.ProjectPage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 29)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, 5)
        self.label = QLabel(self.ProjectPage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.labelSort = QLabel(self.ProjectPage)
        self.labelSort.setObjectName(u"labelSort")

        self.horizontalLayout_4.addWidget(self.labelSort, 0, Qt.AlignHCenter)

        self.pushButtonSort = QPushButton(self.ProjectPage)
        self.pushButtonSort.setObjectName(u"pushButtonSort")
        self.pushButtonSort.setMaximumSize(QSize(16777215, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSort.setIcon(icon10)
        self.pushButtonSort.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.pushButtonSort, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.ProjectPagestackedWidget = QStackedWidget(self.ProjectPage)
        self.ProjectPagestackedWidget.setObjectName(u"ProjectPagestackedWidget")
        self.pageList = QWidget()
        self.pageList.setObjectName(u"pageList")
        self.verticalLayout_9 = QVBoxLayout(self.pageList)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaProjectsList = QScrollArea(self.pageList)
        self.scrollAreaProjectsList.setObjectName(u"scrollAreaProjectsList")
        self.scrollAreaProjectsList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaProjectsList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaProjectsList.setWidgetResizable(True)
        self.scrollAreaWidgetContentsProjectsList = QWidget()
        self.scrollAreaWidgetContentsProjectsList.setObjectName(u"scrollAreaWidgetContentsProjectsList")
        self.scrollAreaWidgetContentsProjectsList.setGeometry(QRect(0, 0, 718, 417))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContentsProjectsList)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollAreaProjectsList.setWidget(self.scrollAreaWidgetContentsProjectsList)

        self.verticalLayout_9.addWidget(self.scrollAreaProjectsList)

        self.ProjectPagestackedWidget.addWidget(self.pageList)
        self.pageGrid = QWidget()
        self.pageGrid.setObjectName(u"pageGrid")
        self.verticalLayout_14 = QVBoxLayout(self.pageGrid)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea = QScrollArea(self.pageGrid)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)

        self.ProjectPagestackedWidget.addWidget(self.pageGrid)

        self.verticalLayout_8.addWidget(self.ProjectPagestackedWidget)

        self.TaskWindowstackedWidget.addWidget(self.ProjectPage)

        self.verticalLayout_5.addWidget(self.TaskWindowstackedWidget)


        self.horizontalLayout.addWidget(self.MainViewQWidget)

        self.mainVerticalLayout.addWidget(self.centralwidget)

        MainWindow.setCentralWidget(self.mainCentralwidget)

        self.retranslateUi(MainWindow)
        self.pushButtonToggleMenu.toggled.connect(self.IconSidebarQWidget.setHidden)
        self.pushButtonToggleMenu.toggled.connect(self.FullSidebarQWidget.setVisible)

        self.TaskWindowstackedWidget.setCurrentIndex(0)
        self.ProjectPagestackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SwiftNotes", None))
        self.pushButtonIconNew.setText("")
        self.pushButtonIconOpen.setText("")
        self.pushButtonIconSave.setText("")
        self.pushButtonIconSaveAs.setText("")
        self.pushButtonIconAdd.setText("")
        self.pushButtonIconClose.setText("")
        self.pushButtonIconTask.setText("")
        self.labelVersion.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.pushButtonFullNew.setText(QCoreApplication.translate("MainWindow", u" New...", None))
        self.pushButtonFullOpen.setText(QCoreApplication.translate("MainWindow", u" Open...", None))
        self.pushButtonFullSave.setText(QCoreApplication.translate("MainWindow", u" Save", None))
        self.pushButtonFullSaveAs.setText(QCoreApplication.translate("MainWindow", u" Save As...", None))
        self.pushButtonFullAdd.setText(QCoreApplication.translate("MainWindow", u" Add Project", None))
        self.pushButtonFullClose.setText(QCoreApplication.translate("MainWindow", u" Close Project", None))
        self.label_light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.pushButtonFullLayout.setText("")
        self.label_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.pushButtonFullTask.setText(QCoreApplication.translate("MainWindow", u" Add Task", None))
        self.pushButtonToggleMenu.setText("")
        self.labelWelcome.setText(QCoreApplication.translate("MainWindow", u"Add a new project", None))
        self.labelWelcomeDrop.setText(QCoreApplication.translate("MainWindow", u"or open an existing .todo file", None))
        self.labelOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelInProgress.setText(QCoreApplication.translate("MainWindow", u"In Progess", None))
        self.labelStuckTest.setText(QCoreApplication.translate("MainWindow", u"Stuck/Test", None))
        self.labelDone.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.labelOpenOutOf.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelInProgressOutOf.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelStuckTestOutOf.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.labelDoneOutOf.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.labelSort.setText(QCoreApplication.translate("MainWindow", u"sorted by: Title", None))
        self.pushButtonSort.setText("")
    # retranslateUi
