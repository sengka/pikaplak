import sys
from PyQt5.QtWidgets import QApplication
from backend_code.girisekrani import GirisEkrani  # senin oluşturduğun giriş ekranı sınıfı

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GirisEkrani()
    pencere.show()
    sys.exit(app.exec_())

