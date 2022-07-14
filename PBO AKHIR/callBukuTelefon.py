from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from matplotlib.pyplot import margins 
from Novi_BukuTelephone import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection.py')
os.system('python CreateTable.py')

global id, namalengkap, prodi, kota, telefon, email

# Users (id INT, Nama lengkap TEXT, Prodi TEXT, Kota TEXT, Telefon TEXT, Email TEXT)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.btnDaftarClick()
        self.ui.btnDaftar.clicked.connect(self.btnDaftarClick)
        self.ui.btnMenyimpan.clicked.connect(self.btnMenyimpanClick)
        self.ui.btnMenghapus.clicked.connect(self.btnMenghapusClick)
        self.ui.btnMemperbarui.clicked.connect(self.btnMemperbaruiClick)
        self.ui.tblDaftar.clicked.connect(self.ListOnClick) 
 
    def btnClear(self):
        self.ui.txtID.clear()
        self.ui.txtNamaLengkap.clear()
        self.ui.txtProdi.clear()
        self.ui.txtKota.clear()
        self.ui.txtTelefon.clear()
        self.ui.txtEmail.clear()

    def ListOnClick(self): 
        self.ui.txtID.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 0).text())
        self.ui.txtNamaLengkap.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 1).text())
        self.ui.txtProdi.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 2).text())
        self.ui.txtKota.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 3).text())
        self.ui.txtTelefon.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 4).text())
        self.ui.txtEmail.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 5).text())
 
    def btnMenyimpanClick(self): 
        id = self.ui.txtID.text()
        namalengkap = self.ui.txtNamaLengkap.text()
        Prodi = self.ui.txtProdi.text()
        kota = self.ui.txtKota.text()
        telefon = self.ui.txtTelefon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("Novi_BukuTelephone.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO Users VALUES (?,?,?,?,?,?)",(id,namalengkap,Prodi,kota,telefon,email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is added successfully to the database.')
        except Exception:
            print('Error', 'Could not add student to the database.')
        
        self.btnClear()
        self.btnDaftarClick()

    def btnDaftarClick(self):  
        self.ui.tblDaftar.clear()
        self.ui.tblDaftar.setColumnCount(6)
        self.ui.tblDaftar.setHorizontalHeaderLabels(('ID','Nama Lengkap','Prodi','Kota','Telefon','Email'))
        self.ui.tblDaftar.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('Novi_BukuTelephone.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM Users"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tblDaftar.setRowCount(len(rows))
        
        for rowIndeks, rowData in enumerate(rows):
            for columnIndeks, columnData in enumerate (rowData):
                self.ui.tblDaftar.setItem(rowIndeks,columnIndeks,QTableWidgetItem(str(columnData))) 
    
    def btnMemperbaruiClick(self):  
        id = self.ui.txtID.text()
        namalengkap = self.ui.txtNamaLengkap.text()
        Prodi = self.ui.txtProdi.text()
        kota = self.ui.txtKota.text()
        telefon = self.ui.txtTelefon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("Novi_BukuTelephone.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE Users SET namalengkap = ?, Prodi = ?, kota = ?, \
                telefon = ?, email = ? WHERE id = ?",(namalengkap,Prodi,kota,telefon,email,id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is updated successfully to the database.')
        except Exception:
            print('Error', 'Could not update student to the database.')

        self.btnClear()
        self.btnDaftarClick()

    def btnMenghapusClick(self): 
        id = self.ui.txtID.text() 

        try:
            self.conn = sql.connect("Novi_BukuTelephone.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM Users WHERE id = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is deleted successfully from the database.')
        except Exception:
            print('Error', 'Could not delete student to the database.')
        
        self.btnClear()
        self.btnDaftarClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()