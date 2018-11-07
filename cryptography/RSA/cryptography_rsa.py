
from ..base.cryptography_abstract import CryptographyBase
from .rsa_misc                    import *

class CryptographyRSA(CryptographyBase):

    def __init__(self, key_length=1024, ):
        self._prime_number_a = None
        self._prime_number_b = None

    def encrypt(self):
        pass
    
    def decrypt(self):
        pass

    def get_key(self) -> str:
        pass

    def get_pq(self) -> (int, int):
        pass

    def set_key(self, key='') -> None:
        pass

    def __str__(self) -> str:
        return "RSA"

    def __repr__(self) -> str:
        return str(self)

    def get_cipher_text(self) -> str:
        pass

    def set_cipher_text(self, cipher_text='') -> None:
        pass

    def set_plain_text(self, plain_text='') -> None:
        pass

    def get_plain_text(self) -> str:
        pass


