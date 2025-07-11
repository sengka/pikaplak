# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:27:06 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from plakgorui import *  
class plakgor(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_plakgor()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = plakgor()  
    ana_pencere.show()
    sys.exit(app.exec_())
