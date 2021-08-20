
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import sqlite3
from PyQt5.QtGui import QPixmap
import Signup
import game
class Ui_MainWindow(object):
    def __init__(self):
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi()
        
       
        self.show()
      
    def show(self):
        self.MainWindow.show()   
    def setupUi(self):
        self.pixmap = QPixmap('download.png')
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(728, 431)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.first=QtWidgets.QStackedWidget(self.centralwidget)

        
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 80, 261, 191))
        self.groupBox.setStyleSheet("background-color: Lightgrey;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 50, 161, 21))
        self.lineEdit.setStyleSheet("background-color:White;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 100, 161, 21))
        self.lineEdit_2.setStyleSheet("background-color:White;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 64, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 150, 121, 28))
        self.pushButton.setStyleSheet("background-color:Lightgreen;\n"
"color:White;\n"
"border-radius:5px;\n"
"border:1px solid green;")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 240, 190))
        self.label_3.setStyleSheet("background-color:White;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(self.pixmap)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 221, 31))
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 310, 121, 28))
        self.pushButton_2.setStyleSheet("background-color:White;\n"
"color:Black;\n"
"border-radius:5px;\n"
"border:1px solid green;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 26))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

       

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "로그인!"))
        self.label_4.setText(_translate("MainWindow", "가위바위보 게임!"))
        self.label_4.setFont(QtGui.QFont("궁서",18))
        self.pushButton_2.setText(_translate("MainWindow", "계정 만들기"))
        
        self.pushButton.clicked.connect(self.asdf)
    def asdf(self):
        return self.lineEdit.text()
    
    
        




