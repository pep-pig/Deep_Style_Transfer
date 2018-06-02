from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class self_QlineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        super(self_QlineEdit, self).__init__(parent)
    def event(self, event):
        if event.type() == QEvent.MouseButtonPress:
            mouseEvent = QMouseEvent(event)
            if mouseEvent.buttons() == Qt.LeftButton:
                self.clicked.emit()
        return QtWidgets.QLineEdit.event(self,event)