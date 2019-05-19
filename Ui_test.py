# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\编程\pyqt5\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

class Ui_form_closewin(object):
    def gettable(self):
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
            sql =f"SELECT tablename FROM pg_tables WHERE tablename NOT LIKE 'pg%' AND tablename NOT LIKE 'sql_%' ORDER BY tablename"
            cur.execute(sql)
            rows=cur.fetchall()
            for row in rows:
                self.comboBox.addItem(row[0])
        except psycopg2.Error as e:
            print(e)
        
    def setupUi(self, form_closewin):
        form_closewin.setObjectName("form_closewin")
        form_closewin.resize(795, 666)
        self.btn_acquiretable = QtWidgets.QPushButton(form_closewin)
        self.btn_acquiretable.setGeometry(QtCore.QRect(140, 360, 93, 28))
        self.btn_acquiretable.setObjectName("btn_acquiretable")
        self.btn_acquiretable.clicked.connect(self.gettable)
        self.comboBox = QtWidgets.QComboBox(form_closewin)
        self.comboBox.setGeometry(QtCore.QRect(80, 270, 221, 41))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(form_closewin)
        QtCore.QMetaObject.connectSlotsByName(form_closewin)

    def retranslateUi(self, form_closewin):
        _translate = QtCore.QCoreApplication.translate
        form_closewin.setWindowTitle(_translate("form_closewin", "Form"))
        self.btn_acquiretable.setText(_translate("form_closewin", "获取表格"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_closewin = QtWidgets.QWidget()
    ui = Ui_form_closewin()
    ui.setupUi(form_closewin)
    form_closewin.show()
    sys.exit(app.exec_())

