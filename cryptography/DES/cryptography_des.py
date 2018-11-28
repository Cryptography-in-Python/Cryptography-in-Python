from .base.misc                   import *
from .des_misc                    import *
from ..base.cryptography_abstract import CryptographyBase

ECB        = 0
CBC        = 1
TRIPLE_DES = 2

class CryptographyDES(CryptographyBase):

    BLOCK_SIZE    = 64
    HALF_BLOCK    = 32
    EXCHANGE_NUM  = 16

    def __init__(self):
        self._BLOCK_SIZE = 8
        self._WORK_MODE  = ECB

    def encrypt(self):
        '''
        encrypt the message with DES
        '''
        if "_plain_text" not in self.__dict__:
            raise ValueError("A plain text needs to be provided")
        if "_subkeys" not in self.__dict__:
            raise ValueError("A user defined key needs to be provided")

        self._cipher_text = b''

        if self._WORK_MODE == ECB: 
            for index in range(0, len(self._plain_text), self._BLOCK_SIZE):  
                self._cipher_text += process_block(
                    self._plain_text[index:index+self._BLOCK_SIZE], 
                    self._subkeys,
                    mode="ENCRYPT"
                )

        elif self._WORK_MODE == CBC:
            pass

    def decrypt(self):
        self._plain_text = b''

        if self._WORK_MODE == ECB:
            for index in range(0, len(self._cipher_text), self._BLOCK_SIZE): 
                self._plain_text += process_block(
                    self._cipher_text[index:index+self._BLOCK_SIZE], 
                    self._subkeys,
                    mode="DECRYPT"
                )

        elif self._WORK_MODE == CBC:
            pass

        self._plain_text = unpad_bytes(self._plain_text, self._BLOCK_SIZE)

    def set_plain_text(self, plain_text='') -> None:
        if isinstance(plain_text, str):
            plain_text = plain_text.encode('ascii')
        
        self._plain_text = pad_bytes(plain_text, self._BLOCK_SIZE)

    def get_plain_text_as_bytes(self) -> bytes:
        return self._plain_text

    def get_plain_text(self) -> str:
        return self._plain_text.decode()

    def get_cipher_text(self) -> str:
        return self._cipher_text.hex()

    def get_cipher_text_as_bytes(self) -> bytes:
        return self._cipher_text

    def set_work_mode(self, work_mode:int):
        assert work_mode in (ECB, CBC, TRIPLE_DES), "invalid work mode! (ECB|CBC|TRIPLE_DES)"
        self._WORK_MODE = work_mode

    def set_key(self, key:'a key, can be str, bytes or bitarray') -> None:
        '''
        set the keys from users
        '''
        if isinstance(key, str):
            key = key.encode('ascii')
        
        key = pad_bytes(key, self._BLOCK_SIZE)
        self._subkeys = generate_subkeys(key)

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
        if isinstance(cipher_text, str):
            cipher_text = bytes.fromhex(cipher_text)
        
        cipher_text = pad_bytes(cipher_text, self._BLOCK_SIZE)
        self._cipher_text = cipher_text


if __name__ == "__main__":
    message = "ItoMarika"

    des_instance = CryptographyDES()
    des_instance.set_plain_text(message)
    des_instance.set_key("Nogizaka")
    des_instance.encrypt()
    hex_output = des_instance.get_cipher_text()
    des_instance.set_cipher_text(hex_output)
    des_instance.decrypt()

