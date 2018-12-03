# -*- coding: utf-8 -*-

from ..sha1 import sha1
from ..MD5 import cryptography_md5
from ..RSA import cryptography_rsa
from ..AES import aes
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton,
                             QComboBox, QApplication, QPlainTextEdit, QFileDialog)

from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import QIcon

import sys
import os
sys.path.append(os.path.abspath('../AES'))

# from ..DES import cryptography_des


class Example(QWidget):

    __algorithm = 'AES'
    __cypher_aes = {
        'cypherText': None,
        'key': None,
        'iv':None,
        'encode_mode': 'CBC',
        'mode': None,
        'length': None,
        'plainText': ''
    }

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

        self.lbl6 = QLabel("Chose block encoding mode", self)
        self.lbl6.move(150, 10)

        combo2 = QComboBox(self)
        combo2.addItem("OFB")
        combo2.addItem("CFB")
        combo2.addItem("CBC")

        combo2.move(150, 30)

        combo2.activated[str].connect(self.onModeChoosed)

        self.lbl7 = QLabel("Chose a text file (optional)", self)
        self.lbl7.move(370, 10)
        self.openFile = QPushButton("Open", self)
        self.openFile.move(370, 30)
        self.openFile.clicked.connect(self.openFileNameDialog)

        self.lbl2 = QLabel("type text to be encrypted:", self)
        self.lbl2.move(10, 60)
        self.textBox = QPlainTextEdit(self)
        self.textBox.setGeometry(10, 80, 300, 80)

        self.lbl3 = QLabel("type encription key:", self)
        self.lbl3.move(10, 170)
        self.textBox2 = QPlainTextEdit(self)
        self.textBox2.setGeometry(10, 190, 300, 80)

        self.encrypt = QPushButton("Encrypt", self)
        self.encrypt.move(320, 100)
        self.encrypt.clicked.connect(self._encrypt)

        self.lbl4 = QLabel("Encripted text:", self)
        self.lbl4.move(420, 60)
        self.textBox3 = QPlainTextEdit(self)
        self.textBox3.setGeometry(420, 80, 300, 80)

        self.decrypt = QPushButton("Decrypt", self)
        self.decrypt.move(320, 220)
        self.decrypt.clicked.connect(self._decrypt)

        self.lbl5 = QLabel("Decripted text:", self)
        self.lbl5.move(420, 170)
        self.textBox4 = QPlainTextEdit(self)
        self.textBox4.setGeometry(420, 190, 300, 80)

        self.setGeometry(300, 300, 750, 300)
        self.setWindowTitle('Group 7')
        self.show()

    def onAlgorithmChoosed(self, text):
        self.__algorithm = text
        print(f'Chose encription algorithm {text}')
        # self.testlabel.setPlainText(self.textBox.toPlainText())

    def onModeChoosed(self, text):
        self.__cypher_aes['encode_mode'] = text
        print(f'Chose encode mode {text}')
        # self.testlabel.setPlainText(self.textBox.toPlainText())

    def _encrypt(self):
        print(f'start encription using {self.__algorithm}.')
        instance = None
        if self.__algorithm == "AES":
            instance = aes.AESModeOfOperation()
            self.__cypher_aes['plainText'] = self.textBox.toPlainText()
            self.__cypher_aes['key'] = instance.set_key(self.textBox2.toPlainText())
            print("key is ",self.__cypher_aes['key'])
            # self.__cypher_aes['key'] = [143, 194, 34, 208, 145, 203, 230,
            #              143, 177, 246, 97, 206, 145, 92, 255, 84]
            self.__cypher_aes['iv'] = [103, 35, 148, 239, 76, 213, 47, 118,
                  255, 222, 123, 176, 106, 134, 98, 92]
                  
            print("key is ",self.__cypher_aes['key'])
            self.__cypher_aes['mode'], self.__cypher_aes['length'], self.__cypher_AES = instance.encrypt(self.__cypher_aes['plainText'], instance.modeOfOperation[self.__cypher_aes['encode_mode']],
                                                                 self.__cypher_aes['key'], instance.aes.keySize["SIZE_128"], self.__cypher_aes['iv'])
            print('m=%s, ol=%s (%s), ciph=%s' %
                  (self.__cypher_aes['mode'], self.__cypher_aes['length'], len(self.__cypher_aes['plainText']), self.__cypher_AES))
            self.textBox3.setPlainText(" ".join(str(x) for x in self.__cypher_AES))
        elif self.__algorithm == "DES":
            # instance = cryptography_des.CryptographyDES()
            pass
        elif self.__algorithm == "RSA":
            instance = cryptography_rsa.CryptographyRSA()
            # instance.set_plain_text(self.textBox.toPlainText())
            # instance.set_key(key='initial')
            digest = instance.encrypt(self.textBox.toPlainText())
            self.textBox3.setPlainText(digest)
            # instance.decrypt()
        elif self.__algorithm == "MD5":
            instance = cryptography_md5.CryptographyMD5()
        elif self.__algorithm == "SHA1":
            self.textBox3.setPlainText(sha1.shaone(self.textBox.toPlainText()))

    def _decrypt(self):
        print(f'start decription using {self.__algorithm}.')
        instance = None
        if self.__algorithm == "AES":
            instance = aes.AESModeOfOperation()
            decr = instance.decrypt(self.__cypher_AES, self.__cypher_aes['length'], self.__cypher_aes['mode'], self.__cypher_aes['key'],
                                    instance.aes.keySize["SIZE_128"], self.__cypher_aes['iv'])
            print(decr)
            self.textBox4.setPlainText(decr)
        elif self.__algorithm == "DES":
            # instance = cryptography_des.CryptographyDES()
            pass
        elif self.__algorithm == "RSA":
            instance = cryptography_rsa.CryptographyRSA()
            # instance.set_plain_text(self.textBox.toPlainText())
            # instance.set_key(key='initial')
            digest = instance.encrypt(self.textBox.toPlainText())
            self.textBox3.setPlainText(digest)
            # instance.decrypt()
        elif self.__algorithm == "MD5":
            print("No decription utility for MD5!")
        elif self.__algorithm == "SHA1":
            print("No decription utility for MD5!")

    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose a .txt to encript", "","text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            text_file = open(fileName,'r')
            self.textBox.setPlainText(text_file.read())
            text_file.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
