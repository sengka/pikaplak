# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:44:24 2024

@author: senag
"""
import sys
import sqlite3
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication

# UI dosyalarını ui_code klasöründen al
from ui_code.girisekranıui import *
from ui_code.yoneticiui import *
from ui_code.kullaniciimenuui import *

# Backend kodlarını backend_code klasöründen al
from backend_code.yoneklesil import *
from backend_code.plakeklesil import *
from backend_code.plaksat import *
from backend_code.pikapsatinal import *
from backend_code.plaksatinal import *
from backend_code.pikapsatinalma import *
from backend_code.plaksatinalma import *


###########################################################################################################################
class pikapsatinalma(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_pikapsatinalma()  
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()
        
        #def
        self.ui.btnmenuyedon.clicked.connect(self.MENUDON)
        self.ui.btnsatnal.clicked.connect(self.musteri) 
        self.sqlgenel="SELECT * FROM Plak"
        self.ui.btnmenudon_2.clicked.connect(self.KAPAT)
        
    def MENUDON(self):
        self.hide()
        self.next = kullanekran()
        self.next.show()
        

    def musteri(self):
        isim = self.ui.lnisim.text()
        numara = self.ui.lntlfn.text()
        eposta = self.ui.lnmail.text()
        adres = self.ui.lnadres.text()
        if not isim or not numara or not eposta or not adres:
            QMessageBox.warning(self, "Uyarı", "Butun alanlar doldurulmalıdır.")
            return
        try:
            sql = "INSERT INTO Müşteri (isimsoy, numara,eposta,adres) VALUES (?, ?, ?, ?)"
            parametreler = (isim, numara, eposta, adres)
            self.cursor.execute(sql, parametreler)
            self.conn.commit()
            QMessageBox.information(self, "Bilgi", "Satın alma gerçekleştirildi.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
            
    def KAPAT(self):
        self.close()
        
####################################################################################################################################
class pikpsatinal(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_pikpsatinal()  
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()
        
        #def
        self.ui.btnmenudon.clicked.connect(self.MENUDON)
        self.ui.btnsat.clicked.connect(self.AL)
        self.ui.lnalbumara_2.textChanged.connect(self.ARApikap)
        self.ui.tablo.itemSelectionChanged.connect(self.ID)
        self.ui.btnsat.clicked.connect(self.SAT)
        self.ui.lnpikapid.textChanged.connect(self.BUTON)
        self.sqll="SELECT * FROM pikap"
        self.TABLODAGOSTER(self.sqll)
        self.ui.tablo.clearSelection()  
        self.ui.lnpikapid.clear()       
        self.BUTON() 
        self.ui.btnmenudon_2.clicked.connect(self.KAPAT)
        
    def MENUDON(self):
        self.hide()
        self.next = kullanekran()
        self.next.show()
         
        
    def AL(self):
        self.hide()
        self.next = pikapsatinalma()
        self.next.show()
        
        
    def TABLODAGOSTER(self, sql):
        try:
            result = list(self.cursor.execute(sql))
            rowcount = len(result)

            if rowcount > 0:
                colcount = min(len(result[0]), 3)
                self.ui.tablo.setColumnCount(colcount)

                self.ui.tablo.setRowCount(rowcount)
                for rowindex, rowdata in enumerate(result):
                    for colindex, coldata in enumerate(rowdata[:colcount]):
                        self.ui.tablo.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
                self.ui.tablo.setCurrentCell(0, 0)
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
        self.ui.tablo.clearSelection()  
        self.ui.lnpikapid.clear()       
        self.BUTON() 
        
        
    def ARApikap(self):
        sql="SELECT * FROM pikap WHERE model LIKE'%"+self.ui.lnalbumara_2.text()+"%'"
        self.TABLODAGOSTER(sql)

            
    def ID(self):
        selected_items = self.ui.tablo.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()  
            self.ui.tablo.selectRow(selected_row)
            pikapid_item = self.ui.tablo.item(selected_row, 0)
            if pikapid_item:
                pikapid = pikapid_item.text()
                self.ui.lnpikapid.setText(pikapid)
            else:
                self.ui.lnpikapid.clear()
        else:
          self.ui.lnpikapid.clear()
          
        self.BUTON()
    
    
    def SAT(self):
        idd = self.ui.lnpikapid.text()
        if not idd:
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return
        
        try:
            sql = "DELETE FROM pikap WHERE pikapid = ?"
            parametre = (idd,)
            self.cursor.execute(sql, parametre)
            self.conn.commit()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
        self.ui.tablo.clearSelection()  
        self.ui.lnpikapid.clear()       
        self.BUTON() 
        

    def BUTON(self):
       if not self.ui.lnpikapid.text():
        self.ui.btnsat.setEnabled(False)
       else:
        self.ui.btnsat.setEnabled(True)
        

    def KAPAT(self):
        self.close()
        

########################################################################################################################################
class SATINAL(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_SATINAL()  
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()
        self.ui.btnmenudon_2.clicked.connect(self.KAPAT)
        
        #def
        self.ui.btnmenuyedon.clicked.connect(self.MENUDON)
        self.ui.btnsatnal.clicked.connect(self.musteri)
    
    def MENUDON(self):
        self.hide()
        self.next = kullanekran()
        self.next.show()
        
        
    def musteri(self):
        isim = self.ui.lnisim.text()
        numara = self.ui.lntlfn.text()
        eposta = self.ui.lnmail.text()
        adres = self.ui.lnadres.text()
        if not isim or not numara or not eposta or not adres:
            QMessageBox.warning(self, "Uyarı", "Butun alanlar doldurulmalıdır.")
            return
        try:
            sql = "INSERT INTO Müşteri (isimsoy, numara,eposta,adres) VALUES (?, ?, ?, ?)"
            parametreler = (isim, numara,eposta,adres)
            self.cursor.execute(sql, parametreler)
            self.conn.commit()
            QMessageBox.information(self, "Bilgi", "Satın alma başarılı.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            

    def KAPAT(self):
        self.close()
        
        
##############################################################################################################################
class plaksatinal(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_plaksatinal()  
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()
        self.currow=0  
        
        #def
        self.ui.btndonus.clicked.connect(self.MENUDON)
        self.ui.btnsat.clicked.connect(self.AL)
        self.ui.lnalbumara.textChanged.connect(self.ARA)
        self.ui.tablo.itemSelectionChanged.connect(self.ID)
        self.ui.btnsat.clicked.connect(self.SAT)
        self.ui.lnplakid.textChanged.connect(self.BUTON)
        self.ui.tablo.clearSelection()  
        self.ui.lnplakid.clear()       
        self.BUTON() 
        self.sqlgenel="SELECT * FROM Plak"
        self.TABLODAGOSTER(self.sqlgenel)
        self.ui.btnmenudon_2.clicked.connect(self.KAPAT)
        
        
    def MENUDON(self):
        self.hide()
        self.next = kullanekran()
        self.next.show()
    
    
    def AL(self):
        self.hide()
        self.next = SATINAL()
        self.next.show()
        
        
    def TABLODAGOSTER(self, sql):
        try:
            result = list(self.cursor.execute(sql))
            rowcount = len(result)
        
            if rowcount > 0:
                colcount = min(len(result[0]), 6)  
                self.ui.tablo.setColumnCount(colcount)
            
                self.ui.tablo.setRowCount(rowcount)
                for rowindex, rowdata in enumerate(result):
                    for colindex, coldata in enumerate(rowdata[:colcount]):  
                        self.ui.tablo.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
            
                self.ui.tablo.setCurrentCell(0, 0)  

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
        
        self.ui.tablo.clearSelection()  
        self.ui.lnplakid.clear()        
        self.BUTON() 
    
    
    def ARA(self):
        sql="SELECT * FROM Plak WHERE sanatçı LIKE'%"+self.ui.lnalbumara.text()+"%'"
        sqll="SELECT * FROM Plak WHERE yıl LIKE'%"+self.ui.lnalbumara.text()+"%'"
        sqlll="SELECT * FROM Plak WHERE albumadı LIKE'%"+self.ui.lnalbumara.text()+"%'"
        sqllll="SELECT * FROM Plak WHERE tür LIKE'%"+self.ui.lnalbumara.text()+"%'"
        self.TABLODAGOSTER(sql)
        self.TABLODAGOSTER(sqll)
        self.TABLODAGOSTER(sqlll)
        self.TABLODAGOSTER(sqllll)
        
        
    def ID(self):
        selected_items = self.ui.tablo.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()  
            self.ui.tablo.selectRow(selected_row)
            plakid_item = self.ui.tablo.item(selected_row, 0)
            if plakid_item:
                plakid = plakid_item.text()
                self.ui.lnplakid.setText(plakid)
            else:
                self.ui.lnplakid.clear()
        else:
            self.ui.lnplakid.clear()
            
        self.BUTON()
        
        
    def SAT(self):
        idd = self.ui.lnplakid.text()
        if not idd:
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return
        
        try:
            sql = "DELETE FROM Plak WHERE plakid = ?"
            parametre = (idd,)
            self.cursor.execute(sql, parametre)
            self.conn.commit()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
        self.ui.tablo.clearSelection()  
        self.ui.lnplakid.clear()       
        self.BUTON() 
        

    def BUTON(self):
       if not self.ui.lnplakid.text():
        self.ui.btnsat.setEnabled(False)
       else:
        self.ui.btnsat.setEnabled(True)
        
        
    def KAPAT(self):
        self.close()
        

######################################################################################################################################
class plaksat(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_plaksat()  
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()
        
        #def
        self.ui.btnmenudns.clicked.connect(self.MENUDON)
        self.ui.lnalbumara.textChanged.connect(self.ARA)
        self.ui.lnalbumara_2.textChanged.connect(self.ARApikap)
        self.ui.btnplaksat.clicked.connect(self.SAT)
        self.ui.btnplaksat_2.clicked.connect(self.SATPIK)
        self.ui.tablo.itemSelectionChanged.connect(self.ID)
        self.ui.tablo_2.itemSelectionChanged.connect(self.ID2)
        self.sqlgenel="SELECT * FROM Plak"
        self.currow=0  
        self.TABLODAGOSTER(self.sqlgenel)
        self.sqll="SELECT * FROM pikap"
        self.TABLO2DEGOSTER(self.sqll)
        self.ui.btnmenudon_2.clicked.connect(self.KAPAT)

        
    def MENUDON(self):
        self.hide()
        self.next = yonekran()
        self.next.show()

        
    def TABLODAGOSTER(self, sql):
        try:
            result = list(self.cursor.execute(sql))
            rowcount = len(result)
        
            if rowcount > 0:
                colcount = min(len(result[0]), 6)  
                self.ui.tablo.setColumnCount(colcount)
            
                self.ui.tablo.setRowCount(rowcount)
                for rowindex, rowdata in enumerate(result):
                    for colindex, coldata in enumerate(rowdata[:colcount]):  
                        self.ui.tablo.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
 

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")


    def TABLO2DEGOSTER(self, sql):
        try:
            result = list(self.cursor.execute(sql))
            rowcount = len(result)

            if rowcount > 0:
                colcount = min(len(result[0]), 3)
                self.ui.tablo_2.setColumnCount(colcount)

                self.ui.tablo_2.setRowCount(rowcount)
                for rowindex, rowdata in enumerate(result):
                    for colindex, coldata in enumerate(rowdata[:colcount]):
                        self.ui.tablo_2.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))


        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
            
    def ARA(self):
        sql="SELECT * FROM Plak WHERE sanatçı LIKE'%"+self.ui.lnalbumara.text()+"%'"
        sqll="SELECT * FROM Plak WHERE yıl LIKE'%"+self.ui.lnalbumara.text()+"%'"
        sqlll="SELECT * FROM Plak WHERE albumadı LIKE'%"+self.ui.lnalbumara.text()+"%'"
        sqllll="SELECT * FROM Plak WHERE tür LIKE'%"+self.ui.lnalbumara.text()+"%'"
        self.TABLODAGOSTER(sql)
        self.TABLODAGOSTER(sqll)
        self.TABLODAGOSTER(sqlll)
        self.TABLODAGOSTER(sqllll)
        
        
    def ARApikap(self):
        sql="SELECT * FROM pikap WHERE model LIKE'%"+self.ui.lnalbumara_2.text()+"%'"
        self.TABLO2DEGOSTER(sql)
        
        
    def ID(self):
        selected_items = self.ui.tablo.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()  
            self.ui.tablo.selectRow(selected_row)
            plakid_item = self.ui.tablo.item(selected_row, 0)
            if plakid_item:
                plakid = plakid_item.text()
                self.ui.lnplakad.setText(plakid)
            else:
                self.ui.lnplakad.clear()
        else:
            self.ui.lnplakad.clear()
            
            
    def ID2(self):
        selected_items = self.ui.tablo_2.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()  
            self.ui.tablo_2.selectRow(selected_row)
            pikapid_item = self.ui.tablo_2.item(selected_row, 0)
            if pikapid_item:
                pikapid = pikapid_item.text()
                self.ui.lnpikapad.setText(pikapid)
            else:
                self.ui.lnpikapad.clear()
        else:
            self.ui.lnpikapad.clear()  
    
    
    def SAT(self):
        idd=self.ui.lnplakad.text()
        if not idd:
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return
        
        try:
            sql = "DELETE FROM Plak WHERE plakid= ?"
            parametre= (idd,)
            self.cursor.execute(sql, parametre)
            self.conn.commit()
        
            if self.cursor.rowcount == 0:
                QMessageBox.warning(self, "Uyarı", "Plak stokta bulunmuyor.")
                
            else:
                QMessageBox.information(self, "Bilgi", "Satın alma başarılı.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
            self.TABLODAGOSTER(self.sqlgenel)
            
        
    def SATPIK(self):
        iddpik = self.ui.lnpikapad.text()
        if not iddpik:
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return

        try:
            sql = "DELETE FROM pikap WHERE pikapid = ?"
            parametre = (iddpik,)  
            self.cursor.execute(sql, parametre)
            self.conn.commit()

            if self.cursor.rowcount == 0:
                QMessageBox.warning(self, "Uyarı", "Pikap stokta bulunmuyor.")           
            else:
                QMessageBox.information(self, "Bilgi", "Satın alma başarılı.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")

            self.TABLO2DEGOSTER(self.sqlgenel)
            
            
    def KAPAT(self):
        self.close()
        
            
############################################################################################################################33
class plakeklesil(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_plakeklesil() 
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()

        
        #def
        self.ui.btnmenudon.clicked.connect(self.MENUDON)
        self.ui.btnplkolstr.clicked.connect(self.PLAKOLUSTUR)
        self.ui.btnplksil.clicked.connect(self.PLAKSIL)
        self.ui.btnpikapolustur.clicked.connect(self.PIKAPOLUSTUR)
        self.ui.btnpikapsil.clicked.connect(self.PIKAPSIL)
        self.ui.tablo.itemSelectionChanged.connect(self.PLAKTAGOSTER)
        self.ui.tablo_2.itemSelectionChanged.connect(self.PIKAPTAGOSTER)
        self.ui.btnmenudon_2.clicked.connect(self.KAPAT)
        self.ui.btnduzenle.clicked.connect(self.DUZELT)
        self.ui.btnduzenle_2.clicked.connect(self.DUZELTPIK)
        self.sqlgenel="SELECT * FROM Plak"
        self.currow=0  
        self.TABLODAGOSTER(self.sqlgenel)
        self.sqll="SELECT * FROM pikap"
        self.TABLO2DEGOSTER(self.sqll)
    
    
    def MENUDON(self):
        self.hide()
        self.next = yonekran()
        self.next.show()


    def PLAKOLUSTUR(self):
        plak_adı = self.ui.lnplkad.text()
        sanatci_adi = self.ui.lnplksntc.text()
        tur = self.ui.lnplktur.text()
        plak_yil = self.ui.lnplkyl.text()
        plakfiyat = self.ui.lnplkfyt.text()

        if not plak_adı or not sanatci_adi or not tur or not plak_yil or not plakfiyat:
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return
        try:
            sql = "INSERT INTO Plak (sanatçı,albumadı, tür, yıl, fiyat) VALUES (?, ?, ?, ?, ?)"
            parametreler = (plak_adı, sanatci_adi, tur, plak_yil, plakfiyat)
            self.cursor.execute(sql, parametreler)
            self.conn.commit()
            QMessageBox.information(self, "Bilgi", "Plak başarıyla eklendi.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
            self.TABLODAGOSTER(self.sqlgenel)
            
            
    def PLAKSIL(self):
        sanatcı = self.ui.lnplkadsil.text()
        ad = self.ui.lnplksntcsil.text()
        tur = self.ui.lnplktursil.text()
        plak_yil = self.ui.lnplakylsil.text()
        plakfiyat = self.ui.lnplkttur.text()

        if not sanatcı or not ad or not tur or not plak_yil or not plakfiyat:
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return

        try:
            sql = "DELETE FROM Plak WHERE sanatçı = ? AND albumadı = ? AND tür = ? AND yıl = ? AND fiyat = ?"
            parametreler = (sanatcı, ad, tur, plak_yil, plakfiyat)
            self.cursor.execute(sql, parametreler)
            self.conn.commit()
        
            if self.cursor.rowcount == 0:
                QMessageBox.warning(self, "Uyarı", "Silinecek plak bulunamadı.")
            else:
                    QMessageBox.information(self, "Bilgi", "Plak başarıyla silindi.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
        self.TABLODAGOSTER(self.sqlgenel)
        
        
    def PIKAPOLUSTUR(self):
        pikap_adı=self.ui.lnpikapad.text()
        fiyat=self.ui.lnpikapfiyat.text()
        if not pikap_adı or not fiyat:
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return
        try:
            sql = "INSERT INTO pikap (model, fiyat) VALUES (?, ?)"
            parametreler = (pikap_adı,fiyat)
            self.cursor.execute(sql, parametreler)
            self.conn.commit()
            QMessageBox.information(self, "Bilgi", "Pikap başarıyla eklendi.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
        
        self.TABLO2DEGOSTER(self.sqll)
    
    
    def PIKAPSIL(self):
        pikap_adı=self.ui.lnpikapadsil.text()
        fiyat=self.ui.lnpikapfiyatsil.text()

        if not pikap_adı or not fiyat :
            QMessageBox.warning(self, "Uyarı", "Tüm alanlar doldurulmalıdır.")
            return
        try:
            sql = "DELETE FROM pikap WHERE model = ? AND fiyat = ?"
            parametreler = (pikap_adı, fiyat)
            self.cursor.execute(sql, parametreler)
            self.conn.commit()
        
            if self.cursor.rowcount == 0:
                QMessageBox.warning(self, "Uyarı", "Silinecek plak bulunamadı.")
            else:
                    QMessageBox.information(self, "Bilgi", "Pikap başarıyla silindi.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
        
        self.TABLO2DEGOSTER(self.sqll)
            
        
    def TABLODAGOSTER(self, sql):
        try:
            result = list(self.cursor.execute(sql))
            rowcount = len(result)
        
            if rowcount > 0:
                colcount = min(len(result[0]), 6)  
                self.ui.tablo.setColumnCount(colcount)
            
                self.ui.tablo.setRowCount(rowcount)
                for rowindex, rowdata in enumerate(result):
                    for colindex, coldata in enumerate(rowdata[:colcount]):  
                        self.ui.tablo.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")


    def TABLO2DEGOSTER(self, sql):
        try:
            result = list(self.cursor.execute(sql))
            rowcount = len(result)

            if rowcount > 0:
                colcount = min(len(result[0]), 3)
                self.ui.tablo_2.setColumnCount(colcount)

                self.ui.tablo_2.setRowCount(rowcount)
                for rowindex, rowdata in enumerate(result):
                    for colindex, coldata in enumerate(rowdata[:colcount]):
                        self.ui.tablo_2.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
            
            
    def PLAKTAGOSTER(self):
        selected_rows = self.ui.tablo.selectedItems()
        if selected_rows:
            plak_adı = self.ui.tablo.item(selected_rows[0].row(), 1).text()
            sanatci_adi = self.ui.tablo.item(selected_rows[0].row(), 2).text()
            tur = self.ui.tablo.item(selected_rows[0].row(), 3).text()
            plak_yil = self.ui.tablo.item(selected_rows[0].row(), 4).text()
            plak_fiyat = self.ui.tablo.item(selected_rows[0].row(), 5).text()

            self.ui.lnplkadsil.setText(plak_adı)
            self.ui.lnplksntcsil.setText(sanatci_adi)
            self.ui.lnplktursil.setText(tur)
            self.ui.lnplakylsil.setText(plak_yil)
            self.ui.lnplkttur.setText(plak_fiyat)
        else:
            QMessageBox.warning(self, "Uyarı", "Düzenlenecek bir plak seçilmedi.")
            
            
    def PIKAPTAGOSTER (self):
        selected_rows = self.ui.tablo_2.selectedItems()
        if selected_rows:
            pikap_adı = self.ui.tablo_2.item(selected_rows[0].row(), 1).text()
            fiyat = self.ui.tablo_2.item(selected_rows[0].row(), 2).text()

            self.ui.lnpikapadsil.setText(pikap_adı)
            self.ui.lnpikapfiyatsil.setText(fiyat)

        else:
            QMessageBox.warning(self, "Uyarı", "Düzenlenecek bir plak seçilmedi.")
            
            
    def DUZELT(self):
        selected_rows = self.ui.tablo.selectedItems()  
        if selected_rows:  
            sanatci = self.ui.tablo.item(selected_rows[0].row(), 1).text()
            plakadi = self.ui.tablo.item(selected_rows[0].row(), 2).text()
            tur = self.ui.tablo.item(selected_rows[0].row(), 3).text()
            yil = self.ui.tablo.item(selected_rows[0].row(), 4).text()
            fiyat = self.ui.tablo.item(selected_rows[0].row(), 5).text()

            _sanatci = self.ui.lnplkadsil.text()
            _plak = self.ui.lnplksntcsil.text()
            _tur = self.ui.lnplktursil.text()
            _plak_yil = self.ui.lnplakylsil.text()
            _plak_fiyat = self.ui.lnplkttur.text()
        
            try:

                sql = "UPDATE Plak SET sanatçı=?, albumadı=?, tür=?, yıl=?, fiyat=? WHERE sanatçı=? AND albumadı=? AND tür=? AND yıl=? AND fiyat=?"
            
                parameters = (_sanatci, _plak, _tur, _plak_yil, _plak_fiyat, sanatci, plakadi, tur, yil, fiyat)
                self.cursor.execute(sql, parameters)
                self.conn.commit()
                QMessageBox.information(self, "Bilgi", "Plak başarıyla güncellendi.")

                self.TABLODAGOSTER(self.sqlgenel)
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
        else:
            QMessageBox.warning(self, "Uyarı", "Düzeltilmek istenen bir plak seçilmedi.")
            
            
    def DUZELTPIK(self):
        selected_rows = self.ui.tablo_2.selectedItems()
        if selected_rows:
            pikap_adı = self.ui.tablo_2.item(selected_rows[0].row(), 1).text()
            fiyatı = self.ui.tablo_2.item(selected_rows[0].row(), 2).text()

            adı = self.ui.lnpikapadsil.text()
            fiyat = self.ui.lnpikapfiyatsil.text()

            try:
                sql = "UPDATE pikap SET model=?,  fiyat=? WHERE model=? AND fiyat=?"  
                parameters = (adı,fiyat,pikap_adı,fiyatı)  
                self.cursor.execute(sql, parameters)
                self.conn.commit()
  
                QMessageBox.information(self, "Bilgi", "Pikap başarıyla güncellendi.")
                self.TABLO2DEGOSTER(self.sqll)
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
        else:   
            QMessageBox.warning(self, "Uyarı", "Düzeltilmek istenen bir plak seçilmedi.")


    def KAPAT(self):
        self.close()

                   
#################################################################################################################################
class yoneklesil(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_yoneklesil()  
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()
        
        #def
        self.ui.btnolustur.clicked.connect(self.YONEKLE)
        self.ui.btnsil.clicked.connect(self.YONSIL)
        self.ui.btnolustur.clicked.connect(self.YONEKLE)
        self.ui.btnsil.clicked.connect(self.YONSIL)
        self.ui.btnmenuyedon.clicked.connect(self.MENUDON)
        self.sqlgenel="SELECT * FROM yonetici"
        self.currow=0  
        self.TABLODAGOSTER(self.sqlgenel)
        self.ui.CIKKK.clicked.connect(self.KAPAT)
        self.ui.tablo.clearSelection()  
        
    def YONEKLE(self):
        kullanıcı_adı = self.ui.lneklekullan.text()
        sifre = self.ui.lneklesifr.text()
        if not kullanıcı_adı or not sifre:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı adı ve şifre boş bırakılamaz.")
            return
        self.cursor.execute("SELECT * FROM yonetici WHERE kullanad = ?", (kullanıcı_adı,))
        mevcut_kullanıcı = self.cursor.fetchone()

        if mevcut_kullanıcı:
                QMessageBox.warning(self, "Uyarı", "Bu kullanıcı adı zaten mevcut.")
        else:
            try:
                sql = "INSERT INTO yonetici (kullanad, sifre) VALUES (?, ?)"
                parametreler = (kullanıcı_adı, sifre)
                self.cursor.execute(sql, parametreler)
                self.conn.commit()
                QMessageBox.information(self, "Bilgi", "Kullanıcı başarıyla eklendi.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
        
        self.TABLODAGOSTER(self.sqlgenel)
        
                
    def YONSIL(self):
        kullanıcı_adı = self.ui.lnsilkullan.text()
        if not kullanıcı_adı:
            QMessageBox.warning(self, "Uyarı", "Silinecek kullanıcı adını girin.")
            return

        try:
            self.cursor.execute("SELECT * FROM yonetici WHERE kullanad = ?", (kullanıcı_adı,))
            mevcut_kullanıcı = self.cursor.fetchone()

            if not mevcut_kullanıcı:
                QMessageBox.warning(self, "Uyarı", "Bu kullanıcı adı bulunamadı.")
            else:
                self.cursor.execute("DELETE FROM yonetici WHERE kullanad = ?", (kullanıcı_adı,))
                self.conn.commit()
                QMessageBox.information(self, "Bilgi", "Kullanıcı başarıyla silindi.")
        except sqlite3.Error as e:
                    QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
                    
        self.TABLODAGOSTER(self.sqlgenel)
        
    
    def MENUDON(self):
        self.hide()
        self.next = yonekran()
        self.next.show()
    
    
    def TABLODAGOSTER(self,sql):
        try:
            result = list(self.cursor.execute(sql))
            rowcount = len(result)
            self.ui.tablo.setRowCount(rowcount)
            self.ui.tablo.setColumnCount(2)  
            for rowindex, rowdata in enumerate(result):
                for colindex, coldata in enumerate(rowdata[1:], start=0):  
                    self.ui.tablo.setItem(rowindex, colindex, QTableWidgetItem(str(coldata)))
                if rowcount > 0:
                    self.ui.tablo.setCurrentCell(0, 0)  
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
        self.ui.tablo.clearSelection()  
        

    def KAPAT(self):
        self.close()
        

##################################################################################################################       
class yonekran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_yonekran()
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()

        #def
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
        
        
#########################################################################################################################
class kullanekran(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_kullanekran()
        self.ui.setupUi(self)
        
        #def
        self.ui.btnplakekle.clicked.connect(self.PIKAPSATINAL)
        self.ui.btnyntekle.clicked.connect(self.PLAKSATINAL)
        
    def PIKAPSATINAL(self):
        self.hide()
        self.next = pikpsatinal()
        self.next.show()
            
        
    def PLAKSATINAL(self):
        self.hide()
        self.next = plaksatinal ()
        self.next.show()
        

########################################################################################################################
class Giris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Giris()
        self.ui.setupUi(self)
        self.conn = sqlite3.connect("plakdb.db")
        self.cursor = self.conn.cursor()

        #def
        self.ui.btnolstr.clicked.connect(self.OLUSTUR)
        self.ui.btnkullncgrs.clicked.connect(self.KULLANICI_GIRIS)  
        self.ui.btnyontcgrs.clicked.connect(self.YONETICI_GIRIS)

    def OLUSTUR(self):
        kullanıcı_adı = self.ui.lnkllcadgrs.text()
        sifre = self.ui.lnkllcsfrgrs.text()
        if not kullanıcı_adı or not sifre:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı adı ve şifre boş bırakılamaz.")
            return
        self.cursor.execute("SELECT * FROM Kullanıcı WHERE kullanıcıadı = ?", (kullanıcı_adı,))
        mevcut_kullanıcı = self.cursor.fetchone()

        if mevcut_kullanıcı:
            QMessageBox.warning(self, "Uyarı", "Bu kullanıcı adı zaten mevcut.")
        else:
            try:
                sql = "INSERT INTO Kullanıcı (kullanıcıadı, sifre) VALUES (?, ?)"
                parametreler = (kullanıcı_adı, sifre)
                self.cursor.execute(sql, parametreler)
                self.conn.commit()
                QMessageBox.information(self, "Bilgi", "Kullanıcı başarıyla eklendi.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")
                

    def KULLANICI_GIRIS(self):
        kullanıcı_adı = self.ui.lnkllncadgrs.text()
        sifre = self.ui.lnkllncsfrgrs.text()
        if not kullanıcı_adı or not sifre:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı adı ve şifre boş bırakılamaz.")
            return

        self.cursor.execute("SELECT * FROM Kullanıcı WHERE kullanıcıadı = ? AND sifre = ?", (kullanıcı_adı, sifre))
        kullanıcı = self.cursor.fetchone()
        if kullanıcı:
            self.hide()
            self.sonraki = kullanekran()
            self.sonraki.show()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış.")


    def YONETICI_GIRIS(self):
        kullanıcı_adı = self.ui.lnyntckulladgrs.text()
        sifre = self.ui.lnyntcsfrgrs.text()
        if not kullanıcı_adı or not sifre:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı adı ve şifre boş bırakılamaz.")
            return

        self.cursor.execute("SELECT * FROM yonetici WHERE kullanad = ? AND sifre = ?", (kullanıcı_adı, sifre))
        kullanad = self.cursor.fetchone()

        if kullanad:
            self.hide()
            self.next = yonekran()
            self.next.show()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış.")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ana_pencere = Giris()
    ana_pencere.show()
    sys.exit(app.exec_())
    
    
    
    
