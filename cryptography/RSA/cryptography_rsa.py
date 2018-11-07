import struct
from ..base.cryptography_abstract import CryptographyBase
from .rsa_misc                    import *

class CryptographyRSA(CryptographyBase):

    def __init__(self, key_length=1024):
        self._key_length     = key_length
        self._block_size     = int(key_length / 8)

        self._ENCRYPT = lambda message, public_key,  totient: pow(message, public_key,  totient)
        self._DECRYPT = lambda cipher,  private_key, totient: pow(cipher,  private_key, totient)

    def encrypt(self):
        if "_plain_text" not in self.__dict__:
            raise ValueError("Plain text has not been set yet")

        result = []
        for txt in self._plain_text:
            # print(txt)
            encrypted = self._ENCRYPT(txt, self._public_key, self._euler_totient)
            result.append(encrypted)
        self._cipher_text = result
    
    def decrypt(self):
        if "_cipher_text" not in self.__dict__:
            raise ValueError("Cipher text has not been set yet") 

        result = []
        for txt in self._cipher_text:
            decrypted = self._DECRYPT(txt, self._private_key, self._euler_totient)
            result.append(decrypted)
        string = ""

        for txt in result:
            txt_as_str = struct.pack("q", txt)
            string += txt_as_str.decode()
        print(string)
        return result

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
        return "RSA"

    def __repr__(self) -> str:
        return str(self)

    def get_cipher_text(self) -> str:
        if "_ciper_text" in self.__dict__:
            return self._ciper_text
        raise ValueError("The plain text has not been encrypted/cipher text has not been set")

    def set_cipher_text(self, cipher_text='') -> None:
        self._ciper_text = cipher_text

    def set_plain_text(self, plain_text='') -> None:
        if isinstance(plain_text, str):
            self._plain_text = plain_text.encode('utf-8')


    def get_plain_text(self) -> str:
        pass

    @classmethod
    def from_instance(cls, instance):
        pass

if __name__ == "__main__":
    rsa_instance = CryptographyRSA()
    rsa_instance.set_key(key='initial')
    rsa_instance.set_plain_text("Nogizaka")
    encrypted = rsa_instance.encrypt()
    # rsa_instance.set_cipher_text(encrypted)
    rsa_instance.decrypt()
