# -*- coding: utf-8 -*-

from ..base.misc                  import *
from ..base.cryptography_abstract import CryptographyBase

from .des_misc                    import *

WORK_MODE_ECB        = 0
WORK_MODE_CBC        = 1
WORK_MODE_TRIPLE_DES = 2

class CryptographyDES(CryptographyBase):

    BLOCK_SIZE     = 64
    HALF_BLOCK     = 32
    EXCHANGE_NUM   = 16
    ALL_WORK_MODES = {value:key for key, value in globals().items() if key.startswith("WORK_MODE")}

    def __init__(self):
        self._BLOCK_SIZE = 8
        self._WORK_MODE  = WORK_MODE_ECB
        self._ENCODING   = 'utf-8'
        self._key_chain  = []

    def encrypt(self):
        '''
        encrypt the message with DES
        '''
        if "_plain_text" not in self.__dict__:
            raise ValueError("A plain text needs to be provided")

        self._cipher_text = b''

        if self._WORK_MODE == WORK_MODE_ECB: 
            for index in range(0, len(self._plain_text), self._BLOCK_SIZE):  
                output = process_block(
                    self._plain_text[index:index+self._BLOCK_SIZE], 
                    self._key_chain[0],
                    mode="ENCRYPT"
                )
                self._cipher_text += list_of_bin_to_bytes(output)

        elif self._WORK_MODE == WORK_MODE_CBC:
            assert "_initialization_vector" in self.__dict__
            mix_mix = self._initialization_vector
            for index in range(0, len(self._plain_text), self._BLOCK_SIZE): 
                input_block = bytes_to_list_of_bin(self._plain_text[index:index+self._BLOCK_SIZE]) 
                input_block = list(map(lambda x, y: x ^ y, input_block, mix_mix))

                output = process_block(
                    input_block, 
                    self._key_chain[0],
                    mode="ENCRYPT"
                )
                mix_mix = output
                self._cipher_text += list_of_bin_to_bytes(output)

        elif self._WORK_MODE == WORK_MODE_TRIPLE_DES:
            assert len(self._key_chain) == 3, "triple DES requires 3 keys"

            first_layer_des = CryptographyDES()
            first_layer_des.set_key(self._key_chain[0])

            second_layer_des = CryptographyDES()
            second_layer_des.set_key(self._key_chain[1])

            third_layer_des  = CryptographyDES()
            third_layer_des.set_key(self._key_chain[2])

            first_layer_des.set_plain_text(self._plain_text)
            first_layer_des.encrypt()
            temp = first_layer_des.get_cipher_text_as_bytes()

            second_layer_des.set_cipher_text(temp)
            second_layer_des.decrypt()
            temp = second_layer_des.get_plain_text_as_bytes()

            third_layer_des.set_plain_text(temp)
            third_layer_des.encrypt()
            self._cipher_text = third_layer_des.get_cipher_text_as_bytes()

    def decrypt(self):
        self._plain_text = b''

        if self._WORK_MODE == WORK_MODE_ECB:
            for index in range(0, len(self._cipher_text), self._BLOCK_SIZE): 
                output = process_block(
                    self._cipher_text[index:index+self._BLOCK_SIZE], 
                    self._key_chain[0],
                    mode="DECRYPT"
                )
                self._plain_text += list_of_bin_to_bytes(output)

        elif self._WORK_MODE == WORK_MODE_CBC:
            assert "_initialization_vector" in self.__dict__
            mix_mix = self._initialization_vector
            for index in range(0, len(self._cipher_text), self._BLOCK_SIZE): 
                input_block = bytes_to_list_of_bin(self._cipher_text[index:index+self._BLOCK_SIZE])

                output= process_block(
                    input_block, 
                    self._key_chain[0],
                    mode="DECRYPT"
                )
                output  = list(map(lambda x, y: x ^ y, output, mix_mix))
                mix_mix = input_block
                self._plain_text += list_of_bin_to_bytes(output)

        elif self._WORK_MODE == WORK_MODE_TRIPLE_DES:
            assert len(self._key_chain) == 3, "triple DES requires 3 keys ({} given)".format(len(self._key_chain))

            first_layer_des = CryptographyDES()
            first_layer_des.set_key(self._key_chain[0])

            second_layer_des = CryptographyDES()
            second_layer_des.set_key(self._key_chain[1])

            third_layer_des  = CryptographyDES()
            third_layer_des.set_key(self._key_chain[2])

            third_layer_des.set_cipher_text(self._cipher_text)
            third_layer_des.decrypt()
            temp = third_layer_des.get_plain_text_as_bytes()

            second_layer_des.set_plain_text(temp)
            second_layer_des.encrypt()
            temp = second_layer_des.get_cipher_text_as_bytes()

            first_layer_des.set_cipher_text(temp)
            first_layer_des.decrypt()
            self._plain_text = first_layer_des.get_plain_text()

        self._plain_text = unpad_bytes(self._plain_text, self._BLOCK_SIZE)

    def set_plain_text(self, plain_text='') -> None:
        if isinstance(plain_text, str):
            plain_text = plain_text.encode(self._ENCODING)
        
        self._plain_text = pad_bytes(plain_text, self._BLOCK_SIZE)

    def get_plain_text_as_bytes(self) -> bytes:
        return self._plain_text

    def get_plain_text(self) -> str:
        if isinstance(self._plain_text, str):
            return self._plain_text
        return self._plain_text.decode()

    def get_cipher_text(self) -> str:
        return to_hex(self._cipher_text)

    def get_cipher_text_as_bytes(self) -> bytes:
        return self._cipher_text

    def set_work_mode(self, work_mode:int):
        assert work_mode in CryptographyDES.ALL_WORK_MODES, "invalid work mode! (ECB|CBC|TRIPLE_DES)"
        self._WORK_MODE = work_mode

    def set_key(self, key:'a key, can be str, bytes or bitarray') -> None:
        '''
        set the keys from users
        '''
        if isinstance(key, str):
            key = key.encode(self._ENCODING)

        elif isinstance(key, list):
            self._key_chain.append(key)
            return
        
        key = pad_bytes(key, self._BLOCK_SIZE)
        self._key_chain.append(generate_subkeys(key))

    def get_init_vector(self) -> [int]:
        if "_initialization_vector" not in self.__dict__:
            self._initialization_vector = get_initialization_vector(CryptographyDES.BLOCK_SIZE)
        return to_hex(list_of_bin_to_bytes(self._initialization_vector))

    def set_init_vector(self, init_vector:[int]):
        raw_vector = bytes_to_list_of_bin(from_hex(init_vector))
        assert len(raw_vector) == CryptographyDES.BLOCK_SIZE
        self._initialization_vector = raw_vector

    def get_key(self):
        return self._key_chain

    def set_encoding(self, encoding='utf-8'):
        self._ENCODING = encoding

    def __repr__(self):
        return "<CryptographyDES | Work_Mode={} | Encode={} | Address={}>".format(
            CryptographyDES.ALL_WORK_MODES[self._WORK_MODE], 
            self._ENCODING,
            hex(id(self))
        )

    def __str__(self):
        return repr(self)

    @classmethod
    def from_instance(cls, existed_instance):
        pass

    def set_cipher_text(self, cipher_text=''):
        if isinstance(cipher_text, str):
            cipher_text = from_hex(cipher_text)
        
        cipher_text = pad_bytes(cipher_text, self._BLOCK_SIZE)
        self._cipher_text = cipher_text

    def clear(self):
        del self._cipher_text
        del self._plain_text
        del self._initialization_vector
        del self._key_chain[:]
        self._WORK_MODE  = WORK_MODE_ECB
        self._BLOCK_SIZE = 8


if __name__ == "__main__":
    message =\
    (
    "Suzukake no ki no michi de 'kimi no hohoemi wo yume ni miru' to itte shimattara"
    "bokutachi no kankei ha do kawatte shimau no ka, bokunari ni nannichi ka kangaeta"
    "ue de no yaya kihazukashii ketsuron no yo na mono "
    )

    key = "Nogizaka"

    # ===== Encryption ======
    des_instance = CryptographyDES()
    des_instance.set_plain_text(message)
    des_instance.set_key(key)
    des_instance.set_work_mode(WORK_MODE_CBC)
    vec = des_instance.get_init_vector()
    des_instance.encrypt()
    hex_output = des_instance.get_cipher_text()
    print("Hex Encrypted Text:", hex_output)
    des_instance.clear()

    # ===== Decryption ======
    des_instance_b = CryptographyDES()
    des_instance_b.set_key(key)
    des_instance_b.set_work_mode(WORK_MODE_CBC)
    des_instance_b.set_cipher_text(hex_output)
    des_instance_b.set_init_vector(vec)
    des_instance_b.decrypt()
    print(des_instance_b)
    print("Decrypted Message:", des_instance_b.get_plain_text())

