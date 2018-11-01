from bitarray import bitarray

from .des_misc                    import *
from ..base.cryptography_abstract import CryptographyBase

class CryptographyDES(CryptographyBase):

    BLOCK_SIZE    = 64
    HALF_BLOCK    = 32
    EXCHANGE_NUM  = 16

    def __init__(self):
        pass

    def encrypt(self):
        '''
        encrypt the message with DES
        '''
        if "_plain_text" not in self.__dict__:
            raise ValueError("A plain text needs to be provided")

        if "_subkeys" not in self.__dict__:
            raise ValueError("A user defined key needs to be provided")

        print("Pre-Process Length:", len(self._plain_text)) # debug

        _inputs = split_data_to_every_n_bits(self._plain_text, CryptographyDES.BLOCK_SIZE)
        _encrypt_output = bitarray()

        for input_block in _inputs:
            input_block = permutation_mapping(input_block, inverse=False)

            left_hand  = input_block[:CryptographyDES.HALF_BLOCK]
            right_hand = input_block[CryptographyDES.HALF_BLOCK:]

            for count in range(CryptographyDES.EXCHANGE_NUM):
                subkey     = self._subkeys[count]

                left_temp  = right_hand
                right_temp = left_hand ^ f_function(right_hand, subkey)

                left_hand, right_hand = left_temp, right_temp

            current_block = bitarray()
            current_block.extend(left_hand)
            current_block.extend(right_hand)
            current_block = permutation_mapping(current_block, inverse=True)

            _encrypt_output.extend(current_block)

        self._cipher_text = _encrypt_output

    def decrypt(self):
        _inputs = split_data_to_every_n_bits(self._cipher_text, CryptographyDES.BLOCK_SIZE)
        _decrypt_output = bitarray()

        decrypt_keys = self._subkeys[::-1]

        for input_block in _inputs:
            left_hand  = input_block[:CryptographyDES.HALF_BLOCK]
            right_hand = input_block[CryptographyDES.HALF_BLOCK:]


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
        elif isinstance(key, bitarray):
            return
        
        self._user_supplied_key = bitarray()
        self._user_supplied_key.frombytes(key)
        self._subkeys = generate_subkeys(self._user_supplied_key)

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
    des_instance.set_key("Ikuta\0\0\0")
    des_instance.encrypt()
    encrypted = des_instance.get_cipher_text()
