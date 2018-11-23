from bitarray import bitarray

from .aes_misc                    import *
from ..base.cryptography_abstract import CryptographyBase


class CryptographyAES128(CryptographyBase):

    BLOCK_SIZE = 128
    HALF_BLOCK = 64
    EXCHANGE_NUM = 16
    KEY_SIZE = 128

    # _current_key = [bitarray(32), bitarray(32), bitarray(32), bitarray(32)]
    _previous_key = bitarray(128)
    def __init__(self):
        pass

    def encrypt(self):
        '''
        encrypt the message with AES
        '''
        if "_plain_text" not in self.__dict__:
            raise ValueError("A plain text needs to be provided")

        if "_user_supplied_key" not in self.__dict__:
            raise ValueError("A user defined key needs to be provided")

        print("Pre-Process Length:", self._plain_text.length())  # debug
         
        fix=128 - self._plain_text.length() % 128
        for i in range(fix):
            self._plain_text = self._plain_text+bitarray('0')
            
        self._cipher_text = bitarray(self._plain_text.length())
        block_num = int(self._plain_text.length() / 128)
        for i in range(block_num):
            block = self._plain_text[i:i+128]
            #init
            self._current_key= set_first_key(self._user_supplied_key)
            block = GF2Add(self._current_key,block)
            #round 1 to 9
            for round in range(1,10):
                print('round',round)
                block=subBytes(block)
                block=shiftRows(block)
                block=mixColumn(block)
                [self._current_key,self._previous_key]=update_round_key(self._current_key,self._previous_key,round)
                block = GF2Add(self._current_key,block)
            #round 10
            block=subBytes(block)
            block=shiftRows(block)
            [self._current_key,self._previous_key]=update_round_key(self._current_key,self._previous_key,round)
            block = GF2Add(self._current_key,block)
            self._cipher_text[i:i+128]=block
        

    def decrypt(self):
        pass

        # self._cipher_text = _encrypt_output

    def set_plain_text(self, plain_text='') -> None:
        if isinstance(plain_text, str):
            plain_text = plain_text.encode('utf-8')
        elif isinstance(plain_text, bitarray):
            return

        self._plain_text = bitarray()
        self._plain_text.frombytes(plain_text)

    def get_plain_text(self) -> str:
        if "_plain_text" not in self.__dict__:
            raise ValueError("No plain text has been set/computed")
        else:
            print(self._plain_text)
            return self._plain_text.tobytes().decode()

    def get_cipher_text(self) -> str:
        if "_cipher_text" not in self.__dict__:
            raise ValueError("No cipher text has been set/computed")
        else:
            return self._cipher_text

    def set_key(self, key: 'a key, can be str, bytes or bitarray') -> None:
        '''
        set the keys from users
        '''
        if isinstance(key, str):
            key = key.encode('utf-8')
        elif isinstance(key, bitarray):
            return

        self._user_supplied_key = bitarray()
        self._user_supplied_key.frombytes(key)
        # print('key length: ',self._user_supplied_key.length())
        if self._user_supplied_key.length() < self.KEY_SIZE:
            raise ValueError("Key size must be at least 128 bits!")
        elif self._user_supplied_key.length() > self.KEY_SIZE:
            self._user_supplied_key = self._user_supplied_key[0:128]
            print("Key is too long, use first 128 bits")

    def get_key(self):
        pass

    def __repr__(self):
        return "Some DES instance"

    def __str__(self):
        return repr(self)

    @classmethod
    def from_instance(cls, existed_instance):
        pass

    def set_cipher_text(self, cipher_text=''):
        return None


if __name__ == "__main__":
    message = "Nogizaka"

    aes_instance = CryptographyAES128()
    aes_instance.set_plain_text(message)
    aes_instance.set_key("Ikuta\0\0\0")
    aes_instance.encrypt()
    encrypted = aes_instance.get_cipher_text()
