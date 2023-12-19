import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem, QWidget

import avtoriz
import registr
from menu import Ui_menu
from client import Ui_client
from employees import Ui_employees
from orders import Ui_orders
from product import Ui_product


db = sqlite3.connect('flowers.db')
cursor = db.cursor()


class Registr(QtWidgets.QMainWindow, registr.Ui_registr):
    def __init__(self):
        super(Registr, self).__init__()
        self.setupUi(self)
        self.lineEdit_Imia_2.setPlaceholderText('Введите логин')
        self.lineEdit_Imia_3.setPlaceholderText('Введите пароль')
        self.pushButton_delete_2.pressed.connect(self.reg)
        self.pushButton_delete.pressed.connect(self.login)

    def login(self):
        self.login_window = Login()
        self.login_window.show()
        self.hide()

        def reg(self):
        try:
            user_login = self.lineEdit_Imia_2.text()
            user_parol = self.lineEdit_Imia_3.text()

            if len(user_login) == 0 or len(user_parol) == 0:
                return

            cursor.execute('INSERT INTO users (login, parol) VALUES (?, ?)', (user_login, user_parol))

            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO users VALUES("{user_login}","{user_parol}")')
                self.label_pustaia.setText(f'Аккаунт {user_login} успешно зарегистрирован')
                db.commit()

        except Exception as e:
            print(f'Ошибка при регистрации: {e}')
            self.label_pustaia.setText(f'Ошибка при регистрации. Попробуйте еще раз.')


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = avtoriz.Ui_avtoriz()
        self.ui.setupUi(self)
        self.ui.lineEdit_Imia_2.setPlaceholderText('Введите логин')
        self.ui.lineEdit_Imia_3.setPlaceholderText('Введите пароль')
        self.ui.pushButton_delete.clicked.connect(self.login)
        self.ui.pushButton_delete_2.clicked.connect(self.reg)

    def reg(self):
        self.reg_window = Registr()
        self.reg_window.show()
        self.hide()

    def login(self):
        try:
            user_login = self.ui.lineEdit_Imia_2.text()
            user_parol = self.ui.lineEdit_Imia_3.text()

            if len(user_login) == 0:
                return
            if len(user_parol) == 0:
                return

            cursor.execute(f'SELECT parol FROM users WHERE login = "{user_login}"')
            check_par = cursor.fetchall()

            cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
            check_login = cursor.fetchall()

            if check_par and check_login and check_par[0][0] == user_parol and check_login[0][0] == user_login:
                self.open_menu()
            else:
                self.ui.label_pustaia.setText(f'Неверный логин или пароль')
        except Exception as e:
            print(f'Ошибка при авторизации: {e}')
            self.ui.label_pustaia.setText(f'Ошибка при авторизации')

    def open_menu(self):
        self.menu = Menu()
        self.menu.show()
        self.hide()

class Menu(QtWidgets.QMainWindow, Ui_menu):
    def __init__(self):
        super(Menu, self).__init__()
        self.setupUi(self)
        self.pushButton_sotrudniki.clicked.connect(self.open_sotrudniki)
        self.pushButton_product.clicked.connect(self.open_product)
        self.pushButton_client.clicked.connect(self.open_client)
        self.pushButton_orders.clicked.connect(self.open_orders)
        self.pushButton_exit.clicked.connect(self.exit_application)



    def open_sotrudniki(self):
        self.sotrudniki_window = Employees()
        self.sotrudniki_window.show()

    def open_product(self):
        self.product_window = Product()
        self.product_window.show()

    def open_client(self):
        self.client_window = Client()
        self.client_window.show()

    def open_orders(self):
        self.orders_window = Orders()
        self.orders_window.show()

    def exit_application(self):
        QApplication.quit()

class Employees(QWidget, Ui_employees):
    def __init__(self):
        super(Employees, self).__init__()
        self.setupUi(self)

        # Добавляем всплывающие подсказки для кнопок
        self.pushButton_open.setToolTip('Открыть записи')
        self.pushButton_delete.setToolTip('Удалить записи')
        self.pushButton_insert.setToolTip('Добавить записи')

        # Добавляем всплывающую подсказку для текстовых полей
        self.lineEdit_Imia_4.setToolTip('Имя')
        self.lineEdit_Familia_2.setToolTip('Фамилия')
        self.lineEdit_Otchestvo_2.setToolTip('Отчество')
        self.lineEdit_numder_2.setToolTip('Номер телефона')
        self.lineEdit_email_2.setToolTip('Email')
        self.lineEdit_Imia_5.setToolTip('Номер клиента')
        self.lineEdit_Imia_6.setToolTip('Номер заказа')
        self.lineEdit_Imia_7.setToolTip('Должность')
        self.lineEdit_Imia_8.setToolTip('Зарплата')
        self.lineEdit_delet1.setToolTip('Удалить запись по фамилии')

        self.pushButton_open.clicked.connect(self.open_employees)
        self.pushButton_delete.clicked.connect(self.delete_employees)
        self.pushButton_insert.clicked.connect(self.insert_employees)
        self.conn = sqlite3.connect('flowers.db')
        self.update()
    def open_employees(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM employees")
            data = cur.fetchall()
            col_name = [i[0] for i in cur.description]
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="SELECT * FROM employees"):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            data = cur.fetchall()
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_employees(self):
        row = [
            self.lineEdit_Imia_4.text(),
            self.lineEdit_Familia_2.text(),
            self.lineEdit_Otchestvo_2.text(),
            self.lineEdit_numder_2.text(),
            self.lineEdit_email_2.text(),
            self.lineEdit_Imia_5.text(),
            self.lineEdit_Imia_6.text(),
            self.lineEdit_Imia_7.text(),
            self.lineEdit_Imia_8.text()
        ]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into employees(name, surname, lastname, post, salary, number, email, 
            id_client, id_orders)
                        values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}',
                        '{row[7]}','{row[8]}')""")

            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись:", r)
            return r

        self.update()





    def delete_employees(self):
        surname = self.lineEdit_delet1.text()
        conn = sqlite3.connect('flowers.db')
        c = conn.cursor()
        c.execute("DELETE FROM employees WHERE surname=?", (surname,))
        conn.commit()
        conn.close()
        self.update()

class Product(QWidget, Ui_product):
    def __init__(self):
        super(Product, self).__init__()
        self.setupUi(self)

        # Добавляем всплывающие подсказки для кнопок
        self.pushButton_open.setToolTip('Открыть записи')
        self.pushButton_delete.setToolTip('Удалить записи')
        self.pushButton_insert.setToolTip('Добавить записи')

        # Добавляем всплывающую подсказку для текстовых полей
        self.lineEdit_Imia.setToolTip('Название товара')
        self.lineEdit_Imia_2.setToolTip('Описание товара')
        self.lineEdit_Imia_3.setToolTip('Цена товара')
        self.lineEdit_Imia_4.setToolTip('Наличие товара')
        self.lineEdit_delet1.setToolTip('Удалить запись по названию товара')

        self.pushButton_open.clicked.connect(self.open_product)
        self.pushButton_delete.clicked.connect(self.delete_product)
        self.pushButton_insert.clicked.connect(self.insert_product)
        self.conn = sqlite3.connect('flowers.db')
        self.update()


    def open_product(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM products")
            data = cur.fetchall()
            col_name = [i[0] for i in cur.description]
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="SELECT * FROM products"):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            data = cur.fetchall()
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_product(self):
        row = [
            self.lineEdit_Imia.text(),
            self.lineEdit_Imia_2.text(),
            self.lineEdit_Imia_3.text(),
            self.lineEdit_Imia_4.text()
        ]

        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into products(name, description, price, availability)
                            values('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}')""")

            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись:", r)
            return r

        self.update()

    def delete_product(self):
        name = self.lineEdit_delet1.text()
        conn = sqlite3.connect('flowers.db')
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE name=?", (name,))
        conn.commit()
        conn.close()
        self.update()



class Client(QWidget, Ui_client):
    def __init__(self):
        super(Client, self).__init__()
        self.setupUi(self)

        # Добавляем всплывающие подсказки для кнопок
        self.pushButton_open.setToolTip('Открыть записи')
        self.pushButton_delete.setToolTip('Удалить записи')
        self.pushButton_insert.setToolTip('Добавить записи')

        # Добавляем всплывающую подсказку для текстовых полей
        self.lineEdit_Imia.setToolTip('Имя')
        self.lineEdit_Familia.setToolTip('Фамилия')
        self.lineEdit_Otchestvo.setToolTip('Отчество')
        self.lineEdit_numder.setToolTip('Номер телефона')
        self.lineEdit_email.setToolTip('Email')
        self.lineEdit_Imia_2.setToolTip('Номер сотрудника')
        self.lineEdit_Imia_3.setToolTip('Номер заказа')
        self.lineEdit_delet1.setToolTip('Удалить запись по фамилии')

        self.pushButton_open.clicked.connect(self.open_client)
        self.pushButton_delete.clicked.connect(self.delete_client)
        self.pushButton_insert.clicked.connect(self.insert_client)
        self.conn = sqlite3.connect('flowers.db')
        self.update()

    def open_client(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM customers")
            data = cur.fetchall()
            col_name = [i[0] for i in cur.description]
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="SELECT * FROM customers"):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            data = cur.fetchall()
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_client(self):
        row = [
            self.lineEdit_Imia.text(),
            self.lineEdit_Familia.text(),
            self.lineEdit_Otchestvo.text(),
            self.lineEdit_numder.text(),
            self.lineEdit_email.text(),
            self.lineEdit_Imia_2.text(),
            self.lineEdit_Imia_3.text()
            ]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into customers(name, surname, lastname,
                            number, email, id_employees, id_orders)
                            values('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}')""")

            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись:", r)
            return r

        self.update()

    def delete_client(self):
        surname = self.lineEdit_delet1.text()
        conn = sqlite3.connect('flowers.db')
        c = conn.cursor()
        c.execute("DELETE FROM customers WHERE surname=?", (surname,))
        conn.commit()
        conn.close()
        self.update()


class Orders(QWidget, Ui_orders):
    def __init__(self):
        super(Orders, self).__init__()
        self.setupUi(self)

        # Добавляем всплывающие подсказки для кнопок
        self.pushButton_open.setToolTip('Открыть записи')
        self.pushButton_delete.setToolTip('Удалить записи')
        self.pushButton_insert.setToolTip('Добавить записи')

        # Добавляем всплывающую подсказку для текстовых полей
        self.lineEdit_Imia_9.setToolTip('Наименование')
        self.lineEdit_Imia_2.setToolTip('Количество товара')
        self.lineEdit_Imia_3.setToolTip('Сумма заказа')
        self.lineEdit_Imia_4.setToolTip('Статус заказа')
        self.lineEdit_Imia_5.setToolTip('Номер клиента')
        self.lineEdit_Imia_6.setToolTip('Номер продукта')
        self.lineEdit_Imia_7.setToolTip('Номер сотрудника')
        self.lineEdit_delet1.setToolTip('Удалить запись по наименованию товара')

        self.pushButton_open.clicked.connect(self.open_order)
        self.pushButton_delete.clicked.connect(self.delete_order)
        self.pushButton_insert.clicked.connect(self.insert_order)
        self.conn = sqlite3.connect('flowers.db')
        self.update()


    def open_order(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM orders")
            data = cur.fetchall()
            col_name = [i[0] for i in cur.description]
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="SELECT * FROM orders"):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            data = cur.fetchall()
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)
            return

        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_order(self):
        row = [
            self.lineEdit_Imia_9.text(),
            self.lineEdit_Imia_2.text(),
            self.lineEdit_Imia_3.text(),
            self.lineEdit_Imia_4.text(),
            self.lineEdit_Imia_5.text(),
            self.lineEdit_Imia_6.text(),
            self.lineEdit_Imia_7.text()
        ]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into orders(name, amount, summ_orders, status_orders,
            id_client, id_products, id_employees)
                        values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}')""")

            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись:", r)
            return r

        self.update()

    def delete_order(self):
        name = self.lineEdit_delet1.text()
        conn = sqlite3.connect('flowers.db')
        c = conn.cursor()
        c.execute("DELETE FROM orders WHERE name=?", (name,))
        conn.commit()
        conn.close()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())