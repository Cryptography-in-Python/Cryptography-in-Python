# -*- coding: utf-8 -*-

from ..sha1 import sha1
from ..DES import cryptography_des
from ..DES import file_encryptor
from ..MD5 import cryptography_md5
from ..RSA import cryptography_rsa
from ..AES import aes
from ..VIG import cryptography_vigenere
from PyQt5.QtWidgets import QWidget,QLabel, QPushButton,QComboBox,QApplication,QPlainTextEdit,QFileDialog, QMainWindow, QApplication,QVBoxLayout,QTabWidget,QHBoxLayout,QSpacerItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

import sys
import os
import os.path
import time
sys.path.append(os.path.abspath('../AES'))

INITIAL_WIDTH  = 800
INITIAL_HEIGHT = 600
TEXT_HEIGHT    = 40
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

        self.filePath = "" # file path for whatever file
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
        self.textAESKey.setFixedHeight(TEXT_HEIGHT) 
        
        self.buttonAESEncrypt.clicked.connect(self._AESEncrypt)
        self.buttonAESDecrypt.clicked.connect(self._AESDecrypt)
        
        # Create DES tab
        
        self.labelDESKey          = QLabel("Key:",self)
        self.labelDESPlain        = QLabel("Plain Text:",self)
        self.labelDESCypher       = QLabel("Cipher Text:",self)
        self.labelDESInitVec      = QLabel("Initial vector:",self)
        self.labelDESPlainFile    = QLabel("",self)
        self.labelDESCypherFile   = QLabel("",self) 
        self.buttonDESEncrypt     = QPushButton("Encrypt",self)
        self.buttonDESDecrypt     = QPushButton("Decrypt",self)
        self.buttonDESEncryptFile = QPushButton("Encrypt file:",self)
        self.buttonDESDecryptFile = QPushButton("Decrypt file:",self)
        self.textDESPlain         = QPlainTextEdit(self)
        self.textDESCypher        = QPlainTextEdit(self)
        self.textDESKey           = QPlainTextEdit(self)
        self.textDESInitVec       = QPlainTextEdit(self)
        self.comboDESMode         = QComboBox(self)
        
        self.comboDESMode.addItem("ECB")
        self.comboDESMode.addItem("CBC")
        self.comboDESMode.addItem("3-DES")
        
        self.layoutDESButton = QVBoxLayout()
        self.layoutDESButton.addStretch()
        self.layoutDESButton.addWidget(self.buttonDESEncrypt)
        self.layoutDESButton.addStretch()
        self.layoutDESButton.addWidget(self.buttonDESDecrypt)
        self.layoutDESButton.addStretch()
        
        self.layoutDESLeftButtom = QHBoxLayout()
        self.layoutDESLeftButtom.addWidget(self.buttonDESEncryptFile)
        self.layoutDESLeftButtom.addWidget(self.labelDESPlainFile)

        self.layoutDESLeft = QVBoxLayout()
        self.layoutDESLeft.addWidget(self.labelDESPlain)
        self.layoutDESLeft.addWidget(self.textDESPlain)
        self.layoutDESLeft.addLayout(self.layoutDESLeftButtom)
        
        self.layoutDESRightButtom = QHBoxLayout()
        self.layoutDESRightButtom.addWidget(self.buttonDESDecryptFile)
        self.layoutDESRightButtom.addWidget(self.labelDESCypherFile)

        self.layoutDESRight = QVBoxLayout()
        self.layoutDESRight.addWidget(self.labelDESCypher)
        self.layoutDESRight.addWidget(self.textDESCypher)
        self.layoutDESRight.addLayout(self.layoutDESRightButtom)
        
        self.layoutDESText = QHBoxLayout()
        self.layoutDESText.addLayout(self.layoutDESLeft)
        self.layoutDESText.addLayout(self.layoutDESButton)
        self.layoutDESText.addLayout(self.layoutDESRight)
        
        self.layoutDESKeyKey = QHBoxLayout()
        self.layoutDESKeyKey.addWidget(self.labelDESKey)
        self.layoutDESKeyKey.addWidget(self.textDESKey)
        self.layoutDESKeyKey.addWidget(self.comboDESMode)
        
        self.layoutDESInitVec = QHBoxLayout()
        self.layoutDESInitVec.addWidget(self.labelDESInitVec)
        self.layoutDESInitVec.addWidget(self.textDESInitVec)
        
        self.layoutDESKey = QVBoxLayout()
        self.layoutDESKey.addLayout(self.layoutDESKeyKey)
        self.layoutDESKey.addLayout(self.layoutDESInitVec)
        
        self.layoutDES = QVBoxLayout()
        self.layoutDES.addLayout(self.layoutDESKey)
        self.layoutDES.addLayout(self.layoutDESText)
        
        self.tabDES.setLayout(self.layoutDES)
        self.textDESKey.setFixedHeight(TEXT_HEIGHT) 
        self.textDESInitVec.setFixedHeight(TEXT_HEIGHT)
        
        self.buttonDESEncrypt.clicked.connect(self._DESEncrypt)
        self.buttonDESDecrypt.clicked.connect(self._DESDecrypt)
        self.buttonDESEncryptFile.clicked.connect(self._DESEncryptFile)
        self.buttonDESDecryptFile.clicked.connect(self._DESDecryptFile)
        
        # Create MD5 tab
        
        self.labelMD5Plain    = QLabel("Plain Text:",self)
        self.labelMD5Digest   = QLabel("Digest Text:",self)
        self.buttonMD5Hash    = QPushButton("Hash",self)
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
        
        self.buttonMD5Hash.clicked.connect(self._MD5Hash)
        
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
        
        self.textRSAKeyLength.setFixedHeight(TEXT_HEIGHT)
        self.textRSAPrivateKey.setFixedHeight(TEXT_HEIGHT)
        self.textRSAEulerTotient.setFixedHeight(TEXT_HEIGHT)
        
        self.buttonRSAEncrypt.clicked.connect(self._RSAEncrypt)
        self.buttonRSADecrypt.clicked.connect(self._RSADecrypt)
       
        # Create SHA tab
        
        self.labelSHAPlain    = QLabel("Plain Text:",self)
        self.labelSHADigest   = QLabel("Digest Text:",self)
        self.buttonSHAHash    = QPushButton("Hash",self)
        self.textSHAPlain     = QPlainTextEdit(self)
        self.textSHADigest    = QPlainTextEdit(self)

        
        self.layoutSHAButton = QVBoxLayout()
        self.layoutSHAButton.addStretch()
        self.layoutSHAButton.addWidget(self.buttonSHAHash)
        self.layoutSHAButton.addStretch()
        
        self.layoutSHALeft = QVBoxLayout()
        self.layoutSHALeft.addWidget(self.labelSHAPlain)
        self.layoutSHALeft.addWidget(self.textSHAPlain)
        
        self.layoutSHARight = QVBoxLayout()
        self.layoutSHARight.addWidget(self.labelSHADigest)
        self.layoutSHARight.addWidget(self.textSHADigest)
        
        self.layoutSHAText = QHBoxLayout()
        self.layoutSHAText.addLayout(self.layoutSHALeft)
        self.layoutSHAText.addLayout(self.layoutSHAButton)
        self.layoutSHAText.addLayout(self.layoutSHARight)
        
        self.layoutSHA = QVBoxLayout()
        self.layoutSHA.addLayout(self.layoutSHAText)
        
        self.tabSHA.setLayout(self.layoutSHA)
        
        self.buttonSHAHash.clicked.connect(self._SHAHash)
        
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
        self.textVIGKey.setFixedHeight(TEXT_HEIGHT) 
        
        self.buttonVIGEncrypt.clicked.connect(self._VIGEncrypt)
        self.buttonVIGDecrypt.clicked.connect(self._VIGDecrypt)
        
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    # Create functions for AES
    def _AESEncrypt(self):
        mode = self.comboAESMode.currentIndex()
        key = self.textAESKey.toPlainText()
        if len(key)>16:
            key = key[:16]
        elif len(key)<16:
            key = key + " "*(16-len(key))
        #print(key)
        cypherKey = []
        for i in key:
            cypherKey.append(ord(i))
        #print(cypherKey)
        
        plainText = self.textAESPlain.toPlainText()
        
        instance = aes.AESModeOfOperation()
        instance.set_key(key)
        initialVector = [103, 35, 148, 239, 76, 213, 47, 118,255, 222, 123, 176, 106, 134, 98, 92]
        
        if mode == 0: # OFB
            encodeMode = "OFB"
        elif mode == 1: # CFB
            encodeMode = "CFB"
        elif mode == 2: # CBC
            encodeMode = "CBC"
        
        #instanceMode = instance.modeOfOperation[encodeMode]
        #instance.aes.keySize["SIZE_128"]
        #print(type(plainText),type(instance.modeOfOperation[encodeMode]),type(cypherKey),type(instance.aes.keySize["SIZE_128"]),type(initialVector))
        modeAES,lengthAES,cypherText = instance.encrypt(plainText,instance.modeOfOperation[encodeMode],cypherKey,instance.aes.keySize["SIZE_128"],initialVector)
        
        self.textAESCypher.setPlainText("".join(chr(x) for x in cypherText))
        #print(cypherText)
        
    def _AESDecrypt(self):
        mode = self.comboAESMode.currentIndex()
        key = self.textAESKey.toPlainText()
        if len(key)>16:
            key = key[:16]
        elif len(key)<16:
            key = key + " "*(16-len(key))
        cypherKey = []
        for i in key:
            cypherKey.append(ord(i))
        cypherText = self.textAESCypher.toPlainText()
        cypherText2 = []
        for i in cypherText:
            cypherText2.append(ord(i))
        
        #print (cypherText2)
        instance = aes.AESModeOfOperation()
        initialVector = [103, 35, 148, 239, 76, 213, 47, 118,255, 222, 123, 176, 106, 134, 98, 92]

        if mode == 0: # OFB
            encodeMode = "OFB"
        elif mode == 1: # CFB
            encodeMode = "CFB"
        elif mode == 2: # CBC
            encodeMode = "CBC"        
        
        plainText = instance.decrypt(cypherText2,None,mode,cypherKey,instance.aes.keySize["SIZE_128"],initialVector)
        #print(plainText)
        self.textAESPlain.setPlainText(plainText)
        
        
    # Create functions for DES
    def _DESEncrypt(self):
        mode = self.comboDESMode.currentIndex()
        key = self.textDESKey.toPlainText()
        plainText = self.textDESPlain.toPlainText()
        
        if plainText == "": # file encrypt
            if self.filePath:
                start = time.time()
                outputPath = os.path.dirname(self.filePath)
                outputExpand = self.filePath.split(".")[-1]
                outputPath = outputPath + "/encrypted" + "." + outputExpand
                print(outputPath)
                encryptor = file_encryptor.FileEncryptor()
                encryptor.register_plain_source(self.filePath)
                encryptor.register_encrypt_source(outputPath)
                encryptor.set_key(key)
                encryptor.start_encrypt()
                end = time.time()
                msgBox = QMessageBox()
                msgText= "Encrypt complete with " + "{:3f}".format((end-start))+"s"
                msgBox.setText(msgText)
                msgBox.setWindowTitle("Success")
                msgBox.exec()
            else:# No input
                msgBox = QMessageBox()
                msgBox.setText("No input for encrypt")
                msgBox.exec()
        else:
            instance = cryptography_des.CryptographyDES()
            instance.set_work_mode(mode)
            instance.set_plain_text(plainText)
            
            if mode == 0: # ECB
                instance.set_key(key)
                instance.encrypt()
            elif mode == 1: # CBC
                instance.set_key(key)
                vec = instance.get_init_vector()
                instance.encrypt()
                self.textDESInitVec.setPlainText(vec)
            elif mode == 2: # 3 DES
                keys = self.textDESKey.toPlainText().split(" ")
                for key in keys:
                    instance.set_key(key)
                instance.encrypt()
            
            cypherText = instance.get_cipher_text()  
            self.textDESCypher.setPlainText(cypherText)  
            
    def _DESDecrypt(self):
        mode = self.comboDESMode.currentIndex()
        key = self.textDESKey.toPlainText()
        cypherText = self.textDESCypher.toPlainText()

        if cypherText == "": #file encrypt
            if self.filePath:
                start = time.time()
                outputPath = os.path.dirname(self.filePath)
                outputExpand = self.filePath.split(".")[-1]
                outputPath = outputPath + "/decrypted" + "." + outputExpand
                decryptor = file_encryptor.FileEncryptor()
                decryptor.register_encrypt_source(self.filePath)
                decryptor.register_plain_source(outputPath)
                decryptor.set_key(key)
                decryptor.start_decrypt()
                end = time.time()
                msgBox = QMessageBox()
                msgText= "Decrypt complete with " + "{:3f}".format((end-start))+"s"
                msgBox.setText(msgText)
                msgBox.setWindowTitle("Success")
                msgBox.exec()
            else:# No input
                msgBox = QMessageBox()
                msgBox.setText("No input for decrypt")
                msgBox.exec()
        else:
            instance = cryptography_des.CryptographyDES()
            instance.set_work_mode(mode)
            instance.set_cipher_text(cypherText)
            
            if mode == 0: # ECB
                instance.set_key(key)
                instance.decrypt()
            elif mode == 1: # CBC
                instance.set_key(key)
                vec = self.textDESInitVec.toPlainText()
                instance.set_init_vector(vec)
                instance.decrypt()
            elif mode == 2: # 3 DES
                keys = self.textDESKey.toPlainText().split(" ")
                for key in keys:
                    instance.set_key(key)
                instance.decrypt()
            
            plainText = instance.get_plain_text()  
            self.textDESPlain.setPlainText(plainText)

    def _DESEncryptFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                      "Choose a file to encrypt", "",
                      "Text Files (*.txt);;Image Files (*.png *.jpg *.bmp);;Video Files (*.mp4 *.avi)", options=options)
        if fileName:
            self.filePath = fileName
            self.labelDESPlainFile.setText(fileName)
    
    def _DESDecryptFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                      "Choose a file to decrypt", "",
                      "Text Files (*.txt);;Image Files (*.png *.jpg *.bmp);;Video Files (*.mp4 *.avi)", options=options)
        if fileName:
            self.filePath = fileName
            self.labelDESCypherFile.setText(fileName)

    # Create function for MD5 
    def _MD5Hash(self):
        plainText = self.textMD5Plain.toPlainText()
        instance = cryptography_md5.CryptographyMD5()
        digest = instance.encrypt(plainText)
        self.textMD5Digest.setPlainText(digest)
    
    # Create function for RSA
    def _RSAEncrypt(self):
        plainText = self.textRSAPlain.toPlainText()
        keyLength = self.textRSAKeyLength.toPlainText()
        keyLength = int(keyLength)
        
        instance = cryptography_rsa.CryptographyRSA(key_length=keyLength)
        instance.set_plain_text(plainText)
        instance.set_key(key='initial')
        
        keyChain = instance.get_key()
        privateKey = keyChain["private_key"]
        eulerTotient = keyChain["euler_totient"]
        
        instance.encrypt()
        
        cypherText = instance.get_cipher_text()
        
        self.textRSACypher.setPlainText(cypherText)
        self.textRSAPrivateKey.setPlainText(str(privateKey))
        self.textRSAEulerTotient.setPlainText(str(eulerTotient))
        
    def _RSADecrypt(self):
        cypherText = self.textRSACypher.toPlainText()
        keyLength = self.textRSAKeyLength.toPlainText()
        keyLength = int(keyLength)
        privateKey = self.textRSAPrivateKey.toPlainText()
        privateKey = int(privateKey)
        eulerTotient = self.textRSAEulerTotient.toPlainText()
        eulerTotient = int(eulerTotient)
        
        instance = cryptography_rsa.CryptographyRSA(key_length=keyLength)
        instance.set_key(key='private_key',
                         private_key=privateKey,
                         totient=eulerTotient)
        instance.set_cipher_text(cypherText)
        
        instance.decrypt()
        
        plainText = instance.get_plain_text_as_string()
        self.textRSAPlain.setPlainText(plainText)

    # Create function for SHA-1
    def _SHAHash(self):
        plainText = self.textSHAPlain.toPlainText()
        digest = sha1.shaone(plainText)
        self.textSHADigest.setPlainText(digest[2:])
        
    # Create function for VIG
    def _VIGEncrypt(self):
        plainText = self.textVIGPlain.toPlainText()
        key = self.textVIGKey.toPlainText()
        instance = cryptography_vigenere.CryptographyVigenere()
        cypherText = instance.encrypt(plainText,key)
        self.textVIGCypher.setPlainText(cypherText)
        
    def _VIGDecrypt(self):       
        cypherText = self.textVIGCypher.toPlainText()
        key = self.textVIGKey.toPlainText()
        instance = cryptography_vigenere.CryptographyVigenere()
        plainText = instance.decrypt(cypherText,key)
        self.textVIGPlain.setPlainText(plainText)
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
