# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:06:19 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import *
from yoneticiui import *
import sqlite3
from yoneklesil import *
from plakeklesil import *
from plaksat import *

class yonekran(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_yonekran()  
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()
    
        self.ui.btnyntekle.clicked.connect(self.YONETEKLE)
        self.ui.btnsat.clicked.connect(self.PLAKSAT)
        self.ui.btnplakekle.clicked.connect(self.PLAKEKLE)
        
    def YONETEKLE(self):
        self.hide()
        self.next = yoneklesil()
        self.next.show()
        
    def PLAKSAT(self):
        self.hide()
        self.next = plaksat ()
        self.next.show()
        
    def PLAKEKLE(self):
        self.hide()
        self.next = plakeklesil ()
        self.next.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = yonekran() 
    ana_pencere.show()
    sys.exit(app.exec_())
