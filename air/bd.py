from PyQt5.QtWidgets import*
import PCM
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from progeckt import prog
import random
import spisok
from Man import Managers
from captcha import Captcha
from admin import Admin
from Derector import Derector
from spisok import Spisok
from prosmotr import Prosmotr
from rukovod1 import Rukovod1


class Avtoriz(PCM.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('progect')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.enter)
        self.pushButton_2.clicked.connect(self.guest)
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton_4.clicked.connect(self.admin)

    def enter(self):
        query = QSqlQuery()
        query.exec(
            f"SELECT * FROM public.staff WHERE login = '{self.lineEdit_Login.text()}' AND password = '{self.lineEdit_Pass.text()}'")
        if query.first():
            if query.value(3) == 2:
                self.sw = Derector2()
                self.sw.show()

            elif query.value(3) == 1:
                self.sw = Managers2()
                self.sw.show()

        else:
            QMessageBox.critical(self, "ОШИБКА", "Логин или пароль не верный")
            self.sw = Captcha1()

            self.sw.show()

    def guest(self):
        self.sw = prog1()
        self.sw.show()

    def dobav(self):
        self.go = spisok()
        self.sw.show()

    def exit(self):
        self.close()

    def admin(self):
        if self.lineEdit_Login.text() == "Admin" and self.lineEdit_Pass.text() == "Admin":
            self.sw = Admin1()
            self.sw.setupUi(self.sw)
            self.sw.show()

class Managers2(Managers):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        queru = QSqlTableModel()
        sql = "SELECT * FROM public.projects"
        queru.setQuery(QSqlQuery(sql))
        print(QSqlQuery(sql).isActive())
        self.tableView.setModel(queru)
        self.tableView.setColumnHidden(0, True)
        self.pushButton_Exit.clicked.connect(self.exit)
        self.pushButton_dobav.clicked.connect(self.dobav)
        self.pushButton_prosmtr.clicked.connect(self.prosmotr)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_prosmotr2.clicked.connect(self.prosmotr2)
    
    def exit(self):
        self.close()

    def dobav(self):
        self.go = Spisoc(self.tableView)
        self.go.setupUi(self.go)
        self.go.show()

    def prosmotr(self):
        self.pr = Prosmotr1()
        self.pr.show()

    def prosmotr2(self):
        self.pr = Rukovod1(self.comboBox.currentText())
        self.pr.show()


    def delete(self):
        query = QSqlTableModel()
        query.setTable("projects")
        query.select()
        selected = self.tableView.selectedIndexes()
        rows = set(index.row() for index in selected)
        rows = list(rows)
        rows.sort()
        first = rows[0]
        query.removeRow(first)
        query.select()
        query = QSqlTableModel()
        query.setTable("projects")
        query.select()
        self.tableView.setModel(query)

class Derector2(Derector):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        queru = QSqlTableModel()
        sql = "SELECT * FROM public.projects"
        queru.setQuery(QSqlQuery(sql))
        print(QSqlQuery(sql).isActive())
        self.tableView.setModel(queru)
        self.tableView.setColumnHidden(0, True)
        self.pushButton_Exit.clicked.connect(self.exit)
        self.pushButton_dobav.clicked.connect(self.dobav)
        self.pushButton_prosmtr.clicked.connect(self.prosmotr)

    def delete(self):
        query = QSqlTableModel()
        query.setTable("projects")
        query.select()
        selected = self.tableView.selectedIndexes()
        rows = set(index.row() for index in selected)
        rows = list(rows)
        rows.sort()
        first = rows[0]
        query.removeRow(first)
        query.select()
        query = QSqlTableModel()
        query.setTable("projects")
        query.select()
        self.tableView.setModel(query)

    def exit(self):
        self.close()

    def dobav(self):
        self.go = Spisoc(self.tableView)
        self.go.setupUi(self.go)
        self.go.show()

    def prosmotr(self):
        self.pr = Prosmotr1()
        self.pr.show()


class Prosmotr1(Prosmotr):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
    
        queru = QSqlQuery()
        sql = "SELECT * FROM public.projects"
        queru.exec(sql)
        values = []
        if queru.first():
            j = 0
            while True:
                if queru.isNull(j):
                    break
                else:
                    values.append(queru.value(j))
                    j += 1
        self.lineEdit_name.setText(values[1])
        self.lineEdit_text.setText(values[2])
        self.lineEdit_director.setText(values[3])
        self.lineEdit_manage.setText(values[4])
        self.lineEdit_change.setText(values[5])
        self.lineEdit_city.setText(values[6])
        self.lineEdit_street.setText(values[7])
        self.lineEdit_index.setText(str(values[8]))
        self.pushButton_Close.clicked.connect(self.exit)
        self.pushButton_close2.clicked.connect(self.exit2)

    def exit(self):
        self.close()

    def exit2(self):

        self.sw = Derector2()
        self.sw.show()
        self.close()


class Spisoc(Spisok):

    def __init__(self, t):
        super().__init__()
        self.tableView = t
        self.setupUi(self)

    def add(self):
        q = f"INSERT INTO public.projects (name, text, director_id, manager_id, change_id, city_id, street, index, date) VALUES ('{self.lineEdit_name.text()}', '{self.lineEdit_text.text()}', '{self.lineEdit_director.text()}', '{self.lineEdit_change.text()}', '{self.lineEdit_city.text()}','{self.lineEdit_street.text()}', '{self.lineEdit_index.text()}', '{self.lineEdit_date.text()})"
        queru = QSqlQuery(q)
        print(queru.isActive())
        queru.exec()
        t = QSqlQueryModel()
        t.setQuery("SELECT * FROM public.projects")
        self.tableView.setModel(t)
        self.close()

    def exit(self):
        self.close()


class Captcha1(Captcha):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.label_Kapcha.setText(str(random.randint(1000, 9000)))

        self.timer = QTimer()
        self.count = 10
        self.label_Time.setText(str(self.count))
        self.timer.timeout.connect(self.timer_tick)

        self.pushButton.clicked.connect(self.ver)

    def ver(self):

        if self.lineEdit_kapcha.text() == self.label_Kapcha.text():
            QMessageBox.information(self, "Успех", "Капча введена правильно")
            self.close()

        else:
            self.lineEdit_kapcha.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "ОШИБКА", "Вы ввели неправильно")
            self.timer_tick()

    def timer_tick(self):
        self.timer.start(1000)
        self.count -= 1
        self.label_Time.setText(str(self.count))

        if self.count == 0:
            self.timer.stop()
            self.count = 10
            self.lineEdit_kapcha.setDisabled(False)


class prog1(prog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        queru = QSqlTableModel()
        sql = "SELECT * FROM public.projects"
        queru.setQuery(QSqlQuery(sql))
        print(QSqlQuery(sql).isActive())
        self.tableView.setModel(queru)
        self.tableView.setColumnHidden(0, True)
        self.pushButton_2.clicked.connect(self.exit)

    def exit(self):
        self.close()

class Admin1(Admin):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def dobav(self):
        q = f"INSERT INTO public.staff (login, password, role_id) VALUES ('{self.lineEdit_Login.text()}', '{self.lineEdit_password.text()}', '2')"

        queru = QSqlQuery(q)
        print(queru.isActive())
        queru.exec()

    def exit(self):
        self.close()
