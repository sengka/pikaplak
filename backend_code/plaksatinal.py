# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:07:25 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import *
from ui_code.plaksatinalui import *
class plaksatinal(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_plaksatinal()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = plaksatinal()  
    ana_pencere.show()
    sys.exit(app.exec_())