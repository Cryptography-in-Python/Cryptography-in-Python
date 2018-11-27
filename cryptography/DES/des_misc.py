import numpy as np
from bitarray import bitarray

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

def to_bin(number:int, bit_length:int) -> str:
    return bin(number)[2:].zfill(bit_length)

def rotate_left_str(number:str, bits_rotate:int) -> str:
    return number[bits_rotate:] + number[:bits_rotate] 

def rotate_right_str(number:str, bits_rotate:int) -> str:
    return number[-bits_rotate:] + number[:-bits_rotate]

def split_bits(number:str, block_size:int) -> [str]:
    return [number[index:index+block_size] for index in range(0, len(number), block_size)]

def mix_number_by_table(number:str, table:np.array, input_size:int) -> str:
    if len(number) < input_size:
        number = number.zfill(input_size)
    elif len(number) > input_size:
        raise ValueError("Number is longer than the input size")
    result   = ""

    for element in table:
        result += number[element]
    return result

@check_input_size(variable_size=S_BOX_INPUT_SIZE_DES, index=1, type=str)
def _lookup_s_box(value:str, s_box_stage:int) -> str:
    '''
    help locate the value's mapping in s boxes
    '''
    first_last_cmb = int(value[0] + value[-1], base=2)
    middle_section = int(value[1:5]          , base=2)
    new_value      = _s_box_tables[s_box_stage][first_last_cmb][middle_section]

    return to_bin(new_value, S_BOX_OUTPUT_SIZE_DES)

@check_input_size(variable_size=F_FUNCTION_OUTPUT_LENGTH_DES, index=1, type=str)
def f_function(plain_text_slice:str, part_of_key:str) -> int:
    '''
    the f function, the core of DES
    '''
    after_expansion = mix_number_by_table(plain_text_slice, _expansion_table, PRE_EXPANSION_LENGTH_DES)
    mixure = int(after_expansion, base=2) ^ int(part_of_key, base=2)
    mixure = to_bin(mixure, POST_EXPANSION_LENGTH_DES)

    temp_results = []
    for stage, member in enumerate(split_bits(mixure, S_BOX_INPUT_SIZE_DES)):
        temp_results.append(_lookup_s_box(member, stage))
    
    return mix_number_by_table("".join(temp_results), _p_replacement_table, 32)
    

@check_input_size(variable_size=FULL_KEY_SIZE_DES, index=1, type=str)
def generate_subkeys(key:str, decrypt=False) -> [int]:
    '''
    generate 16 round keys
    '''
    subkeys = []
    left_key  = mix_number_by_table(key, _permutation_choice_one_left,  FULL_KEY_SIZE_DES)
    right_key = mix_number_by_table(key, _permutation_choice_one_right, FULL_KEY_SIZE_DES)

    for index in range(NUMBER_OF_SHIFTS_KEY_GEN_DES):
       left_key  = rotate_left_str(left_key,  _shift_bits_table[index+1])
       right_key = rotate_left_str(right_key, _shift_bits_table[index+1])
       temp_key  = mix_number_by_table(left_key + right_key, _permutation_choice_two, FULL_KEY_SIZE_DES)
       subkeys.append(temp_key)

    return subkeys

@check_input_size(variable_size=DES_PLAINTEXT_BLOCK_SIZE, index=1, type=str)
def encrypt_block(plain_text:str, subkeys:[str]) -> str:
    after_init_permutation = mix_number_by_table(plain_text, _initial_permutation_table, DES_PLAINTEXT_BLOCK_SIZE)
    left_init  = after_init_permutation[DES_HALF_PLAINTEXT_BLOCK_SIZE:] 
    right_init = after_init_permutation[:DES_HALF_PLAINTEXT_BLOCK_SIZE]

    for stage, key in enumerate(subkeys):
        temp = f_function(right_init, key)
        temp_left = int(left_init, base=2) ^ int(temp, base=2)
        temp_left = to_bin(temp_left, DES_HALF_PLAINTEXT_BLOCK_SIZE)

        if stage < NUMBER_OF_SHIFTS_KEY_GEN_DES - 1:
            left_init, right_init = right_init, temp_left
        else:
            left_init = temp_left
    
    return mix_number_by_table(left_init + right_init, _final_permutation_table, DES_PLAINTEXT_BLOCK_SIZE)

@check_input_size(variable_size=DES_PLAINTEXT_BLOCK_SIZE, index=1, type=str)
def decrypt_block(plain_text:str, subkeys:[str]) -> str:
    after_init_permutation = mix_number_by_table(plain_text, _initial_permutation_table, DES_PLAINTEXT_BLOCK_SIZE)
    left_init  = after_init_permutation[DES_HALF_PLAINTEXT_BLOCK_SIZE:] 
    right_init = after_init_permutation[:DES_HALF_PLAINTEXT_BLOCK_SIZE]

    for stage, key in enumerate(subkeys[::-1]):
        temp = f_function(right_init, key)
        temp_left = int(left_init, base=2) ^ int(temp, base=2)
        temp_left = to_bin(temp_left, DES_HALF_PLAINTEXT_BLOCK_SIZE)

        if stage < 15:
            left_init, right_init = right_init, temp_left
        else:
            left_init, right_init = temp_left, right_init
    
    return mix_number_by_table(left_init + right_init, _final_permutation_table, DES_PLAINTEXT_BLOCK_SIZE)
