import base64
import binascii
import struct

from ..base.cryptography_abstract import CryptographyBase
from .rsa_misc                    import *
from ..base.misc                  import *


class CryptographyRSA(CryptographyBase):

    def __init__(self, key_length=512):
        self._key_length = int(key_length / 2)
        self._block_size = int(key_length / 8)

        self._ENCRYPT = lambda message, public_key,  totient: pow(message, public_key,  totient)
        self._DECRYPT = lambda cipher,  private_key, totient: pow(cipher,  private_key, totient)

        self._BYTEORDER = 'little'

    @check_variables("_plain_text", "_public_key", "_euler_totient")
    def encrypt(self):
        self._cipher_text = [self._ENCRYPT(txt, self._public_key, self._euler_totient) for txt in self._plain_text]
    
    @check_variables("_cipher_text", "_private_key", "_euler_totient")
    def decrypt(self):
        self._plain_text = [self._DECRYPT(txt, self._private_key, self._euler_totient) for txt in self._cipher_text]

    def get_key(self) -> {str : int}:
        return {
            "public_key"    : self._public_key    if "_public_key"    in self.__dict__ else None,
            "private_key"   : self._private_key   if "_private_key"   in self.__dict__ else None,
            "euler_totient" : self._euler_totient if "_euler_totient" in self.__dict__ else None,
        }

    def set_key(self, key='initial', **kwargs) -> None:
        if key == "initial":
            key_packet = key_generation(self._key_length)
            self._public_key, self._private_key, self._euler_totient = key_packet
        
        elif key == "public_key":
            self._public_key    = kwargs["public_key"]
            self._euler_totient = kwargs["totient"]

        elif key == "private_key":
            self._private_key   = kwargs["private_key"]
            self._euler_totient = kwargs["totient"]

        else:
            raise ValueError("Invalid key type")

    def __str__(self) -> str:
        return "RSA Encoder/Decoder (Key Size: {})".format(self._key_length)

    def __repr__(self) -> str:
        return str(self)

    @check_variables("_cipher_text")
    def get_cipher_text(self) -> str:
        return to_hex(self.get_cipher_text_as_bytes())

    def set_cipher_text(self, cipher_text='') -> None:
        if isinstance(cipher_text, str):
            cipher_text = from_hex(cipher_text)
        
        cipher_text = pad_to_fit_block(cipher_text, self._block_size)

        self._cipher_text = [int.from_bytes(cipher_text[index:index+self._block_size], byteorder=self._BYTEORDER)
        for index in range(0, len(cipher_text), self._block_size)]

    def set_plain_text(self, plain_text='') -> None:
        if isinstance(plain_text, str):
            self._plain_text = plain_text.encode('utf-8')
        
        elif isinstance(plain_text, int):
            pass

        elif isinstance(plain_text, bytes):
            self._plain_text = plain_text

    def set_plain_text_from_file(self, file_path:str) -> None:
        with open(file_path, 'rb') as file_handler:
            self._plain_text = file_handler.read()

    @check_variables("_plain_text")
    def get_plain_text(self) -> bytes:
        return self._plain_text

    @check_variables("_cipher_text")
    def get_cipher_text_as_bytes(self):
        return b''.join([member.to_bytes(self._block_size, byteorder=self._BYTEORDER) 
        for member in self._cipher_text])
    
    @check_variables("_plain_text")
    def get_plain_text_as_bytes(self):
        return b''.join([member.to_bytes(self._block_size, byteorder=self._BYTEORDER) 
        for member in self._plain_text])

    @check_variables("_plain_text")
    def get_plain_text_as_string(self):
        try:
            return ''.join([member.to_bytes(member.bit_length(), byteorder=self._BYTEORDER).decode().rstrip('\0')
            for member in self._plain_text])
        except UnicodeDecodeError:
            return " ".join([hex(member) for member in self.get_plain_text_as_bytes()])

    @check_variables("_cipher_text")
    def to_file(self, file_path:str) -> None:
        with open(file_path, 'wb') as file_handler:
            for members in self._plain_text:
                file_handler.write(bytes([members]))

    @classmethod
    def from_instance(cls, instance):
        pass

if __name__ == "__main__":
    rsa_instance = CryptographyRSA()
    rsa_instance.set_key(key='initial')
    rsa_instance.set_plain_text("Tell me, Senpai!")
    rsa_instance.encrypt()
    result_enc = rsa_instance.get_cipher_text()
    print("Encryp Text:", result_enc)

    rsa_instance.set_cipher_text(result_enc)
    rsa_instance.decrypt()

    results = rsa_instance.get_plain_text_as_string()
    print("Plain Text:", results)    
