# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from overide_fun import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(804, 669)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("border-color: rgba(255, 255, 255, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 90))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 120))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"\n"
"border-image: url(:/backgroundpicture/background/1.jpg);")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_3.setStyleSheet("border-style: none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Arial Rounded MT Bold\";")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(95, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{border-style:outside;\n"
"border:2px solid;\n"
"border-radius:5px;\n"
"border-width:2px;\n"
"font:12px;\n"
"border-color:beige;\n"
"background-color: rgb(216, 221, 217);}\n"
"QPushButton:pressed {\n"
"    margin:2px;\n"
"\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(540, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = self_QlineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lineEdit_2.setStyleSheet("text-align: right;\n"
"color: rgb(144, 144, 144);\n"
"font-size:20px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 0, 190);\n"
"font: 75 9pt \"Arial Narrow\";\n"
"font-weight:600;\n"
"color:\"white\";\n"
"border:1px solid;\n"
"border-color:rgb(80,0,190);\n"
"}\n"
"QPushButton:hover{background-color:\"white\" ;color:\"black\";border-color:rgb(80,0,190)}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.lineEdit = self_QlineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        self.lineEdit.setStyleSheet("text-align: right;\n"
"color: rgb(144, 144, 144);\n"
"font-size:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 40))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(1, 1))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(80, 0, 190);\n"
"font: 75 9pt \"Arial Narrow\";\n"
"font-weight:600;\n"
"color:\"white\";\n"
"border:1px solid;\n"
"border-color:rgb(80,0,190);\n"
"}\n"
"QPushButton:hover{background-color:\"white\" ;color:\"black\";border-color:rgb(80,0,190)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton\n"
"{\n"
"border-style: none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(80, 0, 190);\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton\n"
"{\n"
"border-style: none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(80, 0, 190);\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration:underline;}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("\n"
"QLabel{\n"
"border-image: url(:/backgroundpicture/background/3.jpeg);\n"
"\n"
"}\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("QLabel{\n"
"border-image: url(:/style/style_image/oily_mcoilface.jpg);}\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("QLabel{\n"
"border-image: url(:/content/content_image/lion.jpg);}\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"border-image: url(:/style/style_image/oil_crop.jpg);}\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 12)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(300, 300))
        self.graphicsView.setMaximumSize(QtCore.QSize(2000, 2000))
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.graphicsView.setStyleSheet("border-image: url(:/backgroundpicture/background/42_output.png);\n"
"font: 87 20pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(:/button/icon/resizeApi.png);}\n"
"QPushButton:pressed{\n"
"    margin:2px;}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setStyleSheet("border:None;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 16)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 23))
        self.menubar.setObjectName("menubar")
        self.menusetings = QtWidgets.QMenu(self.menubar)
        self.menusetings.setObjectName("menusetings")
        MainWindow.setMenuBar(self.menubar)
        self.actionparameters = QtWidgets.QAction(MainWindow)
        self.actionparameters.setObjectName("actionparameters")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actioncurrent_settings = QtWidgets.QAction(MainWindow)
        self.actioncurrent_settings.setObjectName("actioncurrent_settings")
        self.menusetings.addAction(self.actionparameters)
        self.menusetings.addAction(self.actioncurrent_settings)
        self.menusetings.addAction(self.actionsave)
        self.menubar.addAction(self.menusetings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.graphicsView)
        MainWindow.setTabOrder(self.graphicsView, self.textBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deep Style Transfer"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Matura MT Script Capitals\'; font-size:36pt; color:#ffffff;\">Deep Style Transfer</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial Rounded MT Bold\'; font-size:12pt; font-weight:600; color:#ffffff;\">Using deep learning for artistic style transfer</span></p></body></html>"))
        self.lineEdit_3.setText(_translate("MainWindow", "Try Deep Style Transfer:"))
        self.pushButton_3.setText(_translate("MainWindow", "start transfer"))
        self.pushButton.setText(_translate("MainWindow", "STYLE IMAGE"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "https://unsplash.com/image.jpg"))
        self.pushButton_2.setText(_translate("MainWindow", "CONTENT IMAGE"))
        self.pushButton_8.setText(_translate("MainWindow", "More content images..."))
        self.pushButton_9.setText(_translate("MainWindow", "More style images..."))
        self.lineEdit_4.setText(_translate("MainWindow", "For more detail you can visit:https://github.com/vonlippmann/Neural-style-transfer-application"))
        self.menusetings.setTitle(_translate("MainWindow", "Setting"))
        self.actionparameters.setText(_translate("MainWindow", "parameters"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actioncurrent_settings.setText(_translate("MainWindow", "current settings"))

import picture_rc
