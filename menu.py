# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 489)
        Form.setStyleSheet("background-color: rgb(201, 250, 255);\n"
"")
        self.pushButton_sotrudniki = QtWidgets.QPushButton(Form)
        self.pushButton_sotrudniki.setGeometry(QtCore.QRect(90, 170, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_sotrudniki.setFont(font)
        self.pushButton_sotrudniki.setStyleSheet("background-color: rgb(128, 200, 255);\n"
"")
        self.pushButton_sotrudniki.setObjectName("pushButton_sotrudniki")
        self.pushButton_product = QtWidgets.QPushButton(Form)
        self.pushButton_product.setGeometry(QtCore.QRect(90, 240, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_product.setFont(font)
        self.pushButton_product.setStyleSheet("background-color: rgb(128, 200, 255);\n"
"")
        self.pushButton_product.setObjectName("pushButton_product")
        self.pushButton_client = QtWidgets.QPushButton(Form)
        self.pushButton_client.setGeometry(QtCore.QRect(90, 310, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_client.setFont(font)
        self.pushButton_client.setStyleSheet("background-color: rgb(128, 200, 255);\n"
"")
        self.pushButton_client.setObjectName("pushButton_client")
        self.pushButton_exit = QtWidgets.QPushButton(Form)
        self.pushButton_exit.setGeometry(QtCore.QRect(300, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("background-color: rgb(128, 200, 255);\n"
"")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.client_label = QtWidgets.QLabel(Form)
        self.client_label.setGeometry(QtCore.QRect(220, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.client_label.setFont(font)
        self.client_label.setObjectName("client_label")
        self.pushButton_orders = QtWidgets.QPushButton(Form)
        self.pushButton_orders.setGeometry(QtCore.QRect(90, 380, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_orders.setFont(font)
        self.pushButton_orders.setStyleSheet("background-color: rgb(128, 200, 255);\n"
"")
        self.pushButton_orders.setObjectName("pushButton_orders")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_sotrudniki.setText(_translate("Form", "Сотрудники"))
        self.pushButton_product.setText(_translate("Form", "Продукция"))
        self.pushButton_client.setText(_translate("Form", "Клиенты"))
        self.pushButton_exit.setText(_translate("Form", "Выход"))
        self.client_label.setText(_translate("Form", "Меню"))
        self.pushButton_orders.setText(_translate("Form", "Заказы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_menu()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
