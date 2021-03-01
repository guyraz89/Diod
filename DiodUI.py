# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_diodnuQlXI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DiodSettings(object):
    def setupUi(self, DiodSettings):
        if not DiodSettings.objectName():
            DiodSettings.setObjectName(u"DiodSettings")
        DiodSettings.resize(550, 470)
        self.MainFrame = QFrame(DiodSettings)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(0, 0, 570, 520))
        self.MainFrame.setStyleSheet(u"")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.MainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 550, 330))
        self.frame.setStyleSheet(u"background-color: #1f6f8b;\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nmLabel = QLabel(self.frame)
        self.nmLabel.setObjectName(u"nmLabel")
        self.nmLabel.setGeometry(QRect(10, 10, 50, 20))
        self.nmLabel.setStyleSheet(u"padding: 3px;\n"
"background-color: #eb5e0b;\n"
"")
        self.CWRadioButton = QRadioButton(self.frame)
        self.CWRadioButton.setObjectName(u"CWRadioButton")
        self.CWRadioButton.setGeometry(QRect(410, 70, 82, 17))
        self.SingleRadioButton = QRadioButton(self.frame)
        self.SingleRadioButton.setObjectName(u"SingleRadioButton")
        self.SingleRadioButton.setGeometry(QRect(410, 120, 82, 17))
        self.RepeatRadioButton = QRadioButton(self.frame)
        self.RepeatRadioButton.setObjectName(u"RepeatRadioButton")
        self.RepeatRadioButton.setGeometry(QRect(410, 170, 82, 17))
        self.EnableButton = QPushButton(self.frame)
        self.EnableButton.setObjectName(u"EnableButton")
        self.EnableButton.setGeometry(QRect(410, 20, 75, 25))
        self.EnableButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid #8F8F91;\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x: 0, y2: 1,\n"
"															stop: 0 #F6F7FA, stop: 1 #DADBDE);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x: 0, y2: 1,\n"
"															stop: 0 #DADBDE, stop: 1 #F6F7FA);\n"
"}")
        self.PowerLabel = QLabel(self.frame)
        self.PowerLabel.setObjectName(u"PowerLabel")
        self.PowerLabel.setGeometry(QRect(160, 70, 180, 120))
        self.PowerLabel.setStyleSheet(u"background-color: #FFFFFF;\n"
"font-size: 20px;\n"
"padding-left: 30px;")
        self.IncrementPowerButton = QPushButton(self.frame)
        self.IncrementPowerButton.setObjectName(u"IncrementPowerButton")
        self.IncrementPowerButton.setGeometry(QRect(30, 80, 75, 23))
        self.IncrementPowerButton.setStyleSheet(u"")
        self.DecrementPowerButton = QPushButton(self.frame)
        self.DecrementPowerButton.setObjectName(u"DecrementPowerButton")
        self.DecrementPowerButton.setGeometry(QRect(30, 160, 75, 23))
        self.DecrementPowerButton.setStyleSheet(u"")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 260, 550, 70))
        self.frame_2.setStyleSheet(u"background-color: #e6d5b8")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 29, 60, 31))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 29, 60, 31))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 29, 100, 30))
        self.label_5.setStyleSheet(u"background-color: #FFFFFF;\n"
"padding: 5px")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 29, 100, 30))
        self.label_6.setStyleSheet(u"background-color: #FFFFFF;\n"
"padding: 5px;")
        self.frame_5 = QFrame(self.MainFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 365, 550, 130))
        self.frame_5.setStyleSheet(u"background-color: #e6d5b8;\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(40, 50, 161, 50))
        self.frame_6.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(60, 20, 50, 15))
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 12, 31, 31))
        self.pushButton.setStyleSheet(u"")
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 12, 31, 31))
        self.pushButton_4.setStyleSheet(u"")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(50, 30, 31, 16))
        self.label_14.setStyleSheet(u"")
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(160, 30, 31, 16))
        self.label_15.setStyleSheet(u"")
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(300, 30, 31, 16))
        self.label_17.setStyleSheet(u"")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(410, 30, 31, 16))
        self.label_18.setStyleSheet(u"")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(290, 50, 161, 50))
        self.frame_7.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(60, 20, 50, 15))
        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 12, 31, 31))
        self.pushButton_5.setStyleSheet(u"")
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(120, 12, 31, 31))
        self.pushButton_6.setStyleSheet(u"")

        self.retranslateUi(DiodSettings)

        QMetaObject.connectSlotsByName(DiodSettings)
    # setupUi

    def retranslateUi(self, DiodSettings):
        DiodSettings.setWindowTitle(QCoreApplication.translate("DiodSettings", u"DiodSettings", None))
        self.nmLabel.setText("")
        self.CWRadioButton.setText(QCoreApplication.translate("DiodSettings", u"CW", None))
        self.SingleRadioButton.setText(QCoreApplication.translate("DiodSettings", u"Single", None))
        self.RepeatRadioButton.setText(QCoreApplication.translate("DiodSettings", u"Repeat", None))
        self.EnableButton.setText(QCoreApplication.translate("DiodSettings", u"Enable/Disable", None))
        self.PowerLabel.setText(QCoreApplication.translate("DiodSettings", u"0.0 Watt", None))
        self.IncrementPowerButton.setText(QCoreApplication.translate("DiodSettings", u"^", None))
        self.DecrementPowerButton.setText(QCoreApplication.translate("DiodSettings", u"v", None))
        self.label_3.setText(QCoreApplication.translate("DiodSettings", u"Energy:", None))
        self.label_4.setText(QCoreApplication.translate("DiodSettings", u"Count:", None))
        self.label_5.setText(QCoreApplication.translate("DiodSettings", u"0           J", None))
        self.label_6.setText(QCoreApplication.translate("DiodSettings", u"0", None))
        self.label_16.setText(QCoreApplication.translate("DiodSettings", u"NUMBER", None))
        self.pushButton.setText(QCoreApplication.translate("DiodSettings", u"^", None))
        self.pushButton_4.setText(QCoreApplication.translate("DiodSettings", u"v", None))
        self.label_14.setText(QCoreApplication.translate("DiodSettings", u"T on", None))
        self.label_15.setText(QCoreApplication.translate("DiodSettings", u"ms", None))
        self.label_17.setText(QCoreApplication.translate("DiodSettings", u"T on", None))
        self.label_18.setText(QCoreApplication.translate("DiodSettings", u"ms", None))
        self.label_19.setText(QCoreApplication.translate("DiodSettings", u"NUMBER", None))
        self.pushButton_5.setText(QCoreApplication.translate("DiodSettings", u"^", None))
        self.pushButton_6.setText(QCoreApplication.translate("DiodSettings", u"v", None))
    # retranslateUi

