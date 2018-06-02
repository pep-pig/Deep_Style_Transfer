# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'content_image.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConImg(object):
    def setupUi(self, ConImg):
        ConImg.setObjectName("ConImg")
        ConImg.resize(663, 561)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ConImg)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(ConImg)
        self.label_8.setStyleSheet("QLabel{;\n"
"image: url(:/content/content_image/taj_mahal.jpg);\n"
"border:1px solid;\n"
"    border-color: rgba(255, 255, 255,0);\n"
"}\n"
"QLabel:hover{border:2px solid;\n"
"border-color:\"blue\"}")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(ConImg)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(ConImg)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9 = QtWidgets.QLabel(ConImg)
        self.label_9.setStyleSheet("QLabel{;\n"
"    image: url(:/content/content_image/tubingen.jpg);\n"
"border:1px solid;\n"
"    border-color: rgba(255, 255, 255,0);\n"
"}\n"
"QLabel:hover{border:2px solid;\n"
"border-color:\"blue\"}")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(ConImg)
        self.label_7.setStyleSheet("QLabel{;\n"
"image: url(:/content/content_image/new_york.png);\n"
"border:1px solid;\n"
"    border-color: rgba(255, 255, 255,0);\n"
"}\n"
"QLabel:hover{border:2px solid;\n"
"border-color:\"blue\"}")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(ConImg)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(ConImg)
        self.label_3.setStyleSheet("QLabel{;\n"
"image: url(:/content/content_image/garden.png);\n"
"border:1px solid;\n"
"    border-color: rgba(255, 255, 255,0);\n"
"}\n"
"QLabel:hover{border:2px solid;\n"
"border-color:\"blue\"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(ConImg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(200, 50))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label = QtWidgets.QLabel(ConImg)
        self.label.setStyleSheet("QLabel{image: url(:/content/content_image/3.jpeg);\n"
"border:1px solid;\n"
"    border-color: rgba(255, 255, 255,0);\n"
"}\n"
"QLabel:hover{border:2px solid;\n"
"border-color:\"blue\"}")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(ConImg)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11 = QtWidgets.QLabel(ConImg)
        self.label_11.setStyleSheet("QLabel{\n"
"    image: url(:/content/content_image/04.jpeg);\n"
"border:1px solid;\n"
"    border-color: rgba(255, 255, 255,0);\n"
"}\n"
"QLabel:hover{border:2px solid;\n"
"border-color:\"blue\"}")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(ConImg)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13 = QtWidgets.QLabel(ConImg)
        self.label_13.setStyleSheet("QLabel{\n"
"    image: url(:/content/content_image/lion.jpg);\n"
"border:1px solid;\n"
"    border-color: rgba(255, 255, 255,0);\n"
"}\n"
"QLabel:hover{border:2px solid;\n"
"border-color:\"blue\"}")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(ConImg)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_2.setRowStretch(0, 10)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 10)
        self.gridLayout_2.setRowStretch(3, 2)
        self.gridLayout_2.setRowStretch(4, 10)
        self.gridLayout_2.setRowStretch(5, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(ConImg)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(ConImg)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ConImg)
        self.pushButton_2.clicked.connect(ConImg.accept)
        self.pushButton.clicked.connect(ConImg.reject)
        QtCore.QMetaObject.connectSlotsByName(ConImg)

    def retranslateUi(self, ConImg):
        _translate = QtCore.QCoreApplication.translate
        ConImg.setWindowTitle(_translate("ConImg", "Dialog"))
        self.label_10.setText(_translate("ConImg", "tubingen"))
        self.label_4.setText(_translate("ConImg", "Garden"))
        self.label_2.setText(_translate("ConImg", "rhinoceros"))
        self.label_6.setText(_translate("ConImg", "taj_mahal"))
        self.label_5.setText(_translate("ConImg", "NewYork"))
        self.label_12.setText(_translate("ConImg", "car"))
        self.label_16.setText(_translate("ConImg", "lions"))
        self.pushButton_2.setText(_translate("ConImg", "OK"))
        self.pushButton.setText(_translate("ConImg", "CANCEL"))

import picture_rc
