from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *


class Spisok(QMainWindow):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 275)
        MainWindow.setStyleSheet("background-color: rgb(218, 207, 183);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 1031, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_city = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_city.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.gridLayout.addWidget(self.lineEdit_city, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.lineEdit_street = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_street.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.gridLayout.addWidget(self.lineEdit_street, 1, 5, 1, 1)
        self.lineEdit_date = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_date.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.gridLayout.addWidget(self.lineEdit_date, 1, 7, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.lineEdit_index = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_index.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_index.setObjectName("lineEdit_index")
        self.gridLayout.addWidget(self.lineEdit_index, 1, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)
        self.lineEdit_change = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_change.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_change.setObjectName("lineEdit_change")
        self.gridLayout.addWidget(self.lineEdit_change, 1, 3, 1, 1)
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
        self.lineEdit_director = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_director.setStyleSheet("background-color: rgba(255, 255, 255, 148);\n"
"")
        self.lineEdit_director.setObjectName("lineEdit_director")
        self.gridLayout.addWidget(self.lineEdit_director, 1, 2, 1, 1)
        self.pushButton_dobav = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dobav.setGeometry(QtCore.QRect(930, 240, 101, 26))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_dobav.setFont(font)
        self.pushButton_dobav.setObjectName("pushButton_dobav")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(10, 240, 101, 26))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setObjectName("pushButton_Exit")

        self.pushButton_dobav.clicked.connect(self.add)
        self.pushButton_Exit.clicked.connect(self.exit)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 10, 371, 51))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(330, 170, 481, 101))
        self.label_11.setStyleSheet("font: 25 12pt \"URW Bookman\";")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Руководитель</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Изминенеие </p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Описание</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Сроки</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Город</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Индекс</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Улица</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Название</p></body></html>"))
        self.pushButton_dobav.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Назад"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Внесите данные проекта</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Внесите все данные проекта, полсе чего\n"
" данные добавтся в базу данных. Часть этих данных будут\n"
" ведны другим пользователям."))
