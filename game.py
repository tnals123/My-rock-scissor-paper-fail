
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
import thread
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtTest
import time


    

class Game(object):
    
    def __init__(self,parent=None):
        
        self.mainWindow = QtWidgets.QMainWindow()
        
        self.setupUi()
        
        self.asdf=thread.Enemy(parent,gui=self.label,label=self.label12)
        
        
    def gamestart(self,my):
        self.asdf.game(my)

        
        
    def show(self):
        self.mainWindow.show()
    

    def setupUi(self):
        self.vs=QPixmap('vs.jpg')
        self.vs=self.vs.scaledToWidth(100)
        self.vs=self.vs.scaledToHeight(98)


        self.rock = QPixmap('rock.png')
        self.rock=self.rock.scaledToHeight(130)
        self.rock=self.rock.scaledToWidth(130)
        
        
        self.scissor = QPixmap('sissor.png')
        self.scissor=self.scissor.scaledToHeight(130)
        self.scissor=self.scissor.scaledToWidth(130)

        self.paper = QPixmap('paper.png')
        self.paper=self.paper.scaledToHeight(130)
        self.paper=self.paper.scaledToWidth(130)

        self.enemyrock=QPixmap('rock2.png')
        self.enemyscissor=QPixmap('scissor2.png')
        self.enmeypaper=QPixmap('paper2.png')
        

        self.mainWindow.setObjectName("MainWindow")
        self.mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label12 = QtWidgets.QLabel(self.centralwidget)
        self.label12.setGeometry(QtCore.QRect(400, 300, 93, 28))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 40, 251, 241))
        self.label.setStyleSheet("background:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 251, 241))
        self.label_2.setStyleSheet("background:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 110, 91, 101))
        self.label_3.setStyleSheet("background:white;")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 520, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 520, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 350, 131, 121))
        self.label_4.setStyleSheet("background:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 350, 131, 121))
        self.label_5.setStyleSheet("background:white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 350, 131, 121))
        self.label_6.setStyleSheet("background:white;")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 480, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 480, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 480, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.mainWindow)
        self.statusbar.setObjectName("statusbar")
        self.mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", ""))
        self.label12.setText(_translate("MainWindow", ""))
        
        
        self.label_2.setText(_translate("MainWindow", ""))
        

        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setPixmap(self.vs)
        self.pushButton_4.setText(_translate("MainWindow", "내 정보 보기"))
        self.pushButton_5.setText(_translate("MainWindow", "랭킹 보기"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setPixmap(self.scissor)
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setPixmap(self.rock)
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setPixmap(self.paper)
        self.pushButton.setText(_translate("MainWindow", "가위!"))
        self.pushButton.clicked.connect(self.myscissor)
        self.pushButton_2.setText(_translate("MainWindow", "바위!"))
        self.pushButton_2.clicked.connect(self.myrock)
        self.pushButton_3.setText(_translate("MainWindow", "보!"))
        self.pushButton_3.clicked.connect(self.mypaper)

    def myscissor(self):
        self.asdf.start()
        self.label_2.setPixmap(QtGui.QPixmap('scissor3.png'))
        self.gamestart(1)
        
    def myrock(self):
        self.asdf.start()
        self.label_2.setPixmap(QtGui.QPixmap('rock3.png'))
        self.gamestart(2)
        
    def mypaper(self):
        self.asdf.start()
        self.label_2.setPixmap(QtGui.QPixmap('paper3.png'))
        self.gamestart(3)
        


if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    qpalzm=Game()
    qpalzm.show()
    sys.exit(app.exec_())
