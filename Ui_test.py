# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\编程\pyqt5\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_closewin(object):
    def setupUi(self, form_closewin):
        form_closewin.setObjectName("form_closewin")
        form_closewin.resize(795, 666)
        self.btn_closewin = QtWidgets.QPushButton(form_closewin)
        self.btn_closewin.setGeometry(QtCore.QRect(320, 450, 93, 28))
        self.btn_closewin.setObjectName("btn_closewin")
        self.retranslateUi(form_closewin)
        self.btn_closewin.clicked.connect(form_closewin.close)
        QtCore.QMetaObject.connectSlotsByName(form_closewin)

    def retranslateUi(self, form_closewin):
        _translate = QtCore.QCoreApplication.translate
        form_closewin.setWindowTitle(_translate("form_closewin", "Form"))
        self.btn_closewin.setText(_translate("form_closewin", "关闭窗口"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_closewin = QtWidgets.QWidget()
    ui = Ui_form_closewin()
    ui.setupUi(form_closewin)
    form_closewin.show()
    sys.exit(app.exec_())

