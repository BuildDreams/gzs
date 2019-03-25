# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

ALL_FILES = []  # 所有文件配置
LEFT_FILES = []  # 左表文件
RIGHT_FILES = []  # 右表文件
To_A = 1  # 合并方向参数

import sys
import os
import base64


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QAction, QMenu, QButtonGroup, QMessageBox, \
    QInputDialog, QProgressBar, QLineEdit, QLCDNumber, QDateTimeEdit, QSystemTrayIcon
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QPixmap, QIcon



from show_sheetname import main, jion_left_right, cols_name
from pdf_word import parser_pdfs
from pics import icons


def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()
    return image


icon = get_pic(icons, 'mg.ico')


class Ui_Dialog(QWidget):

    def setupUi(self, Dialog):
        """
        窗体UI控件部分
        :param Dialog: 主窗体
        :return: None
        """

        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 950)
        Dialog.setWindowOpacity(0.95)  # 设置
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1200, 950))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab1")

        self.tabWidget.setCurrentIndex(1)
        # self.tabWidget.showNormal()

        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")

        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab2, "")
        self.tabWidget.setDocumentMode(True)
        self.setAcceptDrops(True)

        self.cwd = os.getcwd()
        self.index = ''

        self.y_outer = QtWidgets.QRadioButton(self.tab)
        self.y_outer.setGeometry(QtCore.QRect(200, 270, 89, 16))
        self.y_outer.setObjectName("y_outer")

        self.y_inner = QtWidgets.QRadioButton(self.tab)
        self.y_inner.setGeometry(QtCore.QRect(200, 300, 89, 16))
        self.y_inner.setObjectName("y_inner")

        self.x_left = QtWidgets.QRadioButton(self.tab)
        self.x_left.setGeometry(QtCore.QRect(200, 560, 89, 16))
        self.x_left.setObjectName("x_left")

        self.x_inner = QtWidgets.QRadioButton(self.tab)
        self.x_inner.setGeometry(QtCore.QRect(200, 530, 89, 16))
        self.x_inner.setObjectName("x_inner")

        self.x_outer = QtWidgets.QRadioButton(self.tab)
        self.x_outer.setGeometry(QtCore.QRect(200, 490, 89, 16))
        self.x_outer.setObjectName("x_outer")
        #
        self.x_right = QtWidgets.QRadioButton(self.tab)
        self.x_right.setGeometry(QtCore.QRect(200, 590, 89, 16))
        self.x_right.setObjectName("x_right")

        self.y_text = QtWidgets.QTextBrowser(self.tab)
        self.y_text.setGeometry(QtCore.QRect(330, 200, 711, 161))
        self.y_text.setObjectName("y_text")

        self.down_left_text = QtWidgets.QTextBrowser(self.tab)
        self.down_left_text.setGeometry(QtCore.QRect(330, 460, 330, 171))
        self.down_left_text.setObjectName("down_left_text")

        self.down_right_text = QtWidgets.QTextBrowser(self.tab)
        self.down_right_text.setGeometry(QtCore.QRect(710, 460, 330, 171))
        self.down_right_text.setObjectName("down_right_text")

        self.y_jions = QtWidgets.QPushButton(self.tab)
        self.y_jions.setGeometry(QtCore.QRect(40, 270, 130, 40))
        self.y_jions.setObjectName("y_jions")

        self.x_jions = QtWidgets.QPushButton(self.tab)
        self.x_jions.setGeometry(QtCore.QRect(40, 530, 130, 40))
        self.x_jions.setObjectName("x_jions")

        self.files_up = QtWidgets.QPushButton(self.tab)
        self.files_up.setGeometry(QtCore.QRect(560, 140, 160, 40))
        self.files_up.setObjectName("files_up")

        self.files_down_left = QtWidgets.QPushButton(self.tab)
        self.files_down_left.setGeometry(QtCore.QRect(460, 400, 130, 40))
        self.files_down_left.setObjectName("files_down")

        self.files_down_right = QtWidgets.QPushButton(self.tab)
        self.files_down_right.setGeometry(QtCore.QRect(800, 400, 130, 40))
        self.files_down_right.setObjectName("files_down")

        self.bg1 = QButtonGroup()
        self.bg1.addButton(self.y_outer, 11)
        self.bg1.addButton(self.y_inner, 21)
        #
        self.bg2 = QButtonGroup()
        self.bg2.addButton(self.x_inner, 11)
        self.bg2.addButton(self.x_left, 21)
        self.bg2.addButton(self.x_outer, 31)
        self.bg2.addButton(self.x_right, 41)

        self.msgBox = QMessageBox()

        self.files_up.clicked.connect(lambda: self.btn_chose_files(1))
        self.files_down_left.clicked.connect(lambda: self.btn_chose_files(2))
        self.files_down_right.clicked.connect(lambda: self.btn_chose_files(3))

        # 时间模块
        self.texttime = QtWidgets.QLCDNumber(self.tab)
        self.texttime.setGeometry(QtCore.QRect(0, 0, 500, 30))
        self.texttime.setMouseTracking(False)
        self.texttime.setDigitCount(19)
        self.texttime.setMode(QLCDNumber.Dec)
        self.texttime.setSegmentStyle(QLCDNumber.Flat)
        self.texttime.setObjectName("texttime")
        # pdf转换模块
        self.pdf = QtWidgets.QPushButton(self.tab2)
        self.pdf.setObjectName("btn_chooseMutiFile")
        self.pdf.setText("pdf-->word")
        self.pdf.setGeometry(QtCore.QRect(50, 100, 200, 40))

        self.pdf_show = QtWidgets.QTextBrowser(self.tab2)
        self.pdf_show.setGeometry(QtCore.QRect(330, 40, 600, 300))
        self.pdf_show.setObjectName("y_text")
        # 窗体最小化部分
        self.winIconPix = QPixmap(16, 16)
        self.setWindowIcon(QIcon('mg.ico'))
        self.tray = QSystemTrayIcon(Dialog)
        self.trayIconPix = QPixmap(16, 16)
        self.tray.setIcon(QIcon('mg.ico'))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        """
        窗体属性/样式/函数部分
        :param Dialog: 主窗体
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "tools"))
        Dialog.setWindowIcon(QIcon('mg.ico'))
        # 属性部分
        self.y_outer.setText(_translate("Dialog", "竖向"))
        self.y_inner.setText(_translate("Dialog", "横向"))
        self.y_jions.setText(_translate("Dialog", "全连接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "合并文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Dialog", "pdf转换为word"))

        self.x_left.setText(_translate("Dialog", "左连接"))
        self.x_inner.setText(_translate("Dialog", "交集"))
        self.x_outer.setText(_translate("Dialog", "全集"))
        self.x_right.setText(_translate("Dialog", "右连接"))
        self.x_jions.setText(_translate("Dialog", "横向合并"))
        self.files_up.setText(_translate("Dialog", "文件1"))
        self.files_down_left.setText(_translate("Dialog", "左表文件"))
        self.files_down_right.setText(_translate("Dialog", "右表文件"))
        # 槽函数部分
        self.y_jions.clicked.connect(lambda: Dialog.yunxing(1, ))
        self.x_jions.clicked.connect(lambda: Dialog.yunxing(2, ))

        self.pdf.clicked.connect(self.run_pdf_parse)
        self.bg1.buttonClicked.connect(self.chose_types)
        self.bg2.buttonClicked.connect(self.chose_types)
        ########################################################################################################
        # 样式部分
        self.y_jions.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')

        self.x_jions.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')

        self.files_down_left.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')

        self.files_down_right.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')

        self.files_up.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')

        self.tab.setStyleSheet("#tab1{background-color:#012456;}")
        self.tab2.setStyleSheet("#tab2{background-color:#012456;}")
        self.tabWidget.setStyleSheet(
            "QTabBar{background-color:#333300;outline:solid 2px;}QTabBar::tab{border-bottom-color:#C2C7CB;min-width: "
            "150px;border-right:2px solid black;border-style: outset;min-height: 40px;"
            "color:white;background-color:#4169E1;}QTabBar::tab:selected{background-color: white;"
            "color:green;border-top-right-radius:10px;border-top-left-radius:10px;border:none}QTabBar::tab:first{margin-left:10px;}"
            "QTabBar::tab:hover:!selected{color:red;background-color:black;}")
        self.down_right_text.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:#FF8C00;border-color:#FFF5EE;")
        self.down_left_text.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:#FF8C00;border-color:#FFF5EE;")
        self.y_text.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:#FF8C00;border-color:#FFF5EE;")
        self.pdf_show.setStyleSheet(
            "background:transparent;border-width:1;border-style:outset;color:#FF8C00;border-color:#FFF5EE;")

        self.x_inner.setStyleSheet("color:white")
        self.x_left.setStyleSheet("color:white")
        self.x_right.setStyleSheet("color:white")
        self.x_outer.setStyleSheet("color:white")
        self.y_inner.setStyleSheet("color:white")
        self.y_outer.setStyleSheet("color:white")

        self.pdf.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')

        self.texttime.setStyleSheet(
            'font: italic 1px \"楷体\";border-width:0;border-style:outset;color:#DC143C;font-size:1px;')
        ##################################################
        # 计时器模块                                       #
        #                                                #
        ##################################################
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.showtime)

        self.timer.start()

    # 选择文件模块
    def btn_chose_files(self, id):
        """

        :param id: 可视化文件路径名/(1：代表最上面文本，2：下面左边模块，3：下面右边模块)
        :return:None
        """

        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "选择文件",
                                                       self.cwd,  # 起始路径'
                                                       "Excle (*.xlsx);;")
        for file in files:  # 对于链接方式的参数配置
            if id == 1:
                self.y_text.append(file)
                ALL_FILES.append(file)
            elif id == 2:
                self.down_left_text.append(file)
                LEFT_FILES.append(file)
                global header
                header, okPressed = QInputDialog.getText(self, "字段名选择", "字段名所在行", QLineEdit.Normal, "1")
                print(header)
                try:
                    header = int(header)
                except:
                    header = 1
                if okPressed and header != '':
                    cols = cols_name(LEFT_FILES[0], int(header))
                    global left_indexs
                    left_indexs = self.getChoice(cols)

            elif id == 3:
                self.down_right_text.append(file)
                RIGHT_FILES.append(files[0])

    def getChoice(self, cols):  # Get item/choice
        """
        选择合并文件的共有字段名
        :param cols: ALL字段名
        :return: 选中的字段名
        """
        cols = [str(x) for x in cols]
        # item, okPressed = QInputDialog.getItem(self, "选择连接轴", "字段", cols, 4, True)#单选复选框，后面功能需要用到
        item, okPressed = QInputDialog.getMultiLineText(self, "删除不需要的字段", "字段名", "\n".join(cols))
        if okPressed and item:
            item = item.split()
            return item

    def chose_types(self):
        """
        选择模式模块
        :return: 选择模式。eg:横向-全集
        """
        sender = self.sender()
        global BTN_ID
        global To_A
        global AXIS_TO
        if sender == self.bg1:
            To_A = 0
            if self.bg1.checkedId() == 11:
                BTN_ID = 'outer'
                AXIS_TO = 1
            elif self.bg1.checkedId() == 21:
                AXIS_TO = 0
                BTN_ID = 'inner'
        if sender == self.bg2:
            To_A = 1
            if self.bg2.checkedId() == 11:
                BTN_ID = 'inner'
            elif self.bg2.checkedId() == 21:
                BTN_ID = 'left'
            elif self.bg2.checkedId() == 31:
                BTN_ID = 'outer'
                # self.getChoice()
            elif self.bg2.checkedId() == 41:
                BTN_ID = 'right'

    def showtime(self):
        """
        显示时间模块
        :return: None
        """
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        test = self.dateEdit.text()
        # self.texttime.setText(test)
        self.texttime.display(test)
        self.texttime.setStyleSheet(
            'font: italic 1px \"宋体\";border-width:0;border-style:outset;color:#DC143C;font-size:1px;')

    def run_pdf_parse(self):
        """
        pdf转换模块（后期优化，放进子进程模块)
        :return: 同文件名word版本.eg:文件.pdf --- 文件.doc
        """
        self.pdf_show.clear()
        files, filetype = QFileDialog.getOpenFileNames(self, "选择文件", self.cwd, "PDF Files (*.pdf);;")

        if len(files) == 0:
            return

        space = "&nbsp;&nbsp;&nbsp;&nbsp;"
        for file in files:
            texts = parser_pdfs(file)
            (filepath, tempfilename) = os.path.split(file)
            for text in texts:
                self.pdf_show.append(
                    "<font color='red' >" + "处理对象:" + tempfilename + "</font>" + "<br />" + "%s页面数:" % space + str(
                        text[0]) + "<br />" + "%s图片数:" % space + str(text[1]) + "<br />" + "%s曲线数:" % space +
                    str(text[2]) + "<br />" + "%s水平文本框:" % space + str(
                        text[3]) + "<br />" + "<font color='red' >" + "-" * 40 + "</font>")


class MyCalc(QWidget):
    """
    重写多进程逻辑
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def yunxing(self, *args):
        """
        运行函数模块，京自动调用Runthread类run函数
        :param args:
        :return:
        """
        self.myThread = Runthread(*args)
        # 6.接收信号并产生回调函数
        self.myThread.updata_date.connect(self.Display)
        self.myThread.start()

    # 7我是回调函数
    def Display(self, data):
        if data == 1:
            QMessageBox.information(self.ui, 'INFO', '合并完成', QMessageBox.Yes, QMessageBox.Yes)
        elif data == 2:
            QMessageBox.warning(self.ui, 'ERROR', '请选择文件/合并模式', QMessageBox.Yes, QMessageBox.Yes)

        self.ui.down_left_text.clear()
        self.ui.down_right_text.clear()
        self.ui.y_text.clear()

        pass


# 进程模块
class Runthread(QtCore.QThread):
    """
    多进程模块
    """
    updata_date = QtCore.pyqtSignal(int)

    def __init__(self, *args):
        super(Runthread, self).__init__()
        self.st = args

    def run(self):
        """
        将自动被调用
        :return: 具体调用函数，并且返回回调函数参数。
        """
        if self.st[0] == 1:  # 纵向合并
            try:
                indexs = ""
                print(AXIS_TO)
                main(ALL_FILES, BTN_ID, To_A,AXIS_TO, indexs=indexs)
                self.updata_date.emit(1)
            except :
                self.updata_date.emit(2)
        elif self.st[0] == 2:  # 横向合并
            try:
                jion_left_right(LEFT_FILES, RIGHT_FILES, left_indexs, BTN_ID, header)
                self.updata_date.emit(1)
            except:
                self.updata_date.emit(2)


# 主入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    win = MyCalc()
    win.show()
    os.remove('mg.ico')
    sys.exit(app.exec_())
