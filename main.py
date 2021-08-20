import title
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import game
import thread
import Signup
from PyQt5.QtWidgets import *
import ctypes
class Log_in:
    def __init__(self):
        self.mainwindow = QtWidgets.QMainWindow()
        
        self.ui = title.Ui_MainWindow()
        self.conn=sqlite3.connect('userdata.db')
        self.cur=self.conn.cursor()
        
        self.player=None
        self.ui.pushButton.clicked.connect(self.start)
        
        
    
        
    
    def start(self):
        
        
        self.idvalue=self.ui.lineEdit.text()
        self.pwvalue=self.ui.lineEdit_2.text()
        self.cur.execute ("SELECT * FROM user WHERE id = '" +self.idvalue+"' and password = '"+self.pwvalue+"'")
        self.result=self.cur.fetchall()
        print(self.result)
        if len(self.result)==0:
            QtWidgets.QMessageBox.warning(self.mainwindow, "Warning", "로그인 실패")
        elif len(self.result)!=0:
            print('로그인 성공!')
            self.player=self.idvalue


    def update(self,win):
        self.win=win
        
        if win ==1:
            self.result[0][5]+1
        if win ==2:
            self.result[0][6]+1
        if win ==3:
            pass
            


class Second(object):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.show()
        


        
if __name__ == "__main__":
        
        app = QtWidgets.QApplication(sys.argv)
        main=Log_in()
        
        
       
        sys.exit(app.exec_())
        




        
    
