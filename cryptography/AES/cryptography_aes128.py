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

    def encrypt(self, iput, key, size):
        '''
        encrypt the message with AES
        '''
        if "_plain_text" not in self.__dict__:
            raise ValueError("A plain text needs to be provided")

        if "_user_supplied_key" not in self.__dict__:
            raise ValueError("A user defined key needs to be provided")

        print("Pre-Process Length:", self._plain_text.length())  # debug
         
        # encrypt(self, iput, key, size):
        output = [0] * 16
        # the number of rounds
        nbrRounds = 0
        # the 128 bit block to encode
        block = [0] * 16
        # set the number of rounds
        nbrRounds = 10

        # the expanded keySize
        expandedKeySize = 16*(nbrRounds+1)

        # Set the block values, for the block:
        # a0,0 a0,1 a0,2 a0,3
        # a1,0 a1,1 a1,2 a1,3
        # a2,0 a2,1 a2,2 a2,3
        # a3,0 a3,1 a3,2 a3,3
        # the mapping order is a0,0 a1,0 a2,0 a3,0 a0,1 a1,1 ... a2,3 a3,3
        #
        # iterate over the columns
        for i in range(4):
            # iterate over the rows
            for j in range(4):
                block[(i+(j*4))] = iput[(i*4)+j]

        # expand the key into an 176, 208, 240 bytes key
        # the expanded key
        expandedKey = expandKey(key, size, expandedKeySize)

        # encrypt the block using the expandedKey
        block = aes_main(block, expandedKey, nbrRounds)

        # unmap the block again into the output
        for k in range(4):
            # iterate over the rows
            for l in range(4):
                output[(k*4)+l] = block[(k+(l*4))]
        return output
        

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
            return self._cipher_text.tobytes().decode()

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
