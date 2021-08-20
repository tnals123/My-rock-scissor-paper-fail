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
import random

import sqlite3
class Enemy(QThread):
    def __init__(self,parent,gui,label):
        QThread.__init__(self, parent)
       
        self.gui=gui
        self.label=label
        self.conn=sqlite3.connect('userdata.db')
        self.cur=self.conn.cursor()
        
        
        
    def run(self):
        
        for q in range(1,3):
            for i in range(1,4):
                if i==1:   
                    self.gui.setPixmap(QtGui.QPixmap('rock2.png'))
                        
                elif i==2:
                    self.gui.setPixmap(QtGui.QPixmap('scissor2.png'))
                
                elif i==3:
                    self.gui.setPixmap(QtGui.QPixmap('paper2.png'))
              
                time.sleep(0.25)
        self.ran=random.randint(1,3)


        _translate = QtCore.QCoreApplication.translate
        if self.ran==1:
            self.gui.setPixmap(QtGui.QPixmap('rock2.png'))
            if self.rival==1:
                self.label.setText(_translate("MainWindow", "패배했습니다."))
                
            if self.rival==2:
                self.label.setText(_translate("MainWindow", "비겼습니다.."))
                
            if self.rival==3:
                self.label.setText(_translate("MainWindow", "승리했습니다!."))
                
        elif self.ran==2:
            self.gui.setPixmap(QtGui.QPixmap('scissor2.png'))
            if self.rival==1:
                self.label.setText(_translate("MainWindow", "비겼습니다."))
                
            if self.rival==2:
                self.label.setText(_translate("MainWindow", "승리했습니다!"))
                
            if self.rival==3:
                self.label.setText(_translate("MainWindow", "패배했습니다."))
                
                    
        elif self.ran==3:
            self.gui.setPixmap(QtGui.QPixmap('paper2.png'))
            if self.rival==1:
                self.label.setText(_translate("MainWindow", "승리했습니다!"))
            if self.rival==2:
                self.label.setText(_translate("MainWindow", "패배했습니다.."))
            if self.rival==3:
                self.label.setText(_translate("MainWindow", "비겼습니다."))

    def game(self,rival):
        self.rival=rival
        
        

            

            



