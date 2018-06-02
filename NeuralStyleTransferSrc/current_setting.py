# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'current_setting.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_current_setting(object):
    def setupUi(self, current_setting):
        current_setting.setObjectName("current_setting")
        current_setting.resize(526, 500)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(current_setting)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(current_setting)
        self.textBrowser.setStyleSheet("border:1px solid;\n"
"border-radius:20px;\n"
"border-width:1px;\n"
"border-color: rgb(28, 162, 97);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Bell MT\";")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(current_setting)
        QtCore.QMetaObject.connectSlotsByName(current_setting)

    def retranslateUi(self, current_setting):
        _translate = QtCore.QCoreApplication.translate
        current_setting.setWindowTitle(_translate("current_setting", "Form"))

