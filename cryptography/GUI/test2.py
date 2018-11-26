# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton,
                             QComboBox, QApplication, QPlainTextEdit)

from PyQt5.QtCore import pyqtSlot

import sys
import os
sys.path.append(os.path.abspath('../AES'))

from ..AES import cryptography_aes128
from ..DES import cryptography_des
from ..RSA import cryptography_rsa
from ..MD5 import cryptography_md5
from ..sha1 import *


class Example(QWidget):

    __algorithm = 'undecided'
    __plainText = ''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # self.testlabel = QPlainTextEdit(self)
        # self.testlabel.setGeometry(400,10,300,80)

        self.lbl = QLabel("Chose Algorithm", self)
        self.lbl.move(10, 10)

        combo = QComboBox(self)
        combo.addItem("AES")
        combo.addItem("DES")
        combo.addItem("RSA")
        combo.addItem("MD5")
        combo.addItem("SHA1")

        combo.move(10, 30)

        combo.activated[str].connect(self.onAlgorithmChoosed)

        self.lbl2 = QLabel("type text to be encrypted:", self)
        self.lbl2.move(10, 60)
        self.textBox = QPlainTextEdit(self)
        self.textBox.setGeometry(10,80,300,80)

        self.lbl3 = QLabel("type encription key:", self)
        self.lbl3.move(10, 170)
        self.textBox2 = QPlainTextEdit(self)
        self.textBox2.setGeometry(10,190,300,80)

        self.encrypt = QPushButton("Encrypt",self)
        self.encrypt.move(320, 100)
        self.encrypt.clicked.connect(self._encrypt)

        self.lbl4 = QLabel("Encripted text:", self)
        self.lbl4.move(420, 60)
        self.textBox3 = QPlainTextEdit(self)
        self.textBox3.setGeometry(420,80,300,80)

        self.decrypt = QPushButton("Decrypt",self)
        self.decrypt.move(320, 220)
        self.decrypt.clicked.connect(self._decrypt)

        self.lbl5 = QLabel("Decripted text:", self)
        self.lbl5.move(420, 170)
        self.textBox4 = QPlainTextEdit(self)
        self.textBox4.setGeometry(420,190,300,80)

        self.setGeometry(300, 300, 750, 300)
        self.setWindowTitle('Group 7')
        self.show()

    def onAlgorithmChoosed(self, text):
        self.__algorithm = text
        print(f'Chose encription algorithm {text}')
        # self.testlabel.setPlainText(self.textBox.toPlainText())

    def _encrypt(self):
        print(f'start encription using {self.__algorithm}.')
        instance = None
        if self.__algorithm == "AES":
            instance = cryptography_aes128.CryptographyAES128()
        elif self.__algorithm == "DES" :
            instance = cryptography_des.CryptographyDES()
        elif self.__algorithm == "RSA" :
            instance = cryptography_rsa.cryptography_rsa()
        elif self.__algorithm == "MD5" :
            instance == cryptography_md5.cryptography_md5()
        elif self.__algorithm == "SHA1" :
            pass
        
        instance.set_plain_text(self.textBox.toPlainText())
        instance.set_key(self.textBox2.toPlainText())
        instance.encrypt()
        self.textBox3.setPlainText(instance.get_cipher_text())
        # instance.decrypt()

    def _decrypt(self):
        print(f'start decription using {self.__algorithm}.')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
