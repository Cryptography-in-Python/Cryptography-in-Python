# Project Cryptography in Python

In this project, we implemented cryptographic algorithm including AES, DES, MD5, RSA, VIG and SHA1. To be user friendly, we also implemented a GUI with pyqt5.

## Prerequisite

Our program requires pyqt5 to launch GUI. To install pyqt5, we can simply execute the command:

```bash
pip3 install pyqt5
```

Another request to run our code is the Boost library which accelerates the computing of encrypting and decrypting with DES. Please refer to this [link](https://www.ibm.com/support/knowledgecenter/en/SSWTQQ_1.0.0/com.ibm.swg.ba.cognos.trade_analytics.1.0.0.doc/t_trd_installboost.html).

## Launch the GUI

To launch the GUI, we can simply use the command:

```bash
python3 -m cryptography.GUI.gui
```



## AES cryptography

The AES cryptography includes OFB, CFB and CBC modes. We can switch between the working mode by choosing different modes in the combo box on the top right. Before doing the encryption and decryption, the users also need to specify the key to be used in the program. The key length shorter than 128bit will be padded with 0. The key length longer than 128bit will be ignored and only the first 128bit of the key will be taken into the algorithm.

Due to the limit of time, we are not able to expose the initial vector to be accessible for the user to change. So the initial vector of the AES are hard-coded.

To run the AES cryptography, press 'Encrypt' to create the cypher text from the plain text and press 'Decrypt' to create the plain text from cypher text.

## DES cryptograhy

The DES cryptography are implemented both in C and in python. The python version of DES is proof-of-feasible and the C version is for productive propose. The DES cryptography could support ECB, CBC and 3-DES modes. Users may also switch between the modes by choosing different modes in the combo box. Similar to the AES cryptography, the users also need to specify the keys used in the DES. The users may also need to give an initial vector when decrypting under the CBC mode. 

Another feature the DES cryptography supports is the encryption and decryption of a file. Currently we support the encryption and decryption of text file (.txt), image file (.png, .jpg .bmp) or video file(.mp4, .avi). The files encrypted are named _encrypted_ and its suffix are the same as the plain text file. The files decrypted are named _decrypted_ and its suffix are also the same as its encrypted file. We also provided several sample files to encrypt and decrypt. Such files are located in the _Sample/_ folder. Encrypting and decrypting a file may be slow, so please be patience when doing so.

NOTE: to encrypt or decrypt a file, please keep the input box of cypher text and plain text empty. 

## MD5 

MD5 provided a hash function. To run MD5, users can type into the plain text input box and push 'Hash' button

## RSA

RSA is an asymmetric cryptographic algorithm. To run RSA, users can first specify the length of key and then  type into the plain text input box. After that, they can push the 'Encrypt' button and see the result of encrypting. In the contrary, when filling the key length, Euler totient and the key, the users can decrypt the cypher text by pushing 'Decrypt' button.

## VIG

Vigenere cypher is another cryptographic algorithm that we implemented. The way of running it is nearly the same as AES.

## SHA1

SHA1 is another hashing function. Its usage is nearly the same to MD5.
