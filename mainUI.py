# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainDGdDRC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"Calibri")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_page_1.setFont(font1)
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	margin: 50px, 50px\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #99a8b2;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setFont(font1)
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	margin: 50px, 50px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #99a8b2;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        self.btn_page_3.setFont(font2)
        self.btn_page_3.setAutoFillBackground(False)
        self.btn_page_3.setStyleSheet(u"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #99a8b2;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	margin: 50px, 50px\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.Diagnostics = QWidget()
        self.Diagnostics.setObjectName(u"Diagnostics")
        self.verticalLayout_7 = QVBoxLayout(self.Diagnostics)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget.addWidget(self.Diagnostics)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(128)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.frame_3 = QFrame(self.Settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 600, 1190, 180))
        self.frame_3.setStyleSheet(u"background-color: #e6d5b8;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 90, 1190, 90))
        self.frame_4.setStyleSheet(u"background-color: #1f6f8b;\n"
"padding: 5px;\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 60, 25))
        self.label_7.setStyleSheet(u"")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 10, 100, 25))
        self.label_8.setStyleSheet(u"border: 1px solid black;")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(250, 10, 320, 25))
        self.label_9.setStyleSheet(u"border: 1px solid black;")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(110, 50, 100, 25))
        self.label_10.setStyleSheet(u"border: 1px solid black;")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 50, 60, 25))
        self.label_11.setStyleSheet(u"")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 50, 320, 25))
        self.label_12.setStyleSheet(u"border: 1px solid black;")
        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(590, 10, 3, 61))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(130, 50, 250, 20))
        self.progressBar.setFocusPolicy(Qt.NoFocus)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	border: 2px solid gray;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(255,36,0);\n"
"	width: 50%;\n"
"	border-radius: 2px;\n"
"	margin: 0.5px;\n"
"}")
        self.progressBar.setValue(60)
        self.DecrementBeamButton = QPushButton(self.frame_3)
        self.DecrementBeamButton.setObjectName(u"DecrementBeamButton")
        self.DecrementBeamButton.setGeometry(QRect(20, 50, 75, 23))
        self.IncrementBeamButton = QPushButton(self.frame_3)
        self.IncrementBeamButton.setObjectName(u"IncrementBeamButton")
        self.IncrementBeamButton.setGeometry(QRect(420, 50, 75, 23))
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(210, 0, 161, 41))
        font3 = QFont()
        font3.setPointSize(11)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"padding: 10px;")
        self.StandbyButton = QPushButton(self.frame_3)
        self.StandbyButton.setObjectName(u"StandbyButton")
        self.StandbyButton.setGeometry(QRect(1010, 0, 180, 180))
        self.StandbyButton.setStyleSheet(u"border-radius: 90px;\n"
"background-color: #FFFFFF;\n"
"border: 5px solid black;")
        self.horizontalLayoutWidget = QWidget(self.Settings)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 60, 1181, 531))
        self.SettingsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.SettingsLayout.setObjectName(u"SettingsLayout")
        self.SettingsLayout.setContentsMargins(30, 30, 0, 0)
        self.DiagnosticsFrame = QFrame(self.Settings)
        self.DiagnosticsFrame.setObjectName(u"DiagnosticsFrame")
        self.DiagnosticsFrame.setGeometry(QRect(0, -1, 1181, 101))
        self.DiagnosticsFrame.setStyleSheet(u"background-color: #FFFFFF")
        self.DiagnosticsFrame.setFrameShape(QFrame.StyledPanel)
        self.DiagnosticsFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.DiagnosticsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 131, 31))
        self.label_2 = QLabel(self.DiagnosticsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 40, 131, 31))
        self.label_3 = QLabel(self.DiagnosticsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 40, 131, 31))
        self.label_4 = QLabel(self.DiagnosticsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(550, 40, 131, 31))
        self.stackedWidget.addWidget(self.Settings)
        self.Calibration = QWidget()
        self.Calibration.setObjectName(u"Calibration")
        self.verticalLayout_8 = QVBoxLayout(self.Calibration)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget.addWidget(self.Calibration)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Diagnostics", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"980 nm:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Time:  0 Sec", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ready, please wear the safety goggles before laser emission!", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Time:  0 Sec", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"1470 nm:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ready, please wear the safety goggles before laser emission!", None))
        self.DecrementBeamButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.IncrementBeamButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Aiming Beam", None))
        self.StandbyButton.setText(QCoreApplication.translate("MainWindow", u"Ready/Standby", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temprature: 0 C", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tec: Disable", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Footswitch: Unpressed", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Interlock: Close", None))
    # retranslateUi

