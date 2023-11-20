from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *


class spisoc(QMainWindow):
    
    def __init__(self, t):
        super().__init__()
        self.tableView = t
        self.setupUi(self)

      

        
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 319)
        MainWindow.setStyleSheet("background-color: rgb(218, 207, 183);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 971, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_change = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_change.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_change.setObjectName("lineEdit_change")
        self.gridLayout.addWidget(self.lineEdit_change, 1, 4, 1, 1)
        self.lineEdit_city = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_city.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 1, 5, 1, 1)
        self.lineEdit_director = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_director.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_director.setObjectName("lineEdit_director")
        self.gridLayout.addWidget(self.lineEdit_director, 1, 2, 1, 1)
        self.lineEdit_street = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_street.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.gridLayout.addWidget(self.lineEdit_street, 1, 6, 1, 1)
        self.lineEdit_index = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_index.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_index.setObjectName("lineEdit_index")
        self.gridLayout.addWidget(self.lineEdit_index, 1, 7, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 1, 0, 1, 1)
        self.lineEdit_manage = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_manage.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_manage.setObjectName("lineEdit_manage")
        self.gridLayout.addWidget(self.lineEdit_manage, 1, 3, 1, 1)
        self.lineEdit_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_text.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_text.setObjectName("lineEdit_text")
        self.gridLayout.addWidget(self.lineEdit_text, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 7, 1, 1)
        self.pushButton_dobav = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dobav.setGeometry(QtCore.QRect(880, 280, 101, 26))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_dobav.setFont(font)
        self.pushButton_dobav.setObjectName("pushButton_dobav")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(10, 280, 101, 26))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Exit.clicked.connect(self.Exit)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 10, 371, 51))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_dobav.clicked.connect(self.add)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Название</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Описание</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Руководитель</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Менеджр</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Изминенеие </p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Город</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Улица</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Индекс</p></body></html>"))
        self.pushButton_dobav.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Назад"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Внесите данные проекта</p></body></html>"))

    def add(self):
        q = f"INSERT INTO public.projects (name, text, director_id, manager_id, change_id, city_id, street, index) VALUES ('{self.lineEdit_name.text()}', '{self.lineEdit_text.text()}', '{self.lineEdit_director.text()}', '{self.lineEdit_manage.text()}', '{self.lineEdit_change.text()}', '{self.lineEdit_city.text()}', '{self.lineEdit_street.text()}', '{self.lineEdit_index.text()}')"
        # db = QSqlDatabase.addDatabase('QPSQL')
        # db.setDatabaseName('progect')
        # db.setHostName('localhost')
        # db.setPort(5432)
        # db.setUserName('postgres')
        # db.setPassword('student')
        # db.open()
        
        queru = QSqlQuery(q)
        print(queru.isActive())
        queru.exec()
        t = QSqlQueryModel()
        t.setQuery("SELECT * FROM public.projects")
        self.tableView.setModel(t)
        self.close()


    def Exit(self):
        self.close()