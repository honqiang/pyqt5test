# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\编程\pyqt5\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main_win import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 330, 291, 39))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.btn_login.clicked.connect(self.login_username)
        self.horizontalLayout.addWidget(self.btn_login)
        self.btn_logout = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.btn_logout.clicked.connect(MainWindow.close)
        self.horizontalLayout.addWidget(self.btn_logout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(480, 240, 191, 41))
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(16)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 240, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(480, 150, 191, 41))
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(16)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setContextMenuPolicy(
            QtCore.Qt.DefaultContextMenu)
        self.lineEdit_username.setObjectName("lineEdit_username")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_login.setText(_translate("MainWindow", "登录"))
        self.btn_logout.setText(_translate("MainWindow", "取消"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.lineEdit_password.setPlaceholderText(
            _translate("MainWindow", "输入密码"))
        self.label_2.setText(_translate("MainWindow", "密     码"))
        self.lineEdit_username.setPlaceholderText(
            _translate("MainWindow", "请输入用户名"))

    def login_username(self):
        usr_login = self.lineEdit_username.text()
        pwd_login = self.lineEdit_password.text()
        if usr_login == "admin":
            ui_main.show()
            MainWindow.close()
        else:
            QMessageBox.warning(self,
                                "警告",
                                "用户名或密码错误",
                                QMessageBox.Yes)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui_main = first_mainwindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
