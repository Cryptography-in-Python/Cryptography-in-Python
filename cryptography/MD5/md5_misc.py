'''
Author: Yu Mi
Supportive functions and values for MD5 hashing, may not be used since some of them
are included in MD5 class as private members.
'''
import numpy as np
from ..base.misc    import *

_MAGIC_A = 0X67452301
_MAGIC_B = 0XEFCDAB89
_MAGIC_C = 0X98BADCFE
_MAGIC_D = 0X10325476


def _LINEAR_F(X,Y,Z):
    _X = number_to_bitarray(X)
    _Y = number_to_bitarray(Y)
    _Z = number_to_bitarray(Z)

    return bitarray_to_number(_X&_Y)|((~_X)&_Z)
