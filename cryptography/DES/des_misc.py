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

def _lookup_s_box(value:bitarray, s_box_stage:int) -> bitarray:
    '''
    help locate the value's mapping in s boxes
    '''
    first_last_cmb = int(value[0]) << 1 | int(value[-1])
    middle_section = int(value[1:-1].to01(), base=2)

    new_value  = _s_box_tables[s_box_stage][first_last_cmb][middle_section]
    raw_output = bitarray(bin(new_value)[2:])

    return expand_bitarray_to_n_bits(raw_output, S_BOX_OUTPUT_SIZE_DES)

def f_function(plain_text_slice:bitarray, part_of_key:bitarray) -> bitarray:
    '''
    the f function, the core of DES
    '''
    # perform expansion
    empty_array = bitarray()
    for member in _expansion_table:
        empty_array.append(plain_text_slice[member])

    #use XOR to mix with the key
    #use S BOX to make the process non-linear
    eight_bit_slices = list(split_data_to_every_n_bits(empty_array ^ part_of_key, S_BOX_INPUT_SIZE_DES))
    pst_s_box_result = bitarray()

    for index, member in enumerate(eight_bit_slices):
        pst_s_box_result.extend(_lookup_s_box(member, index))

    #use permutation table to squeeze the result back to 32 bit
    final_result = bitarray()
    for member in _p_replacement_table:
        final_result.append(pst_s_box_result[member])
    
    return final_result

def generate_subkeys(key:bitarray, decrypt=False) -> [bitarray]:
    '''
    generate 16 round keys
    '''
    subkeys    = []
    expand_key = expand_bitarray_to_n_bits(key.copy(), FULL_KEY_SIZE_DES)

    initial_choice = bitarray()
    for bit in _permutation_choice_one:
        initial_choice.append(expand_key[bit])

    left_hand, right_hand = initial_choice[:HALF_ROUND_KEY_SIZE_DES], initial_choice[HALF_ROUND_KEY_SIZE_DES:]
    for count in range(NUMBER_OF_SHIFTS_KEY_GEN_DES):

        lft_temp_int = int(left_hand.to01(), base=2)
        rgt_temp_int = int(right_hand.to01(), base=2)

        lft_temp_int = rotate_left(lft_temp_int, _shift_bits_table[count + 1], max_bits=HALF_ROUND_KEY_SIZE_DES)
        rgt_temp_int = rotate_left(rgt_temp_int, _shift_bits_table[count + 1], max_bits=HALF_ROUND_KEY_SIZE_DES)

        lft_temp_bit = bitarray(bin(lft_temp_int)[2:])
        rgt_temp_bit = bitarray(bin(rgt_temp_int)[2:])

        lft_temp_bit = expand_bitarray_to_n_bits(lft_temp_bit, HALF_ROUND_KEY_SIZE_DES)
        rgt_temp_bit = expand_bitarray_to_n_bits(rgt_temp_bit, HALF_ROUND_KEY_SIZE_DES)

        all_current_bit = bitarray()
        all_current_bit.extend(lft_temp_bit)
        all_current_bit.extend(rgt_temp_bit)

        subkey = bitarray()

        for member in _permutation_choice_two:
            subkey.append(all_current_bit[member])
        subkeys.append(subkey)

        left_hand, right_hand = lft_temp_bit, rgt_temp_bit

    return subkeys

def permutation_mapping(bit_array:bitarray, inverse=False) -> bitarray:
    result = bitarray()
    table  = _initial_permutation_table if not inverse else _final_permutation_table
    for member in table:
        result.append(bit_array[member])
    return result
