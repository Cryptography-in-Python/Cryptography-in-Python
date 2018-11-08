import struct
from ..base.cryptography_abstract import CryptographyBase
from .rsa_misc                    import *

class CryptographyRSA(CryptographyBase):

    def __init__(self, key_length=512):
        self._key_length     = int(key_length / 2)
        self._block_size     = int(key_length / 8)

        self._ENCRYPT = lambda message, public_key,  totient: pow(message, public_key,  totient)
        self._DECRYPT = lambda cipher,  private_key, totient: pow(cipher,  private_key, totient)

    @check_variables("_plain_text", "_public_key", "_euler_totient")
    def encrypt(self):
        result = []
        for txt in self._plain_text:
            result.append(self._ENCRYPT(txt, self._public_key, self._euler_totient))
        self._cipher_text = result
    
    @check_variables("_cipher_text", "_private_key", "_euler_totient")
    def decrypt(self):
        result = []
        for txt in self._cipher_text:
            result.append(self._DECRYPT(txt, self._private_key, self._euler_totient))
        self._plain_text = result

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

    @check_variables("_plain_text")
    def get_cipher_text(self) -> str:
        return self._cipher_text

    def set_cipher_text(self, cipher_text='') -> None:
        self._cipher_text = cipher_text

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
    
    @check_variables("_plain_text")
    def get_plain_text(self, decode_func=bytes.decode) -> None:
        return (decode_func(member) for member in self._plain_text)

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
    rsa_instance.set_plain_text_from_file("summary_3_jerome_mao.txt")
    rsa_instance.encrypt()
    rsa_instance.decrypt()
    rsa_instance.to_file("test_out.txt")
    
    # def decoder(int_like:int) -> str:
    #     return bytes([int_like]).decode()

    # results = rsa_instance.get_plain_text(decode_func=decoder)
    # print("".join([mem for mem in results]))
    
