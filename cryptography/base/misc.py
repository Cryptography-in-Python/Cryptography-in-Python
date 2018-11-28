import binascii
import struct

from bitarray import bitarray

def rotate_left(val, r_bits, max_bits=16):
    '''
    circular shift to left for r_bits
    from https://www.falatic.com/index.php/108/python-and-bitwise-rotation
    '''
    return (val << r_bits % max_bits) & (2 ** max_bits - 1) | \
    ((val & (2 ** max_bits - 1)) >> (max_bits -(r_bits % max_bits)))
 
def rotate_right(val, r_bits, max_bits=16):
    '''
    circular shift to right for r_bits
    from https://www.falatic.com/index.php/108/python-and-bitwise-rotation
    '''
    return ((val & (2 ** max_bits - 1)) >> r_bits % max_bits) | \
    (val << (max_bits -(r_bits % max_bits)) & (2 ** max_bits - 1))

def string_to_bitarray(string:str) -> bitarray:
    '''
    convert string to bit arrays
    '''
    string_in_bytes = string.encode("utf-8")
    bit_array       = bitarray()

    return bit_array.frombytes(string_in_bytes)

def expand_bitarray_to_n_bits(bit_array:bitarray, new_size:int, padToEnd = True) -> bitarray:
    '''
    expand the bitarray to n bits
    '''
    if len(bit_array) > new_size:
        raise ValueError("the new size is smaller than the bit array")

    elif len(bit_array) == new_size:
        return bit_array

    elif padToEnd:
        bits = [False for i in range(new_size - len(bit_array))]
        bit_array.extend(bits)
        return bit_array
    else:
        bits = [False for i in range(new_size - len(bit_array))]
        bits.extend(bit_array)
        return bits

def split_data_to_every_n_bits(bit_array:bitarray, slice_size:int):
    '''
    split the data into slices with each slice = [slice size]
    '''
    slice_num     = (len(bit_array) // slice_size)
    slice_num     = slice_num + 1 if len(bit_array) % slice_size else slice_num

    bit_array_cpy = bit_array.copy()
    bit_array_cpy = expand_bitarray_to_n_bits(bit_array_cpy, slice_num * slice_size)

    current_ptr = 0
    while current_ptr < len(bit_array_cpy):
        yield bit_array_cpy[current_ptr:current_ptr + slice_size]
        current_ptr += slice_size

def number_to_bitarray(number:int) -> bitarray:
    return bitarray(bin(number)[2:])

def bitarray_to_number(bitarr:bitarray) -> int:
    return int((bitarr).to01(),base=2)

def hexdigest(number:int)-> str:
    ''' returns hex form of an integer value, for example:
    >>>hexdigest(65535)
    'FFFF'
    NOTE: this function only takes int, you may need to call it mutiple times when
    dealing with larger numbers
    '''
    temp = '';
    while number >0:
        this_num = number %16
        number = int(number /16)
        this_hex = hex(this_num)
        temp = this_hex[2].upper() + temp 
    return temp

def to_hex(byte_str:bytes) -> str:
    try:
        return byte_str.hex()
    except AttributeError:
        return binascii.hexlify(byte_str)

def from_hex(hex_str:str) -> bytes:
    try:
        return hex_str.from_hex()
    except AttributeError:
        return binascii.unhexlify(hex_str)

# ======================= Function Tools ===========================
def check_variables(*variables):
    def mid_level_wrapper(func):
        def inner(self, *args, **kwargs):
            for variable in variables:
                if variable not in self.__dict__:
                    raise ValueError("{} does not exist".format(variable))

            return func(self, *args, **kwargs)
        return inner
    return mid_level_wrapper

def check_input_size(variable_size=64, index=1, type=int):
    def mid_level_wrapper(func):
        def inner(*args, **kwargs):
            if type == int:
                assert args[index-1].bit_length() == variable_size, "the argument does not have the declared size"
            elif type == str:
                assert len(args[index-1]) == variable_size, "the argument does not have the declared size"
            return func(*args, **kwargs)
        return inner
    return mid_level_wrapper

# ======================== Padding Tools ========================
def pad_bytes(byte_string:bytes, expected_length:int) -> bytes:
    if len(byte_string) == expected_length:
        return byte_string

    elif len(byte_string) < expected_length:
        return byte_string + b'\x00' * (expected_length - len(byte_string))
    
    else:
        raise ValueError("The expected length is shorter than the actual size of the byte string")

def pad_to_fit_block(byte_string:bytes, block_size:int) -> bytes:
    nearest_size = int(((len(byte_string) // block_size) + 1) * block_size)
    return pad_bytes(byte_string, nearest_size)

def pad_int(number:int, bits:int) -> int:
    if number.bit_length() < bits:
        return number << (bits - number.bit_length()) 
    elif number.bit_length() == bits:
        return number
    else:
        raise ValueError("number of bits is longer than the size of number")


