import numpy as np
from bitarray       import bitarray
from ..base.misc    import *

_MAGIC_A = 0X67452301L
_MAGIC_B = 0XEFCDAB89L
_MAGIC_C = 0X98BADCFEL
_MAGIC_D = 0X10325476L


def _LINEAR_F(X,Y,Z):
    _X = number_to_bitarray(X)
    _Y = number_to_bitarray(Y)
    _Z = number_to_bitarray(Z)

    return bitarray_to_number(_X&_Y)|((~_X)&_Z)
    
    
    
    

