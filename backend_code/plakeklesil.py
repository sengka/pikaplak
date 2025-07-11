# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:29:46 2024

@author: senag
"""


import sys
from PyQt5.QtWidgets import *
from ui_code.plakeklesilui import *
class plakeklesil(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_plakeklesil()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = plakeklesil()  
    ana_pencere.show()
    sys.exit(app.exec_())
