# -*- coding: utf-8 -*-

#PyQt5 standard import
import sys 	
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import re
from overide_fun import *
from functools import partial
import os
#qt source file
import picture_rc
#user defined file
from gui import *
from content_image import *
from style_image import *
from setting import *
from current_setting import *
from solve_dialog import *
from arguments import args
from neural_style import *
import scipy.optimize.lbfgsb as lbfgs
class MyMainWindow(QMainWindow, Ui_MainWindow):
    #self defined signal
    label_clicked = pyqtSignal(QLabel)
    label_2clicked = pyqtSignal(QLabel)
    label_3clicked = pyqtSignal(QLabel)
    label_4clicked = pyqtSignal(QLabel)
    label_released = pyqtSignal(QLabel)
    label_2released = pyqtSignal(QLabel)
    label_3released = pyqtSignal(QLabel)
    label_4released = pyqtSignal(QLabel)
    finished = pyqtSignal()
    sizeChanged = pyqtSignal()

    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.args = args
        self.results = ""
        self.scene = QGraphicsScene()
        self.settingWin = SettingWindow()
        self.currentsetWin = Current_settingWin()
        self.solve_dialog = SolveDialog(self)
        self.cal_thread = CalThread()
        #signals connect to slots
        self.sizeChanged.connect(self.update_image)

        self.lineEdit.editingFinished.connect(self.content_image)
        self.lineEdit_2.editingFinished.connect(self.style_image)
        self.lineEdit.clicked.connect(self.show_contentimg)
        self.lineEdit_2.clicked.connect(self.show_styimg_)

        self.actioncurrent_settings.triggered.connect(self.current_settings)
        self.actionsave.triggered.connect(self.save_results)
        self.pushButton.clicked.connect(lambda:self.openfile('--style_image'))
        self.pushButton_2.clicked.connect(lambda:self.openfile('--content_image'))

        self.pushButton_3.clicked.connect(self.start)
        self.pushButton_3.clicked.connect(self.animation)
        self.pushButton_3.clicked.connect(self.subsolvedialog)

        self.cal_thread.finished.connect(self.complete)
        # self.solve_dialog.stop.connect(self.stop_thread)
        # self.solve_dialog.pushButton_2.clicked.connect(self.show_image)
        # self.solve_dialog.pushButton.clicked.connect(self.stop_thread)

        self.pushButton_4.clicked.connect(self.show_styimg)

        self.label_clicked.connect(self.renderlabel)
        self.label_released.connect(self.renderlabel_)
        self.label_2clicked.connect(self.renderlabel)
        self.label_2released.connect(self.renderlabel_)
        self.label_3clicked.connect(self.renderlabel)
        self.label_3released.connect(self.renderlabel_)
        self.label_4clicked.connect(self.renderlabel)
        self.label_4released.connect(self.renderlabel_)

        self.label.installEventFilter(self)
        self.label_2.installEventFilter(self)
        self.label_3.installEventFilter(self)
        self.label_4.installEventFilter(self)

        self.pushButton_8.clicked.connect(self.subconwin)
        self.pushButton_9.clicked.connect(self.substywin)

        self.settingWin.close()
        #menu window
        self.actionparameters.triggered.connect(self.subsettingwin)
        self.actioncurrent_settings.triggered.connect(self.subcurrentsetwin)

        #setting signal conntect to slots
        self.settingWin.horizontalSlider.valueChanged.connect(partial(self.set_args,key = '--content_weight'))
        self.settingWin.horizontalSlider_3.valueChanged.connect(partial(self.set_args,key = '--style_weight'))
        self.settingWin.treeWidget_2.itemChanged.connect(partial(self.set_args,key = '--style_imgs_weights'))
        self.settingWin.tableWidget.itemChanged.connect(partial(self.set_args,key = '--style_layer_weights'))
        self.settingWin.tableWidget_3.itemChanged.connect(partial(self.set_args,key = '--content_layer_weights'))
        self.settingWin.radioButton.clicked.connect(partial(self.set_args,key = '--original_colors',transcolor = False))
        self.settingWin.radioButton_2.clicked.connect(partial(self.set_args,key = '--original_colors',transcolor=True))
        self.settingWin.radioButton_3.clicked.connect(partial(self.set_args,key = '--device',device = '/gpu:0'))
        self.settingWin.radioButton_4.clicked.connect(partial(self.set_args, key='--device', device='/cpu:0'))
        self.settingWin.doubleSpinBox_2.valueChanged.connect(partial(self.set_args,key = '--learning_rate'))
        self.settingWin.spinBox.valueChanged.connect(partial(self.set_args,key = '--max_iterations'))
        self.settingWin.comboBox_4.currentIndexChanged.connect(partial(self.set_args,key = '--color_convert_type'))
        self.settingWin.comboBox.currentIndexChanged.connect(partial(self.set_args, key='--pooling_type'))
        self.settingWin.comboBox_2.currentIndexChanged.connect(partial(self.set_args, key='--optimizer'))
        self.settingWin.comboBox_3.currentIndexChanged.connect(partial(self.set_args, key='--content_loss_function'))
        self.settingWin.spinBox_2.valueChanged.connect(partial(self.set_args,key = '--max_size'))



    def event(self, event):
        if event.type()==QEvent.Resize:
            self.sizeChanged.emit()
        return QMainWindow.event(self, event)
    #slots
    def update_image(self):
        if self.results !='':
            self.show_image(self.results)
    def start(self):
        self.results = ''
        lbfgs.loss_fun = []
        parameters = ''
        for key in self.args:
            key_=key
            value = self.args[key]
            if key =='--content_image':
                key_ = '--content_img'
            if key == '--style_image':
                key_ = '--style_imgs'
            if type(value)==list:
                string = ''
                for i in value:
                    string += str(i)+' '
                value = string
            parameters+= key_+' '+str(value)+' '
        # args = parse_args(parameters)
        self.cal_thread.parameters = parameters
        self.cal_thread.original_color = self.args['--original_colors']
        self.cal_thread.start()
    def complete(self,fname):
        self.solve_dialog.pushButton_2.setEnabled(True)
        self.solve_dialog.pushButton.setEnabled(False)
        self.results = fname
        if self.results !='':
            self.show_image(fname)
        else:
            self.show_contentimg()
    def current_settings(self):
        pass
    def save_results(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save results', 'C:\\', "Images(*.png);;Images(*.ppm);;Images(*.jpg);;Images(*pgm)")
        if fname!='' and self.results!='':
            QFile.copy(self.results,fname)
            # QFile.remove(self.results)
        else:
            pass
    def show_contentimg(self):

        try:
            self.pushButton_4.setMaximumSize(QtCore.QSize(0, 0))
            self.show_image(self.args['--content_image'])
        except:
            pass
    def show_styimg_(self):

        string = self.lineEdit_2.text()
        if string != '' and len(string.split(';')) > 1:
            self.pushButton_4.setMaximumSize(QtCore.QSize(20, 100))
            self.show_styimg()
        else:
            try:
                self.show_image(self.args['--style_image'])
            except:
                pass
    def content_image(self):
        string = self.lineEdit.text()
        if string != self.args['--content_image'] and string!='':
            self.args['--content_image']=string
            self.lineEdit.setText(string)
            print(args)
    def style_image(self):
        string = self.lineEdit_2.text()
        if string != self.args['--style_image'] and string!='' and len(string.split(';'))<=1:
            self.args['--style_image']=string
            self.lineEdit_2.setText(string)
    def openfile(self,str):
        fname,_ = QFileDialog.getOpenFileName(self,'Open File','C:\\',"Images(*.png *.ppm *.jpg *pgm)")
        if fname != '':
            self.args[str] = fname
            if str =='--style_image':
                self.lineEdit_2.setText(fname)
            if str =='--content_image':
                self.lineEdit.setText(fname)
            print(args)
            picture = QPixmap(fname)
            if self.graphicsView.height()/picture.height()*picture.width()>self.graphicsView.width():
                picture = picture.scaled(self.graphicsView.width(),self.graphicsView.width()/picture.width()*picture.height())
            else:
                picture=picture.scaled(self.graphicsView.height()/picture.height()*picture.width(),self.graphicsView.height())
            self.scene = QGraphicsScene()
            self.scene.clear()
            self.scene.setBackgroundBrush(Qt.white)
            self.scene.addPixmap(picture)
            #self.graphicsView.centerOn(self.graphicsView.width() / 2, self.graphicsView.height() / 2)
            self.graphicsView.setScene(self.scene)
            self.graphicsView.show()
    def show_image(self,fname):

        picture = QPixmap(fname)
        if self.graphicsView.height() / picture.height() * picture.width() > self.graphicsView.width():
            picture = picture.scaled(self.graphicsView.width(),
                                     self.graphicsView.width() / picture.width() * picture.height())
        else:
            picture = picture.scaled(self.graphicsView.height() / picture.height() * picture.width(),
                                     self.graphicsView.height())
        self.scene = QGraphicsScene()
        self.scene.clear()
        self.scene.setBackgroundBrush(Qt.white)
        self.scene.addPixmap(picture)
        # self.graphicsView.centerOn(self.graphicsView.width() / 2, self.graphicsView.height() / 2)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
    def show_multiimg(self,styimg_list):
        if len(styimg_list)==0:
            pass# self.pushButton_4.setMaximumSize(QtCore.QSize(0, 0))
        else:
            if len(styimg_list)==1:
                self.pushButton_4.setMaximumSize(QtCore.QSize(0, 0))
                self.show_image(styimg_list[0])
                self.args["--style_image"] = styimg_list[0]
                self.lineEdit_2.setText(styimg_list[0])
            else:
                self.pushButton_4.setMaximumSize(QtCore.QSize(20, 100))
                strs = ''
                str_=''
                self.settingWin.treeWidget_2.topLevelItem(0).takeChildren()
                i = 0
                for fname in styimg_list:

                    strs+=fname+' '
                    str_+=fname+';'
                    self.settingWin.treeWidget_2.topLevelItem(0).addChild(QTreeWidgetItem([fname, str(1/len(styimg_list))]))
                    self.settingWin.treeWidget_2.topLevelItem(0).child(i).setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    i+=1
                self.args["--style_image"]=strs
                self.args['--style_imgs_weights']=[1/len(styimg_list) for _ in range(len(styimg_list))]
                self.lineEdit_2.setText(str_)
                self.style_list = styimg_list
                self.i = 0
                self.show_styimg()
    def show_styimg(self):
        self.scene = QGraphicsScene()
        self.scene.clear()
        self.scene.setBackgroundBrush(Qt.white)
        if self.i>=len(self.style_list):
            self.i = 0
        fname = self.style_list[self.i]
        self.i+=1
        label = QLabel()
        picture = QPixmap(fname)
        if self.graphicsView.height() / picture.height() * picture.width() > self.graphicsView.width():
            picture = picture.scaled(self.graphicsView.width(),
                                     self.graphicsView.width() / picture.width() * picture.height())
        else:
            picture = picture.scaled(self.graphicsView.height() / picture.height() * picture.width(),
                                     self.graphicsView.height())
        label.setPixmap(picture)
        self.scene.addWidget(label)
            # self.scene.addItem(picture)
        # self.graphicsView.centerOn(self.graphicsView.width() / 2, self.graphicsView.height() / 2)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
    def animation(self):
        self.scene_1 = QGraphicsScene()
        self.scene_1.setBackgroundBrush(QColor(0, 0, 0, 160))
        gif_anim = QLabel()
        gif_anim.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        movie = QMovie('icon\\adding_style.gif')
        gif_anim.setMovie(movie)
        movie.start()
        self.scene_1.addWidget(gif_anim)
        self.graphicsView.setScene(self.scene_1)
        self.graphicsView.show()
    def renderlabel(self,label):
        if label == self.label:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/3.jpeg);\n"
"margin:4px;")

        if label == self.label_2:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/oily_mcoilface.jpg);\n"
"margin:4px;")
        if label == self.label_3:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/lion.jpg);\n"
"margin:4px;")
        if label == self.label_4:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/oil_crop.jpg);\n"
"margin:4px;")
    def renderlabel_(self,label):
        if label == self.label:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/3.jpeg);\n"
                                "margin:0px;")
            self.show_image('content_image/3.jpeg')
            # path = os.path.join('','content_image/3.jpeg')
            path = os.path.abspath('content_image/3.jpeg')
            self.args['--content_image']=path
            self.lineEdit.setText(path)
        if label == self.label_2:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/oily_mcoilface.jpg);\n"
                                "margin:0px;")
            self.show_image('style_image\\oily_mcoilface.jpg')
            path = os.path.abspath('style_image\\oily_mcoilface.jpg')
            self.args['--style_image']=path
            self.settingWin.treeWidget_2.topLevelItem(0).takeChildren()
            self.args['--style_imgs_weights'] = [1.0]
            self.lineEdit_2.setText(path)
        if label == self.label_3:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/lion.jpg);\n"
                                "margin:0px;")
            self.show_image('content_image\\lion.jpg')
            path = os.path.abspath('content_image\\lion.jpg')
            self.args['--content_image'] =path
            self.lineEdit.setText(path)
        if label == self.label_4:
            label.setStyleSheet("border-image: url(:/backgroundpicture/background/oil_crop.jpg);\n"
                                "margin:0px;")
            self.show_image('style_image\\oil_crop.jpg')
            path = os.path.abspath('style_image\\oil_crop.jpg')
            self.args['--style_image'] = path
            self.settingWin.treeWidget_2.topLevelItem(0).takeChildren()
            self.args['--style_imgs_weights'] = [1.0]
            self.lineEdit_2.setText(path)
    def eventFilter(self, watched, event):
        if watched == self.label:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.label_clicked.emit(self.label)
            if event.type() == QEvent.MouseButtonRelease:
                self.label_released.emit(self.label)
        if watched == self.label_2:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.label_2clicked.emit(self.label_2)
            if event.type() == QEvent.MouseButtonRelease:
                self.label_2released.emit(self.label_2)
        if watched == self.label_3:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.label_3clicked.emit(self.label_3)
            if event.type() == QEvent.MouseButtonRelease:
                self.label_3released.emit(self.label_3)
        if watched == self.label_4:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.label_4clicked.emit(self.label_4)
            if event.type() == QEvent.MouseButtonRelease:
                self.label_4released.emit(self.label_4)
        return QMainWindow.eventFilter(self, watched, event)
    def subconwin(self):
        self.conWin = MyConWindow(self)
        self.conWin.exec_()
        if self.conWin.content_img!= None and self.conWin.statuts == True:
            path = os.path.abspath(self.conWin.content_img)
            self.args['--content_image']=path
            self.show_image(self.conWin.content_img)
            self.lineEdit.setText(path)
    def substywin(self):
        self.styWin = MyStyWindow(self)
        self.styWin.exec_()
        if self.styWin.statuts == True:
            self.show_multiimg(self.styWin.style_img_list)
    def subsettingwin(self):
        self.settingWin.show()
    def subcurrentsetwin(self):

        settings = 'current settings:\n'
        for keys in self.args.keys():
            settings +=keys+': '+str(self.args[keys])+'\n'
        self.currentsetWin.textBrowser.setText(settings)
        self.currentsetWin.show()
    def subsolvedialog(self):
        self.solve_dialog = SolveDialog(self)
        if self.args['--optimizer']=='lbfgs':

            self.solve_dialog.widget.mpl.solver= 'lbfgs'
        else:
            self.solve_dialog.widget.mpl.solver = 'adam'
        # self.solve_dialog.widget.initUi(solver)
        self.solve_dialog.pushButton_2.setEnabled(False)
        self.solve_dialog.exec_()
        print('stopping thread')
        self.cal_thread.terminate()
        self.cal_thread.wait()
        if self.results == '':
            self.show_contentimg()

    def set_args(self,*args,**kwargs):
        value = ''
        if kwargs['key'] == '--content_weight':
            value = args[0]
        if kwargs['key'] =='--style_weight':
            value = args[0]
        if kwargs['key'] =='--style_imgs_weights':
            if args[1]==1:
                qwidgetitem = args[0]
                colume = args[1]
                index_=self.args['--style_image'].strip(' ').split(' ').index(qwidgetitem.text(0))
                self.args['--style_imgs_weights'][index_]=float((qwidgetitem.text(colume)))
                value = self.args['--style_imgs_weights']
        if kwargs['key'] == '--style_layer_weights':
            for i in range(len(self.args['--style_layer_weights'])):
                self.args['--style_layer_weights'][i]=float(self.settingWin.tableWidget.item(0,i).text())
            value =  self.args['--style_layer_weights']
        if kwargs['key'] =='--content_layer_weights':
            for i in range(len(self.args['--content_layer_weights'])):
                self.args['--content_layer_weights'][i] = float(self.settingWin.tableWidget_3.item(0,i).text())
            value = self.args['--content_layer_weights']
        if kwargs['key'] == '--original_colors':
            value = kwargs['transcolor']
        if kwargs['key'] == '--color_convert_type':
            index_=args[0]
            types = ['yuv', 'ycrcb', 'lab','luv']
            value = types[index_]
        if kwargs['key'] =='--pooling_type':
            if args[0]==0:
                value = 'avg'
            if args[0]==1:
                value = 'max'
        if kwargs['key'] =='--device':
            value = kwargs['device']
        if kwargs['key'] =='--optimizer':
            ['lbfgs', 'adam']
            if args[0]==0:
                value = 'lbfgs'
            if args[0]==1:
                value = 'adam'
        if kwargs['key'] =='--learning_rate':
            value = args[0]
        if kwargs['key'] =='--max_iterations':
            value = args[0]
        if kwargs['key']=='--max_size':
            value = args[0]
        if kwargs['key'] =='--content_loss_function':
            if args[0]==0:
                value = 1
            if args[0]==1:
                value =2
            if args[0]==2:
                value = 3
        self.args[kwargs['key']] = value
class CalThread(QThread):
    finished = pyqtSignal(str)
    def __init__(self):
        super(CalThread,self).__init__()
        self.parameters = None
        self.original_color = False
    def run(self):
        result = ''
        # result = compute()
        result = start_cal(self.parameters,self.original_color)
        self.finished.emit(result)
class MyConWindow(QDialog,Ui_ConImg):
    subwin_label_clicked = pyqtSignal(QLabel)
    def __init__(self, parent=None):
        super(MyConWindow, self).__init__(parent)
        self.setupUi(self)
        self.old_label = self.label_3
        self.old_str = self.label_3.styleSheet()
        self.subwin_label_clicked.connect(self.select_image)
        self.content_img = None
        self.statuts = False

        self.pushButton_2.clicked.connect(self.ok_clicked)

        self.label_3.installEventFilter(self)
        self.label_7.installEventFilter(self)
        self.label_8.installEventFilter(self)
        self.label_9.installEventFilter(self)
        self.label.installEventFilter(self)
        self.label_11.installEventFilter(self)
        self.label_13.installEventFilter(self)

    def eventFilter(self, watched, event):
        if type(watched) == QLabel:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.subwin_label_clicked.emit(watched)
            # if event.type() == QEvent.MouseButtonRelease:
            #     self.label_released.emit(self.label)
        return QDialog.eventFilter(self, watched, event)
    def select_image(self,label):
        if label.text()=='':
            self.old_label.setStyleSheet(self.old_str)
            self.old_label = label
            self.old_str = label.styleSheet()
            new_str=self.old_str+"QLabel{border:2px solid;border-color:\"blue\"}"
            label.setStyleSheet(new_str)
            self.content_img=re.findall(r"content_image/.*png|content_image/.*ppm|content_image/.*jpg|content_image/.*pgm|content_image/.*jpeg", new_str)[0]
    def ok_clicked(self):
        self.statuts = True
class MyStyWindow(QDialog,Ui_StyleImg):
    subwin_label_clicked = pyqtSignal(QLabel)
    def __init__(self, parent=None):
        super(MyStyWindow, self).__init__(parent)
        self.setupUi(self)
        self.style_img_num = 0
        self.style_img_list = []
        self.old_label = self.label_3
        self.old_str = self.label_3.styleSheet()
        self.fname = self.subwin_label_clicked.connect(self.select_image)
        self.pushButton_2.clicked.connect(self.ok_clicked)
        self.statuts = False

        self.label_3.installEventFilter(self)
        self.label_7.installEventFilter(self)
        self.label_8.installEventFilter(self)
        self.label_9.installEventFilter(self)
        self.label.installEventFilter(self)
        self.label_11.installEventFilter(self)
        self.label_13.installEventFilter(self)
        self.label_14.installEventFilter(self)
        self.label_15.installEventFilter(self)
        self.label_19.installEventFilter(self)
        self.label_20.installEventFilter(self)
    def eventFilter(self, watched, event):
        if type(watched) == QLabel:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.subwin_label_clicked.emit(watched)
            # if event.type() == QEvent.MouseButtonRelease:
            #     self.label_released.emit(self.label)
        return QDialog.eventFilter(self, watched, event)
    def select_image(self, label):

        if label.text() == '':
            if re.search(r'QLabel{border:',label.styleSheet()):
                #print(label.styleSheet())
                self.style_img_list.remove(os.path.abspath(re.findall(r'style_image/.*png|style_image/.*ppm|style_image/.*jpg|style_image/.*pgm',label.styleSheet())[0]))
                self.style_img_num -= 1
                label.setStyleSheet(re.sub(r"QLabel{border:2px solid;border-color:\"blue\"}",'',label.styleSheet()))

            else:

                if self.style_img_num>=4:
                    pass
                else:
                    self.style_img_num += 1
                    r = re.findall(r"style_image/.*png|style_image/.*ppm|style_image/.*jpg|style_image/.*pgm",label.styleSheet())[0]

                    self.style_img_list.append(os.path.abspath(r))
                    new_str = label.styleSheet() + "QLabel{border:2px solid;border-color:\"blue\"}"
                    label.setStyleSheet(new_str)
    def ok_clicked(self):
        self.statuts = True
class SettingWindow(QWidget,Ui_setting):
    def __init__(self, parent=None):
        super(SettingWindow, self).__init__(parent)
        self.setupUi(self)
        self.settings = ''
        self.horizontalSlider.valueChanged.connect(self.doubleSpinBox.setValue)
        self.doubleSpinBox.valueChanged.connect(self.horizontalSlider.setValue)
        self.horizontalSlider_3.valueChanged.connect(self.doubleSpinBox_3.setValue)
        self.doubleSpinBox_3.valueChanged.connect(self.horizontalSlider_3.setValue)
class SolveDialog(QDialog,Ui_Dialog):

    def __init__(self, parent=None):
        super(SolveDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.stop_computing)
        self.pushButton_2.clicked.connect(self.finish_computing)
    def stop_computing(self):

        self.close()
    def finish_computing(self):
        self.close()

class Current_settingWin(QWidget,Ui_current_setting):
    def __init__(self, parent=None):
        super(Current_settingWin, self).__init__(parent)
        self.setupUi(self)
if __name__=="__main__":  
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
