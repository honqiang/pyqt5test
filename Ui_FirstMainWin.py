# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\编程\pyqt5\FirstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 891, 491))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(690, 520, 151, 28))
        self.btn_load.setObjectName("btn_load")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 520, 251, 96))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(27)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbx_tablelist = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cbx_tablelist.setFont(font)
        self.cbx_tablelist.setObjectName("cbx_tablelist")
        self.verticalLayout.addWidget(self.cbx_tablelist)
        self.btn_gettablename = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_gettablename.setObjectName("btn_gettablename")
        self.verticalLayout.addWidget(self.btn_gettablename)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_load.setText(_translate("MainWindow", "load"))
        self.btn_gettablename.setText(_translate("MainWindow", "获取表格"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

