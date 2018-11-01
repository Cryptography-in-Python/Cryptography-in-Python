from abc import ABC
from abc import abstractclassmethod
from abc import abstractmethod

class CryptographyBase(ABC):
    '''
    The base class for all the cryptography implementation
    '''

    @abstractclassmethod
    def from_instance(cls, existed_instance):
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def __init__(self, key=None):
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def encrypt(self):
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def decrypt(self, cipher_text='') -> str:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def get_key(self) -> str:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def set_key(self, key='') -> None:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def get_cipher_text(self) -> str:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def set_cipher_text(self, cipher_text='') -> None:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def set_plain_text(self, plain_text='') -> None:
        raise NotImplementedError("It is an abstract method")

    @abstractmethod
    def get_plain_text(self) -> str:
        raise NotImplementedError("It is an abstract method")
