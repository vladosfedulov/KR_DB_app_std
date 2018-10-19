# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime

from PyQt5 import QtCore, QtWidgets
from query import query_in


DB_REQUEST_FIO = "select distinct FIO_prep from zanyatie"
DB_REQUEST_Ngrupp = "select distinct N_gruppi from gruppazanyatie"

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 680)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 681))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 381, 611))
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 10, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 40, 381, 611))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setOverwriteMode(False)
        self.textEdit_2.setReadOnly(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(70, 50, 47, 13))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_3)
        self.lcdNumber.setGeometry(QtCore.QRect(250, 10, 121, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Расписание занятий"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Расписание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Найти преподавателя"))
        self.pushButton.setText(_translate("Form", "NULL"))
        self.pushButton_2.setText(_translate("Form", "NOT NULL"))
        self.label.setText(_translate("Form", "Choice"))
        self.label_2.setText(_translate("Form", "Good luck"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Казино"))

        self.lcdNumber.display(datetime.strftime(datetime.now(), "%H:%M"))

        position_cb = 0

        for Ngroup in query_in(DB_REQUEST_Ngrupp):
            self.comboBox.addItem("")
            self.comboBox.setItemText(position_cb, _translate("MainWindow", Ngroup[0]))
            position_cb += 1

        position_cb = 0

        for fio in query_in(DB_REQUEST_FIO):
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(position_cb, _translate("MainWindow", fio[0]))
            position_cb += 1