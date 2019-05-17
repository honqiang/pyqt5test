# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\OneDrive\OneDrive - Shanghai Jiao Tong University\编程\pyqt5\FirstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2


class Ui_MainWindow(object):
    def loadData(self):
        try:
            host_ip = "192.168.17.146"
            user = "postgres"
            password = "postgres"
            database = "testDB"
            conn = psycopg2.connect(
                host=f"{host_ip}", user=f"{user}", password=f"{password}", database=f"{database}")
            print(f"连接{database}数据库成功")
        except psycopg2.Error as e:
            print(e)

        try:
            cur = conn.cursor()
            sql = "SELECT * FROM customers"
            cur.execute(sql)
            result = cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_date in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colum_number, date in enumerate(row_date):
                    self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(date)))

        except psycopg2.Error as e:
            print(e)
        conn.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 891, 491))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(400, 540, 93, 28))
        self.btn_load.setObjectName("btn_load")
        self.btn_load.clicked.connect(self.loadData)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
