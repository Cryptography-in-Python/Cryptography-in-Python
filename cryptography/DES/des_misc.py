try:
    import secrets
    randbits = secrets.randbits
except ImportError:
    import random
    randbits = random.getrandbits

import numpy as np

from ..base.misc import *

_initial_permutation_table = \
[
58,	50,	42,	34,	26,	18,	10,	2,
60,	52,	44,	36,	28,	20,	12,	4,
62,	54,	46,	38,	30,	22,	14,	6,
64,	56,	48,	40,	32,	24,	16,	8,
57,	49,	41,	33,	25,	17,	9,	1,
59,	51,	43,	35,	27,	19,	11,	3,
61,	53,	45,	37,	29,	21,	13,	5,
63,	55,	47,	39,	31,	23,	15,	7
]

_initial_permutation_table = np.array(_initial_permutation_table)
_initial_permutation_table -= 1

_expansion_table = \
[
32,	1,	2,	3,	4,	5,
4,	5,	6,	7,	8,	9,
8,	9,	10,	11,	12,	13,
12,	13,	14,	15,	16,	17,
16,	17,	18,	19,	20,	21,
20,	21,	22,	23,	24,	25,
24,	25,	26,	27,	28,	29,
28,	29,	30,	31,	32,	1,
]

_expansion_table = np.array(_expansion_table)
_expansion_table -= 1

_final_permutation_table = \
[
40,	8,  48,	16,	56,	24,	64,	32,
39,	7,  47,	15,	55,	23,	63,	31,
38,	6,  46,	14,	54,	22,	62,	30,
37,	5,  45,	13,	53,	21,	61,	29,
36,	4,  44,	12,	52,	20,	60,	28,
35,	3,  43,	11,	51,	19,	59,	27,
34,	2,  42,	10,	50,	18,	58,	26,
33,	1,  41,	9,	49,	17,	57,	25
]

_final_permutation_table = np.array(_final_permutation_table)
_final_permutation_table -= 1

_p_replacement_table = \
[
16,	7,  20,	21,
29,	12,	28,	17,
1,	15,	23,	26,
5,	18,	31,	10,
2,	8,	24,	14,
32,	27,	3,  9,
19,	13,	30, 6,
22,	11,	4,  25
]

_p_replacement_table = np.array(_p_replacement_table)
_p_replacement_table -= 1

_permutation_choice_one_left = \
[
57,	49,	41,	33,	25,	17,	9,
1,	58,	50,	42,	34,	26,	18,
10,	2,	59,	51,	43,	35,	27,
19,	11,	3,  60,	52,	44,	36
]

_permutation_choice_one_left = np.array(_permutation_choice_one_left)
_permutation_choice_one_left -= 1

_permutation_choice_one_right = \
[
63,	55,	47,	39,	31,	23,	15,
7,	62,	54,	46,	38,	30,	22,
14,	6,	61,	53,	45,	37,	29,
21,	13,	5,	28,	20,	12,	4
]

_permutation_choice_one_right = np.array(_permutation_choice_one_right)
_permutation_choice_one_right -= 1

_permutation_choice_one = np.concatenate((_permutation_choice_one_left, _permutation_choice_one_right))

_permutation_choice_two = \
[
14,	17,	11,	24,	1,	5,
3,	28,	15,	6,	21,	10,
23,	19,	12,	4,	26,	8,
16,	7,	27,	20,	13,	2,
41,	52,	31,	37,	47,	55,
30,	40,	51,	45,	33,	48,
44,	49,	39,	56,	34,	53,
46,	42,	50,	36,	29,	32
]

_permutation_choice_two = np.array(_permutation_choice_two)
_permutation_choice_two -= 1

_s_box_tables = \
[
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

_shift_bits_table = \
{
    1  : 1,
    2  : 1,
    3  : 2,
    4  : 2,
    5  : 2,
    6  : 2,
    7  : 2,
    8  : 2,
    9  : 1,
    10 : 2,
    11 : 2,
    12 : 2,
    13 : 2,
    14 : 2,
    15 : 2,
    16 : 1,
}

PRE_EXPANSION_LENGTH_DES  = 32
POST_EXPANSION_LENGTH_DES = 48

F_FUNCTION_OUTPUT_LENGTH_DES = 32
NUMBER_OF_SHIFTS_KEY_GEN_DES = 16

S_BOX_OUTPUT_SIZE_DES = 4
S_BOX_INPUT_SIZE_DES  = 6

HALF_ROUND_KEY_SIZE_DES = 28
FULL_KEY_SIZE_DES       = 64

DES_PLAINTEXT_BLOCK_SIZE      = 64
DES_HALF_PLAINTEXT_BLOCK_SIZE = 32

def get_initialization_vector(size=DES_PLAINTEXT_BLOCK_SIZE) -> [int]:
    return randbits(size)

def pad_bytes(raw_bytes:bytes, block_size:int) -> bytes:
    if len(raw_bytes) % block_size:
        pad_length = block_size - (len(raw_bytes) % block_size)
        return raw_bytes + (bytes([pad_length]) * pad_length)
    else:
        return raw_bytes

def unpad_bytes(raw_bytes:bytes, block_size:int) -> bytes:
    pad_length = raw_bytes[-1]
    if isinstance(pad_length, str) or pad_length >= block_size:
        return raw_bytes
    else:
        return raw_bytes[:-pad_length]

def rotate_left(number:[int]) -> [int]:
    result = number
    result.append(result[0])
    del result[0]
    return result

def split_bits(number:str, block_size:int) -> [str]:
    return [number[index:index+block_size] for index in range(0, len(number), block_size)]

def mix_number_by_table(number:[int], table:np.array) -> [int]:
    return list(map(lambda x: number[x], table))

def bytes_to_list_of_bin(input_bytes:bytes) -> [int]:
    result = [0] * len(input_bytes) * 8
    cursor = 0
    for ch in input_bytes:
        for i in range(7, -1, -1):
            result[cursor] = int(ch & (1 << i) != 0)
            cursor += 1

    return result

def list_of_bin_to_bytes(input_bytes:[int]) -> bytes:
    result = []
    c = 0
    for cursor in range(len(input_bytes)):
        c += input_bytes[cursor] << (7 - (cursor % 8))

        if (cursor % 8) == 7:
            result.append(c)
            c = 0
    
    return bytes(result)

def _lookup_s_box(value:[int], s_box_stage:int) -> str:
    '''
    help locate the value's mapping in s boxes
    '''
    # print("sbox in ", s_box_stage, value)
    first_last_cmb = value[0] << 1 | value[-1]
    middle_section = value[1] << 3 | value[2] << 2 | value[3] << 1 | value[4]
    value_from_box = _s_box_tables[s_box_stage][first_last_cmb][middle_section]
    return [
        (value_from_box & 8) >> 3,
        (value_from_box & 4) >> 2,
        (value_from_box & 2) >> 1,
        (value_from_box & 1)
    ]


def f_function(plain_text_slice:[int], part_of_key:[int]) -> [int]:
    '''
    the f function, the core of DES
    '''
    plain_text_slice = mix_number_by_table(plain_text_slice, _expansion_table)
    plain_text_slice = list(map(lambda x, y: x ^ y, plain_text_slice, part_of_key))
    s_box_inputs = [plain_text_slice[i:i+S_BOX_INPUT_SIZE_DES] for i in range(0, len(plain_text_slice), S_BOX_INPUT_SIZE_DES)]
    result       = []
    for index, inputs in enumerate(s_box_inputs):
        result.extend(_lookup_s_box(inputs, index))
    # print("after p", mix_number_by_table(result, _p_replacement_table))
    return mix_number_by_table(result, _p_replacement_table)
    

def generate_subkeys(key:bytes, decrypt=False) -> [[int]]:
    '''
    generate 16 round keys
    '''
    subkeys = []
    raw_key = mix_number_by_table(bytes_to_list_of_bin(key), _permutation_choice_one)
    left_key, right_key = raw_key[:28], raw_key[28:]

    for index in range(NUMBER_OF_SHIFTS_KEY_GEN_DES):
        for _ in range(_shift_bits_table[index+1]):
            left_key  = rotate_left(left_key)
            right_key = rotate_left(right_key)

        subkeys.append(mix_number_by_table(left_key + right_key, _permutation_choice_two))
    return subkeys

def process_block(plain_text:bytes, subkeys:[[int]], mode="ENCRYPT") -> bytes:
    '''
    process each plain text block. The block size should be 64bit/8bytes
    '''
    if isinstance(plain_text, bytes):
        plain_text = bytes_to_list_of_bin(plain_text)

    plain_text = mix_number_by_table(plain_text, _initial_permutation_table)
    left_block, right_block = plain_text[:32], plain_text[32:]

    if mode == "ENCRYPT":
        iterate_through = range(NUMBER_OF_SHIFTS_KEY_GEN_DES)
        stop_condition  = NUMBER_OF_SHIFTS_KEY_GEN_DES - 1
    elif mode == "DECRYPT":
        iterate_through = range(NUMBER_OF_SHIFTS_KEY_GEN_DES - 1, -1, -1)
        stop_condition  = 0
    else:
        raise ValueError("Invalid mode type! (ENCRYPT|DECRYPT)")

    for index in iterate_through:
        left_block = list(map(lambda x, y: x ^ y, left_block, f_function(right_block, subkeys[index])))

        if index != stop_condition:
            left_block, right_block = right_block, left_block

    result = mix_number_by_table(left_block + right_block, _final_permutation_table)
    print(result)
    return result

