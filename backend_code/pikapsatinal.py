# -*- coding: utf-8 -*-
"""
Created on Sun May 26 13:19:48 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import *
from ui_code.pikapsatinalui import *
class pikpsatinal(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_pikpsatinal()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = pikpsatinal()    
    ana_pencere.show()
    sys.exit(app.exec_())
