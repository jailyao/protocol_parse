# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from UI import about
from parse import protocol_104, common_interface, protocol_13761, protocol_698

protocol_type_dic = {'104': 0, '1376.1': 1, '698': 2, '101': 3}

class Ui_Mainwindow(object):
    def __init__(self):
        self.ParseObj = 0

    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parse_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.parse_pushButton.setGeometry(QtCore.QRect(630, 220, 75, 23))
        self.parse_pushButton.setObjectName("parse_pushButton")
        self.protocol_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.protocol_comboBox.setGeometry(QtCore.QRect(100, 220, 69, 22))
        self.protocol_comboBox.setObjectName("protocol_comboBox")
        self.protocol_comboBox.addItem("")
        self.protocol_comboBox.addItem("")
        self.protocol_comboBox.addItem("")
        self.protocol_comboBox.addItem("")
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(100, 30, 131, 16))
        self.input_label.setObjectName("input_label")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(100, 250, 131, 16))
        self.output_label.setObjectName("output_label")
        self.input_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.input_textEdit.setGeometry(QtCore.QRect(100, 60, 601, 151))
        self.input_textEdit.setObjectName("input_textEdit")
        self.output_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.output_textEdit.setGeometry(QtCore.QRect(100, 280, 601, 271))
        self.output_textEdit.setObjectName("output_textEdit")
        Mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mainwindow)
        self.statusbar.setObjectName("statusbar")
        Mainwindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(Mainwindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(Mainwindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Mainwindow)
        self.actionAbout.triggered.connect(self.show_About)
        self.parse_pushButton.clicked.connect(self.Get_Protocol_type)
        self.parse_pushButton.clicked.connect(self.show_parse_result)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "规约解析工具"))
        self.parse_pushButton.setText(_translate("Mainwindow", "解析"))
        self.protocol_comboBox.setItemText(0, _translate("Mainwindow", "104"))
        self.protocol_comboBox.setItemText(1, _translate("Mainwindow", "1376.1"))
        self.protocol_comboBox.setItemText(2, _translate("Mainwindow", "698"))
        self.protocol_comboBox.setItemText(3, _translate("Mainwindow", "101"))
        self.input_label.setText(_translate("Mainwindow", "请输入待解析规约："))
        self.output_label.setText(_translate("Mainwindow", "规约解析如下："))
        self.menuHelp.setTitle(_translate("Mainwindow", "Help"))
        self.actionAbout.setText(_translate("Mainwindow", "About"))
        self.actionHelp.setText(_translate("Mainwindow", "Help"))

    def show_About(self):
        self.AboutWindow = QtWidgets.QMainWindow()
        self.about_ui = about.Ui_About()
        self.about_ui.setupUi(self.AboutWindow)
        self.AboutWindow.show()

    def Get_Protocol_type(self):
        type_description = self.protocol_comboBox.currentText()
        self.protocol_type = protocol_type_dic[type_description]
        if self.protocol_type == 0:    # 104 protocol
            self.ParseObj = protocol_104.Pro_104_Parse()
        elif self.protocol_type == 1:  # 1376.1 protocol
            self.ParseObj = protocol_13761.Pro_13761_Parse()
        else:
            self.ParseObj = protocol_698.Pro_69845_Parse()

    def show_parse_result(self):
        self.input_frame = self.input_textEdit.toPlainText()
        if self.input_frame is '':
            self.output_textEdit.setText('未输入有效帧，请重新输入！\n')
            return
        self.input_frame = self.input_frame.replace(' ', '')  # replace space
        self.input_frame = self.input_frame.replace('-', '')  # replace '-'
        self.input_frame = self.input_frame.replace('\n', '')  # replace '\n'
        for c_data in self.input_frame:
            if not ((c_data <= '9' and c_data >= '0') or (c_data >= 'a' and c_data <= 'f') or (c_data >= 'A' and c_data <= 'F')):
                self.output_textEdit.setText('未输入有效帧，请重新输入！\n')
                return
        self.frame = common_interface.HexStrToHexArray(self.input_frame)
        self.output_result = self.ParseObj.ParseFrame(self.frame)
        self.output_textEdit.setText(self.output_result)
