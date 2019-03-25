# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_tools.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QAction, QMenu, QButtonGroup, QMessageBox, \
    QInputDialog, QProgressBar, QLineEdit, QLCDNumber, QDateTimeEdit, QSystemTrayIcon
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QPixmap, QIcon
from functions import Show_sheet_name
import os
from PyQt5.QtGui import QIcon,  QPixmap, QFont
from pdf_str import readPDF
from spiders import spider_weath


direction = ''
class Ui_Dialog(QWidget):

    def setupUi(self, Dialog):
        """
        UI模块
        :param Dialog:主界面
        :return:
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(1116, 738)
        self.cwd = os.getcwd()
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1121, 741))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tabWidget.setDocumentMode(True)
        self.setAcceptDrops(True)
        self.outers = QtWidgets.QPushButton(self.tab)
        self.outers.setGeometry(QtCore.QRect(60, 110, 100, 40))
        self.outers.setObjectName("outers")

        self.outer_y = QtWidgets.QRadioButton(self.tab)
        self.outer_y.setGeometry(QtCore.QRect(200, 100, 89, 16))
        self.outer_y.setObjectName("outer_y")

        self.outer_x = QtWidgets.QRadioButton(self.tab)
        self.outer_x.setGeometry(QtCore.QRect(200, 150, 89, 16))
        self.outer_x.setObjectName("outer_x")

        self.show_files = QtWidgets.QTextBrowser(self.tab)
        self.show_files.setGeometry(QtCore.QRect(360, 60, 271, 131))
        self.show_files.setObjectName("show_files")

        # self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        # self.pushButton_2.setGeometry(QtCore.QRect(60, 290, 100, 40))
        # self.pushButton_2.setObjectName("pushButton_2")
        #
        # self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        # self.radioButton_3.setGeometry(QtCore.QRect(200, 270, 89, 16))
        # self.radioButton_3.setObjectName("radioButton_3")
        #
        # self.radioButton_4 = QtWidgets.QRadioButton(self.tab)
        # self.radioButton_4.setGeometry(QtCore.QRect(200, 330, 89, 16))
        # self.radioButton_4.setObjectName("radioButton_4")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.groups_up = QButtonGroup()

        self.groups_up.addButton(self.outer_y, 11)
        self.groups_up.addButton(self.outer_x, 21)

        self.texttime = QtWidgets.QLCDNumber(self.tab)
        self.texttime.setGeometry(QtCore.QRect(0, 0, 500, 30))
        self.texttime.setMouseTracking(False)
        self.texttime.setDigitCount(19)
        self.texttime.setMode(QLCDNumber.Dec)
        self.texttime.setSegmentStyle(QLCDNumber.Flat)
        self.texttime.setObjectName("texttime")

        self.pdf = QtWidgets.QPushButton(self.tab)
        self.pdf.setObjectName("btn_chooseMutiFile")
        self.pdf.setText("pdf-->word")
        self.pdf.setGeometry(QtCore.QRect(700, 100, 200, 40))

        self.pdf_show = QtWidgets.QTextBrowser(self.tab)
        self.pdf_show.setGeometry(QtCore.QRect(650, 150, 300, 500))
        self.pdf_show.setObjectName("y_text")

        self.weather = QtWidgets.QTextBrowser(self.tab)
        self.weather.setGeometry(QtCore.QRect(50, 300, 600, 200))
        self.weather.setObjectName("weather")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TOOLS"))
        self.outers.setText(_translate("Dialog", "全连接"))
        self.outer_y.setText(_translate("Dialog", "横向"))
        self.outer_x.setText(_translate("Dialog", "竖向"))

        # self.pushButton_2.setText(_translate("Dialog", "交集"))
        # self.radioButton_3.setText(_translate("Dialog", "横向"))
        # self.radioButton_4.setText(_translate("Dialog", "横向"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Tool", "主页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "。。。"))
        self.outers.clicked.connect(self.Chose_file)
        self.outers.clicked.connect(lambda: Dialog.yunxing(direction, 'outer',self.show_files.toPlainText().split('\n')))

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.showtime)

        self.timer.start()

        self.pdf.clicked.connect(self.run_pdf_parse)
        self.Function_outer()
        self.Css()
        self.run_spider()
    def Function_outer(self):
        """
        槽函数挂载函数
        :return:
        """

        # self.outers.clicked.connect(self.Chose_file)
        self.groups_up.buttonClicked.connect(self.Chose_types)

    def Css(self):
        self.tab.setStyleSheet("#tab{background-color:#012456;}")
        self.tab_2.setStyleSheet("#tab_2{background-color:#012456;}")
        self.tabWidget.setStyleSheet(
            "QTabBar{background-color:#333300;outline:solid 2px;}QTabBar::tab{border-bottom-color:#C2C7CB;min-width: "
            "150px;border-right:2px solid black;border-style: outset;min-height: 40px;"
            "color:white;background-color:#4169E1;}QTabBar::tab:selected{background-color: white;"
            "color:green;border-top-right-radius:10px;border-top-left-radius:10px;border:none}QTabBar::tab:first{margin-left:10px;}"
            "QTabBar::tab:hover:!selected{color:red;background-color:black;}")
        self.outers.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')
        self.outer_y.setStyleSheet("color:white")
        self.outer_x.setStyleSheet("color:white")
        self.show_files.setStyleSheet(
            "background:transparent;border-style:outset;color:#FF8C00;border-color:#FFF5EE;")
        # self.pushButton_2.setStyleSheet(
        #     'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')
        self.pdf.setStyleSheet(
            'QPushButton{background-Color:#7FFF00;border-radius: 10px;border: 2px solid green;}QPushButton:hover{color:red;background-color:black;}')
        self.pdf_show.setStyleSheet(
            "background:transparent;border-style:outset;color:#FF8C00;border-color:#FFF5EE;font-size:20px;")
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

    def Chose_file(self):
        """
        选择多个文件
        :return:
        """

        files1 = []
        files, filetype = QFileDialog.getOpenFileNames(self,"选择文件",self.cwd,"Excle (*.xlsx);;")
        for  i in files:
            self.show_files.append(i)
        # self.outers.clicked.connect(lambda: Dialog.yunxing(direction, 2, FILES))

    def Chose_types(self):
        """
        选择合并类型函数
        :return:
        """
        sender = self.sender()
        global direction
        if sender == self.groups_up:
            if self.groups_up.checkedId() == 11:

                print('chosE函数',sender)
                direction = 1

            elif self.groups_up.checkedId() == 21:

                direction = 0

    def run_pdf_parse(self):
        """
        pdf转换模块（后期优化，放进子进程模块)
        :return: 同文件名word版本.eg:文件.pdf --- 文件.doc
        """
        self.pdf_show.clear()
        files, filetype = QFileDialog.getOpenFileNames(self, "选择文件", self.cwd, "PDF Files (*.pdf);;")

        if len(files) == 0:
            return

        for file in files:
            texts = readPDF(file)
            self.pdf_show.append(texts)

    def run_spider(self):
        result = spider_weath()
        print(result)
        # ip = get_host_ip()
        # QMessageBox.question(self, 'HI', '来自 %s %s %s的你,你好吖！'%(result[0], result[1], result[2]),
        #                      QMessageBox.Yes, QMessageBox.Yes)
        # self.weather.setHtml(
        #     " &nbsp;<font color='red' >📍&nbsp;</font>：%s %s %s <br /> <font color='#FF8C00' >&nbsp;➤&nbsp;</font>：%s <br /> &nbsp;"
        #     "<font color='#FF4500' >☎&nbsp;</font>：%s" % (
        #         result[0], result[1], result[2], result[3], 'uu'))

        self.weather.setFont(QFont("Mongolian Baiti", 10, QFont.Bold))
        self.weather.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:white")
        # self.weather.setHtml("<font color='#FF8C00' >555</font>" + result[10] + "  " + result[11])
        self.weather.setFont(QFont("Mongolian Baiti", 10, QFont.Bold))
        self.weather.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:white")
        # -----------------------------------------------------------------------------------------
        self.weather.setText("%s°" % result[4])  # 温度
        self.weather.setFont(QFont("Mongolian Baiti", 40, QFont.Bold))
        self.weather.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	white")

        # self.textBrowser_5.setText("")  # 温度
        # self.textBrowser_5.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        # self.textBrowser_5.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	white")

        self.weather.setHtml(
            "<font color='#FF8C00' >%s %s</font><br/> <font color='green' >湿度%s%% </font><br/> %s %s%s级 %s <br/> <font color='green' >%s</font><br/>" % (result[0],result[1],
                result[5], result[7], result[8], result[6], result[9],result[-1]))  # 温度
        self.weather.setFont(QFont("Mongolian Baiti", 15, QFont.Bold))
        self.weather.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:	white")