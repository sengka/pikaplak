# -*- coding: utf-8 -*-
"""
Created on Sun May 26 13:26:51 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import *
from ui_code.plaksatinalmauiui import *
class SATINAL(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_SATINAL()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = SATINAL()  
    ana_pencere.show()
    sys.exit(app.exec_())