# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\编程\pyqt5\test_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_closewin(object):
    def setupUi(self, form_closewin):
        form_closewin.setObjectName("form_closewin")
        form_closewin.resize(795, 666)
        self.btn_acquiretable = QtWidgets.QPushButton(form_closewin)
        self.btn_acquiretable.setGeometry(QtCore.QRect(140, 360, 93, 28))
        self.btn_acquiretable.setObjectName("btn_acquiretable")
        self.comboBox = QtWidgets.QComboBox(form_closewin)
        self.comboBox.setGeometry(QtCore.QRect(80, 270, 221, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(form_closewin)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(450, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(form_closewin)
        QtCore.QMetaObject.connectSlotsByName(form_closewin)

    def retranslateUi(self, form_closewin):
        _translate = QtCore.QCoreApplication.translate
        form_closewin.setWindowTitle(_translate("form_closewin", "Form"))
        self.btn_acquiretable.setText(_translate("form_closewin", "获取表格"))
        self.pushButton.setText(_translate("form_closewin", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_closewin = QtWidgets.QWidget()
    ui = Ui_form_closewin()
    ui.setupUi(form_closewin)
    form_closewin.show()
    sys.exit(app.exec_())

