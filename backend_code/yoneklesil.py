# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:01:43 2024

@author: senag
"""

import sys
from PyQt5.QtWidgets import *
from ui_code.yoneklesilui import *
class yoneklesil(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_yoneklesil()  
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = yoneklesil()  
    ana_pencere.show()
    sys.exit(app.exec_())