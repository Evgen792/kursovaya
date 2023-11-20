

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Captcha(QMainWindow):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 190)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(199, 179, 151);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.label.setObjectName("label")
        self.label_Kapcha = QtWidgets.QLabel(self.centralwidget)
        self.label_Kapcha.setGeometry(QtCore.QRect(140, 10, 71, 18))
        font = QtGui.QFont()
        font.setFamily("MathJax_Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(True)
        self.label_Kapcha.setFont(font)
        self.label_Kapcha.setMouseTracking(False)
        self.label_Kapcha.setText("")
        self.label_Kapcha.setObjectName("label_Kapcha")
        self.lineEdit_kapcha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kapcha.setGeometry(QtCore.QRect(80, 50, 113, 26))
        font = QtGui.QFont()
        font.setFamily("MathJax_Script")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_kapcha.setFont(font)
        self.lineEdit_kapcha.setObjectName("lineEdit_kapcha")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 140, 101, 26))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_Time = QtWidgets.QLabel(self.centralwidget)
        self.label_Time.setGeometry(QtCore.QRect(110, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Time.setFont(font)
        self.label_Time.setObjectName("label_Time")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Введите капчу:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Проверить"))
        self.label_Time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))