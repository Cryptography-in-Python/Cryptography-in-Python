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
 
        # Create AES tab
        
        self.labelAESKey      = QLabel("Key:",self)
        self.labelAESPlain    = QLabel("Plain Text:",self)
        self.labelAESCypher   = QLabel("Cipher Text:",self)
        self.buttonAESEncrypt = QPushButton("Encrypt",self)
        self.buttonAESDecrypt = QPushButton("Decrypt",self)
        self.textAESPlain     = QPlainTextEdit(self)
        self.textAESCypher    = QPlainTextEdit(self)
        self.textAESKey       = QPlainTextEdit(self)
        self.comboAESMode     = QComboBox(self)
        
        self.comboAESMode.addItem("OFB")
        self.comboAESMode.addItem("CFB")
        self.comboAESMode.addItem("CBC")
        
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
        self.layoutAESKey.addWidget(self.comboAESMode)
        
        self.layoutAES = QVBoxLayout()
        self.layoutAES.addLayout(self.layoutAESKey)
        self.layoutAES.addLayout(self.layoutAESText)
        
        self.tabAES.setLayout(self.layoutAES)
        self.textAESKey.setFixedHeight(40) 
        
        # Create DES tab
        
        self.labelDESKey      = QLabel("Key:",self)
        self.labelDESPlain    = QLabel("Plain Text:",self)
        self.labelDESCypher   = QLabel("Cipher Text:",self)
        self.buttonDESEncrypt = QPushButton("Encrypt",self)
        self.buttonDESDecrypt = QPushButton("Decrypt",self)
        self.textDESPlain     = QPlainTextEdit(self)
        self.textDESCypher    = QPlainTextEdit(self)
        self.textDESKey       = QPlainTextEdit(self)
        self.comboDESMode     = QComboBox(self)
        
        self.comboDESMode.addItem("EBC")
        self.comboDESMode.addItem("CBC")
        self.comboDESMode.addItem("3 DES")
        
        self.layoutDESButton = QVBoxLayout()
        self.layoutDESButton.addStretch()
        self.layoutDESButton.addWidget(self.buttonDESEncrypt)
        self.layoutDESButton.addStretch()
        self.layoutDESButton.addWidget(self.buttonDESDecrypt)
        self.layoutDESButton.addStretch()
        
        self.layoutDESLeft = QVBoxLayout()
        self.layoutDESLeft.addWidget(self.labelDESPlain)
        self.layoutDESLeft.addWidget(self.textDESPlain)
        
        self.layoutDESRight = QVBoxLayout()
        self.layoutDESRight.addWidget(self.labelDESCypher)
        self.layoutDESRight.addWidget(self.textDESCypher)
        
        self.layoutDESText = QHBoxLayout()
        self.layoutDESText.addLayout(self.layoutDESLeft)
        self.layoutDESText.addLayout(self.layoutDESButton)
        self.layoutDESText.addLayout(self.layoutDESRight)
        
        self.layoutDESKey = QHBoxLayout()
        self.layoutDESKey.addWidget(self.labelDESKey)
        self.layoutDESKey.addWidget(self.textDESKey)
        self.layoutDESKey.addWidget(self.comboDESMode)
        
        self.layoutDES = QVBoxLayout()
        self.layoutDES.addLayout(self.layoutDESKey)
        self.layoutDES.addLayout(self.layoutDESText)
        
        self.tabDES.setLayout(self.layoutDES)
        self.textDESKey.setFixedHeight(40) 
        
        # Create MD5 tab
        
        self.labelMD5Plain    = QLabel("Plain Text:",self)
        self.labelMD5Digest   = QLabel("Digest Text:",self)
        self.buttonMD5Hash    = QPushButton("Digest",self)
        self.textMD5Plain     = QPlainTextEdit(self)
        self.textMD5Digest    = QPlainTextEdit(self)
        
        self.layoutMD5Button = QVBoxLayout()
        self.layoutMD5Button.addStretch()
        self.layoutMD5Button.addWidget(self.buttonMD5Hash)
        self.layoutMD5Button.addStretch()
        
        self.layoutMD5Left = QVBoxLayout()
        self.layoutMD5Left.addWidget(self.labelMD5Plain)
        self.layoutMD5Left.addWidget(self.textMD5Plain)
        
        self.layoutMD5Right = QVBoxLayout()
        self.layoutMD5Right.addWidget(self.labelMD5Digest)
        self.layoutMD5Right.addWidget(self.textMD5Digest)
        
        self.layoutMD5Text = QHBoxLayout()
        self.layoutMD5Text.addLayout(self.layoutMD5Left)
        self.layoutMD5Text.addLayout(self.layoutMD5Button)
        self.layoutMD5Text.addLayout(self.layoutMD5Right)
        
        self.layoutMD5 = QVBoxLayout()
        self.layoutMD5.addLayout(self.layoutMD5Text)
        
        self.tabMD5.setLayout(self.layoutMD5)
        
        # Create RSA tab
        
        self.labelRSAKeyLength    = QLabel("Key length:",self)
        self.labelRSAPrivateKey   = QLabel("Private Key:",self)
        self.labelRSAEulerTotient = QLabel("Euler Totient:",self)
        self.labelRSAPlain        = QLabel("Plain Text:",self)
        self.labelRSACypher       = QLabel("Cipher Text:",self)
        self.buttonRSAEncrypt     = QPushButton("Encrypt",self)
        self.buttonRSADecrypt     = QPushButton("Decrypt",self)
        self.textRSAPlain         = QPlainTextEdit(self)
        self.textRSACypher        = QPlainTextEdit(self)
        self.textRSAKeyLength     = QPlainTextEdit(self)
        self.textRSAPrivateKey = QPlainTextEdit(self)
        self.textRSAEulerTotient=QPlainTextEdit(self)
        
        self.layoutRSAButton = QVBoxLayout()
        self.layoutRSAButton.addStretch()
        self.layoutRSAButton.addWidget(self.buttonRSAEncrypt)
        self.layoutRSAButton.addStretch()
        self.layoutRSAButton.addWidget(self.buttonRSADecrypt)
        self.layoutRSAButton.addStretch()
        
        self.layoutRSALeft = QVBoxLayout()
        self.layoutRSALeft.addWidget(self.labelRSAPlain)
        self.layoutRSALeft.addWidget(self.textRSAPlain)
        
        self.layoutRSARight = QVBoxLayout()
        self.layoutRSARight.addWidget(self.labelRSACypher)
        self.layoutRSARight.addWidget(self.textRSACypher)
        
        self.layoutRSAText = QHBoxLayout()
        self.layoutRSAText.addLayout(self.layoutRSALeft)
        self.layoutRSAText.addLayout(self.layoutRSAButton)
        self.layoutRSAText.addLayout(self.layoutRSARight)
        
        self.layoutRSAKeyLength = QHBoxLayout()
        self.layoutRSAKeyLength.addWidget(self.labelRSAKeyLength)
        self.layoutRSAKeyLength.addWidget(self.textRSAKeyLength)
        
        self.layoutRSAPrivateKey = QHBoxLayout()
        self.layoutRSAPrivateKey.addWidget(self.labelRSAPrivateKey)
        self.layoutRSAPrivateKey.addWidget(self.textRSAPrivateKey)
        
        self.layoutRSAEulerTotient = QHBoxLayout()
        self.layoutRSAEulerTotient.addWidget(self.labelRSAEulerTotient)
        self.layoutRSAEulerTotient.addWidget(self.textRSAEulerTotient)
        
        self.layoutRSAKey = QVBoxLayout()
        self.layoutRSAKey.addLayout(self.layoutRSAKeyLength)
        self.layoutRSAKey.addLayout(self.layoutRSAPrivateKey)
        self.layoutRSAKey.addLayout(self.layoutRSAEulerTotient)
        
        
        self.layoutRSA = QVBoxLayout()
        self.layoutRSA.addLayout(self.layoutRSAKey)
        self.layoutRSA.addLayout(self.layoutRSAText)
        
        self.tabRSA.setLayout(self.layoutRSA)
        
        self.textRSAKeyLength.setFixedHeight(40)
        self.textRSAPrivateKey.setFixedHeight(40)
        self.textRSAEulerTotient.setFixedHeight(40)
        
        # Create SHA tab
        
        self.labelSHAKey      = QLabel("Key:",self)
        self.labelSHAPlain    = QLabel("Plain Text:",self)
        self.labelSHACypher   = QLabel("Cipher Text:",self)
        self.buttonSHAEncrypt = QPushButton("Encrypt",self)
        self.buttonSHADecrypt = QPushButton("Decrypt",self)
        self.textSHAPlain     = QPlainTextEdit(self)
        self.textSHACypher    = QPlainTextEdit(self)
        self.textSHAKey       = QPlainTextEdit(self)
        
        self.layoutSHAButton = QVBoxLayout()
        self.layoutSHAButton.addStretch()
        self.layoutSHAButton.addWidget(self.buttonSHAEncrypt)
        self.layoutSHAButton.addStretch()
        self.layoutSHAButton.addWidget(self.buttonSHADecrypt)
        self.layoutSHAButton.addStretch()
        
        self.layoutSHALeft = QVBoxLayout()
        self.layoutSHALeft.addWidget(self.labelSHAPlain)
        self.layoutSHALeft.addWidget(self.textSHAPlain)
        
        self.layoutSHARight = QVBoxLayout()
        self.layoutSHARight.addWidget(self.labelSHACypher)
        self.layoutSHARight.addWidget(self.textSHACypher)
        
        self.layoutSHAText = QHBoxLayout()
        self.layoutSHAText.addLayout(self.layoutSHALeft)
        self.layoutSHAText.addLayout(self.layoutSHAButton)
        self.layoutSHAText.addLayout(self.layoutSHARight)
        
        self.layoutSHAKey = QHBoxLayout()
        self.layoutSHAKey.addWidget(self.labelSHAKey)
        self.layoutSHAKey.addWidget(self.textSHAKey)
        
        self.layoutSHA = QVBoxLayout()
        self.layoutSHA.addLayout(self.layoutSHAKey)
        self.layoutSHA.addLayout(self.layoutSHAText)
        
        self.tabSHA.setLayout(self.layoutSHA)
        self.textSHAKey.setFixedHeight(40) 
        
        # Create VIG tab
        
        self.labelVIGKey      = QLabel("Key:",self)
        self.labelVIGPlain    = QLabel("Plain Text:",self)
        self.labelVIGCypher   = QLabel("Cipher Text:",self)
        self.buttonVIGEncrypt = QPushButton("Encrypt",self)
        self.buttonVIGDecrypt = QPushButton("Decrypt",self)
        self.textVIGPlain     = QPlainTextEdit(self)
        self.textVIGCypher    = QPlainTextEdit(self)
        self.textVIGKey       = QPlainTextEdit(self)
        
        self.layoutVIGButton = QVBoxLayout()
        self.layoutVIGButton.addStretch()
        self.layoutVIGButton.addWidget(self.buttonVIGEncrypt)
        self.layoutVIGButton.addStretch()
        self.layoutVIGButton.addWidget(self.buttonVIGDecrypt)
        self.layoutVIGButton.addStretch()
        
        self.layoutVIGLeft = QVBoxLayout()
        self.layoutVIGLeft.addWidget(self.labelVIGPlain)
        self.layoutVIGLeft.addWidget(self.textVIGPlain)
        
        self.layoutVIGRight = QVBoxLayout()
        self.layoutVIGRight.addWidget(self.labelVIGCypher)
        self.layoutVIGRight.addWidget(self.textVIGCypher)
        
        self.layoutVIGText = QHBoxLayout()
        self.layoutVIGText.addLayout(self.layoutVIGLeft)
        self.layoutVIGText.addLayout(self.layoutVIGButton)
        self.layoutVIGText.addLayout(self.layoutVIGRight)
        
        self.layoutVIGKey = QHBoxLayout()
        self.layoutVIGKey.addWidget(self.labelVIGKey)
        self.layoutVIGKey.addWidget(self.textVIGKey)
        
        self.layoutVIG = QVBoxLayout()
        self.layoutVIG.addLayout(self.layoutVIGKey)
        self.layoutVIG.addLayout(self.layoutVIGText)
        
        self.tabVIG.setLayout(self.layoutVIG)
        self.textVIGKey.setFixedHeight(40) 
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
