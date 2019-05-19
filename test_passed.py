# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2


class Ui_MainWindow(object):
    def loadData(self):
        table_name = "table_customers"
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

            sql = f"SELECT * FROM {table_name}"
            cur.execute(sql)
            result = cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_date in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colum_number, date in enumerate(row_date):
                    self.tableWidget.setItem(
                        row_number, colum_number, QtWidgets.QTableWidgetItem(str(date)))
        except psycopg2.Error as e:
            print(e)
        conn.close()

    def gettablename(self):
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
            sql =f"SELECT tablename FROM pg_tables WHERE tablename NOT LIKE 'pg%' AND tablename NOT LIKE 'sql_%'  AND tablename NOT LIKE '%finished' ORDER BY tablename"
            cur.execute(sql)
            rows=cur.fetchall()
            for row in rows:
                self.cbx_tablelist.addItem(row[0])
        except psycopg2.Error as e:
            print(e)

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
        self.btn_load.clicked.connect(self.loadData)        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 520, 251, 96))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(27)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbx_tablelist = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cbx_tablelist.setFont(font)
        self.cbx_tablelist.setObjectName("cbx_tablelist")

        self.verticalLayout.addWidget(self.cbx_tablelist)
        self.btn_gettablename = QtWidgets.QPushButton(self.widget)
        self.btn_gettablename.setObjectName("btn_gettablename")
        self.btn_gettablename.clicked.connect(self.gettablename)        
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
