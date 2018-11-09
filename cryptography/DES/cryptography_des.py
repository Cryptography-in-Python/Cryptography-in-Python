from .des_misc                    import *
from ..base.cryptography_abstract import CryptographyBase

# from Crypto.Cipher import DES

class CryptographyDES(CryptographyBase):

    BLOCK_SIZE    = 64
    HALF_BLOCK    = 32
    EXCHANGE_NUM  = 16

    def __init__(self):
        self._block_size = 8
        self._BYTEORDER  = 'little'

    def encrypt(self):
        '''
        encrypt the message with DES
        '''
        if "_plain_text" not in self.__dict__:
            raise ValueError("A plain text needs to be provided")
        if "_subkeys" not in self.__dict__:
            raise ValueError("A user defined key needs to be provided")
        
        result = []
        print("Plain Text:", self._plain_text[0])
        for member in self._plain_text:
            result.append(encrypt_block(member, self._subkeys))
        
        self._cipher_text = result
        for line in result:
            print("line", line)

    def decrypt(self):
        result = []
        for member in self._cipher_text:
            result.append(decrypt_block(member, self._subkeys))
        
        print("Decrypted:", result[0])

        # des = DES.new("IkutaIku")
        # cipher_text = int(self._cipher_text[0], base=2).to_bytes(8, byteorder=self._BYTEORDER)
        # print(des.decrypt(cipher_text))

    def set_plain_text(self, plain_text='') -> None:
        if isinstance(plain_text, str):
            plain_text = plain_text.encode('utf-8')
        
        self._plain_text = [int.from_bytes(plain_text[index:index+self._block_size], byteorder=self._BYTEORDER)
        for index in range(0, len(plain_text), self._block_size)]

        self._plain_text = [to_bin(member, 64) for member in self._plain_text]

    def get_plain_text(self) -> str:
        if "_plain_text" not in self.__dict__:
            raise ValueError("No plain text has been set/computed")
        else:
            return self._plain_text.tobytes().decode()

    def get_cipher_text(self) -> str:
        if "_cipher_text" not in self.__dict__:
            raise ValueError("No cipher text has been set/computed")
        else:
            return self._cipher_text

    def set_key(self, key:'a key, can be str, bytes or bitarray') -> None:
        '''
        set the keys from users
        '''
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        self._user_supplied_key = int.from_bytes(key, byteorder='little')
        self._subkeys = generate_subkeys(to_bin(self._user_supplied_key, 64))

    def get_key(self):
        return self._subkeys

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

    des_instance = CryptographyDES()
    des_instance.set_plain_text(message)
    des_instance.set_key("IkutaIku")
    des_instance.encrypt()
    des_instance.decrypt()

