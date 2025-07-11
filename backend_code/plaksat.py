# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:02:41 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import *
from ui_code.plaksatui import *
class plaksat(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_plaksat()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = plaksat()  
    ana_pencere.show()
    sys.exit(app.exec_())
