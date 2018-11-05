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
        self.__K = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
                    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
                    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
                    0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
                    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
                    0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
                    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
                    0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
                    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
                    0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
                    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
                    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
                    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
                    0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
                    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
                    0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]
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

    def __pad(self,message):
        ''' First step of hashing, pad 1 and length to the end of message'''
        padded = ''
        messageLength = len(message)

        message += '1' # append 1 to mark end of message

        while (len(message)%512!=448):
            message += '0' 
        #bring the length of the message up to 64 bits fewer than a multiple of 512

        return message + self.__padlength(messageLength)
        # rewrite message with 1 and the ending length

    def __padlength(self,length):
        ''' The remaining bits are filled up with 64 bits representing 
            the length of the original message, modulo 2^64'''
        binLength = bin(length)[2:]
        if (len(binLength)>64):
            return binLength[len(binLength)-64:]
        else:
            return ''.join([0 for i in range(64-len(binLength))])+binLength

    def __splitIntoBlocks(self,message,n):
        ''' This function is used to split the message into blocks according to the 
        assigned length 'n' '''
        return [message[i:i+n] for i in range(0,len(message),n)]

    def __hash(self,message):
        '''The main hashing function'''
        messageLength = len(message.encode('utf-8'))


''' public methods'''
    def encrypt(self):
        

    def set_plain_text(self):


    def get_cipher_text(self,plain_text):
        

if __name__ =='__main__':
    '''
    Create tests for this file
    '''