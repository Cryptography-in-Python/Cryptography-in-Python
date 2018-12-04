import io
import os.path
import shutil
import time

from .cryptography_des import CryptographyDES

class FileEncryptor(object):

    def __init__(self):
        self._encryption_kernel = CryptographyDES()
        self._encrypt_file_src  = None
        self._plain_file_src    = None
        self._key               = None
        self._buffer_size       = 1024

    def register_encrypt_source(self, file_path):
        self._encrypt_file_src = file_path

    def register_plain_source(self, file_path):
        self._plain_file_src = file_path

    def set_key(self, key):
        self._key = key
        self._encryption_kernel.set_key(key)

    def start_encrypt(self):
        with open(self._plain_file_src, "rb") as plain, open(self._encrypt_file_src, "wb") as encrypt:
            block = plain.read(self._buffer_size)
            while block:
                self._encryption_kernel.set_plain_text(block)
                self._encryption_kernel.encrypt()
                encrypt.write(self._encryption_kernel.get_cipher_text_as_bytes())
                block = plain.read(self._buffer_size)

    def start_decrypt(self):
        with open(self._encrypt_file_src, "rb") as plain, open(self._plain_file_src, "wb") as encrypt:
            block = plain.read(self._buffer_size)
            self._encryption_kernel.set_padding(False)

            while block:
                self._encryption_kernel.set_cipher_text(block)
                self._encryption_kernel.decrypt()
                encrypt.write(self._encryption_kernel.get_plain_text_as_bytes())
                block = plain.read(self._buffer_size)

if __name__ == "__main__":
    start = time.time()
    encryptor = FileEncryptor()
    encryptor.register_plain_source("/Users/jeromemao/Desktop/cryptography/cryptography/DES/decrypted.png")
    encryptor.register_encrypt_source("encrypted.png")
    encryptor.set_key("Nogizaka")
    encryptor.start_encrypt()
    end = time.time()
    print("Encryption Done. Time Elapsed {:.3f}s".format(end-start))

    start = time.time()
    decryptor = FileEncryptor()
    decryptor.register_plain_source("decrypted.png")
    decryptor.register_encrypt_source("encrypted.png")
    decryptor.set_key("Nogizaka")
    decryptor.start_decrypt()
    end = time.time()
    print("Decryption Done. Time Elapsed {:.3f}s".format(end-start))