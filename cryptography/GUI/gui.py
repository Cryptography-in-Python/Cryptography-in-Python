# -*- coding: utf-8 -*-

from ..sha1 import sha1
from ..MD5 import cryptography_md5
from ..RSA import cryptography_rsa
from ..AES import aes
from ..VIG import cryptography_vigenere
from PyQt5.QtWidgets import QWidget,QLabel, QPushButton,QComboBox,QApplication,QPlainTextEdit,QFileDialog, QMainWindow, QApplication,QVBoxLayout,QTabWidget,QHBoxLayout,QSpacerItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

import sys
import os
sys.path.append(os.path.abspath('../AES'))

INITIAL_WIDTH = 800
INITIAL_HEIGHT= 600

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title  = 'Cryptography project -- Group 7'
        self.left   = 0
        self.top    = 0
        self.width  = INITIAL_WIDTH
        self.height = INITIAL_HEIGHT
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
 
        self.show()
        
class MyTableWidget(QWidget):        
 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabAES = QWidget()	
        self.tabDES = QWidget()
        self.tabMD5 = QWidget()
        self.tabRSA = QWidget()
        self.tabSHA = QWidget()
        self.tabVIG = QWidget()
            
        self.tabs.resize(INITIAL_WIDTH,INITIAL_HEIGHT) 
 
        # Add tabs
        self.tabs.addTab(self.tabAES,"AES")
        self.tabs.addTab(self.tabDES,"DES")
        self.tabs.addTab(self.tabMD5,"MD5")
        self.tabs.addTab(self.tabRSA,"RSA")
        self.tabs.addTab(self.tabSHA,"SHA1")
        self.tabs.addTab(self.tabVIG,"VIG")
 
        # Create first tab
        self.tabAES.layout = QVBoxLayout(self)
        
        self.labelAESKey      = QLabel("Key:",self)
        self.labelAESPlain    = QLabel("Plain Text:",self)
        self.labelAESCypher   = QLabel("Cypther Text:",self)
        self.buttonAESEncrypt = QPushButton("Encrypt",self)
        self.buttonAESDecrypt = QPushButton("Decrypt",self)
        self.textAESPlain     = QPlainTextEdit(self)
        self.textAESCypher    = QPlainTextEdit(self)
        self.textAESKey       = QPlainTextEdit(self)
        
        
        self.layoutAESButton = QVBoxLayout()
        self.layoutAESButton.addStretch()
        self.layoutAESButton.addWidget(self.buttonAESEncrypt)
        self.layoutAESButton.addStretch()
        self.layoutAESButton.addWidget(self.buttonAESDecrypt)
        self.layoutAESButton.addStretch()
        
        self.layoutAESLeft = QVBoxLayout()
        self.layoutAESLeft.addWidget(self.labelAESPlain)
        self.layoutAESLeft.addWidget(self.textAESPlain)
        
        self.layoutAESRight = QVBoxLayout()
        self.layoutAESRight.addWidget(self.labelAESCypher)
        self.layoutAESRight.addWidget(self.textAESCypher)
        
        self.layoutAESText = QHBoxLayout()
        self.layoutAESText.addLayout(self.layoutAESLeft)
        self.layoutAESText.addLayout(self.layoutAESButton)
        self.layoutAESText.addLayout(self.layoutAESRight)
        
        
        self.layoutAESKey = QHBoxLayout()
        self.layoutAESKey.addWidget(self.labelAESKey)
        self.layoutAESKey.addWidget(self.textAESKey)
        
        self.layoutAES = QVBoxLayout()
        self.layoutAES.addLayout(self.layoutAESKey)
        self.layoutAES.addLayout(self.layoutAESText)
        
        
        self.tabAES.setLayout(self.layoutAES)
        self.textAESKey.setFixedHeight(40) 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
