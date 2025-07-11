# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:49:25 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import *
from kullaniciimenuui import *

class Giris(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_kullanekran()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = Giris()  
    ana_pencere.show()
    sys.exit(app.exec_())
