'''
Author: Yu Mi
Create a class to implement MD5 hashing, the real hashing function is in __hash, 
while other functions and values would be supportive use.
Reference:https://en.wikipedia.org/wiki/MD5
'''
from ..base.cryptography_abstract	import CryptographyBase
from ..base.misc 					import *
from md5_misc						import *
DEBUG_FLAG = 1 # Change to 0 for release
MAX_BITS = 32 # Max bits of an integer, normally 32

class CryptographyMD5(CryptographyBase):

    def __init__(self):
        # Some magic numbers used in MD5
        self.__A = 0X67452301L
        self.__B = 0XEFCDAB89L
        self.__C = 0X98BADCFEL
        self.__D = 0X10325476L

        pass;
''' private methods'''
    def __F(self,x,y,z):
        ''' linear function F'''
        return (x&y)|((~x)&z)

    def __G(self,x,y,z):
        '''linear function G'''
        return (x&z)|(y&(~z))

    def __H(self,x,y,z):
        '''linear function H'''
        return x^y^z

    def __I(self,x,y,z):
        '''linear function I'''
        return y^(x|(~z))

    def __R(self,function,a,b,c,d,x,s,ac):
        '''Warpper function for MD5 rounds'''
        r = a + function(b,c,d)
        r = r + x
        r = r + ac
        r = r & 0xffffffff
        r = rotate_left(r,s,MAX_BITS)
        r = r & 0xffffffff
        r = r + b
        return r & 0xffffffff # <- to make r unsigned
''' public methods'''
    def encrypt(self):
        

    def set_plain_text(self):


    def get_cipher_text(self,plain_text):
        

if __name__ =='__main__':
    '''
    Create tests for this file
    '''

