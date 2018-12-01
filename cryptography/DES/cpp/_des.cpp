#include <cstdint>
#include <bitset>
#include <iostream>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>


#define GETBIT(X, N) ((X >> (N)) & 1UL)
#define SETBIT(X, N) (X |= 1UL << (N))
#define LEFTSHIFT(X) (0x0fffffff & (X << 1))  | (0x00000001 & (X >> 27))

#define DES64BITMASK 1UL
#define DES32BITMASK 0x00000001
#define LOW32_MASK  0x00000000ffffffff

const char MODE_ENCRYPT = 0;
const char MODE_DECRYPT = 1;

int S_BOX[8][4][16]={
    {
        {14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7},
         {0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8},
         {4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0},
        {15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13}
    },
    {
        {15, 1,  8, 14,  6, 11,  3,  4,  9, 7,  2, 13, 12,  0,  5, 10},
        {3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5},
        {0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15},
        {13,  8, 10, 1,  3, 15,  4,  2, 11, 6,  7, 12,  0,  5, 14,  9}
    },
    {
        {10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8},
        {13,  7,  0,  9,  3,  4,  6, 10,  2, 8, 5, 14, 12, 11, 15,  1},
        {13,  6,  4,  9,  8, 15, 3, 0, 11,  1,  2, 12,  5, 10, 14,  7},
        {1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14, 3, 11,  5,  2, 12}
    },
    {
        {7, 13, 14,  3,  0,  6, 9, 10,  1,  2,  8,  5, 11, 12,  4, 15},
        {13, 8, 11,  5,  6, 15, 0,  3,  4,  7,  2, 12,  1, 10, 14,  9},
        {10, 6,  9,  0, 12, 11, 7, 13, 15,  1,  3, 14,  5,  2,  8,  4},
        {3, 15,  0,  6, 10,  1, 13, 8,  9,  4,  5, 11, 12,  7,  2, 14}
    },
    {
        {2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9},
        {14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6},
        {4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14},
        {11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3}
    },
    {
        {12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14, 7,  5, 11},
        {10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8},
        {9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6},
        {4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13}
    },
    {
        {4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1},
        {13,  0, 11, 7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6},
        {1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2},
        {6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12}
    },
    {
        {13,  2,  8, 4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7},
        {1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2},
        {7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8},
        {2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11}
    }
};

int FINAL_PERMUTATION[64] = {
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41,  9, 49, 17, 57, 25
};

int EXPANSION_TABLE[48] = {
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
};

int INITIAL_PERMUTATION[64] = {
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
};

int PERMUTATION_CHOICE_ONE[56] = {
    57,	49,	41,	33,	25,	17,	9,
    1,	58,	50,	42,	34,	26,	18,
    10,	2,	59,	51,	43,	35,	27,
    19,	11,	3,  60,	52,	44,	36,
    63,	55,	47,	39,	31,	23,	15,
    7,	62,	54,	46,	38,	30,	22,
    14,	6,	61,	53,	45,	37,	29,
    21,	13,	5,	28,	20,	12,	4
};

int PERMUTATION_CHOICE_TWO[56] = {
    14,	17,	11,	24,	1,	5,
    3,	28,	15,	6,	21,	10,
    23,	19,	12,	4,	26,	8,
    16,	7,	27,	20,	13,	2,
    41,	52,	31,	37,	47,	55,
    30,	40,	51,	45,	33,	48,
    44,	49,	39,	56,	34,	53,
    46,	42,	50,	36,	29,	32
};

int SHIFT_BITS[16] = {
1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
};

int P_REPLACEMENT[32] = {
    16,	7,  20,	21,
    29,	12,	28,	17,
    1,	15,	23,	26,
    5,	18,	31,	10,
    2,	8,	24,	14,
    32,	27,	3,  9,
    19,	13,	30, 6,
    22,	11,	4,  25
};

std::vector<uint64_t> key_generation(uint64_t key);

uint32_t check_s_box(const char& input, const int);

uint32_t f_function(const uint32_t& input_block, const uint64_t&);

uint32_t check_s_box(const char& input, const int stage)
{
    char out    = ((input >> 5) & 1) << 1 | (input & 0b1);
    char middle = (input >> 1) & 0b00001111;
    return S_BOX[stage][out][middle];
}

std::vector<uint64_t> key_generation(uint64_t key)
{
    std::vector<uint64_t> key_chain;

    uint64_t after_permutation_one = 0;
    for(int i = 0; i < 56; i++)
    {
        after_permutation_one <<= 1;
        after_permutation_one |= (key >> (64 - PERMUTATION_CHOICE_ONE[i])) & DES64BITMASK;
    }

    uint32_t key_left  = (uint32_t) ((after_permutation_one >> 28) & LOW32_MASK);
    uint32_t key_right = (uint32_t)  (after_permutation_one & LOW32_MASK);

    for (int i = 0; i < 16; i++)
    {
        for (int j = 0; j < SHIFT_BITS[i]; j++)
        {
            key_left  = LEFTSHIFT(key_left);
            key_right = LEFTSHIFT(key_right);
        }

        uint64_t before_permutation_choice_two = (((uint64_t) key_left) << 28) | (uint64_t) key_right;
        uint64_t result = 0;
        for(int j = 0; j < 48; j++)
        {
            result <<= 1;
            result |= (before_permutation_choice_two >> (56 - PERMUTATION_CHOICE_TWO[j])) & DES64BITMASK;;
        }

        key_chain.push_back(result);
    }
    return key_chain;
}

uint32_t f_function(const uint32_t& input_block, const uint64_t& part_of_the_key)
{
    uint64_t s_input = 0;
    for (int i = 0; i < 48; i++)
    {
        s_input <<= 1;
        s_input |= (uint64_t) ((input_block >> (32- EXPANSION_TABLE[i])) & DES32BITMASK);
    }

    s_input = s_input ^ part_of_the_key;

    uint32_t s_box_output = 0;
    for(int i = 0; i < 8; i++)
    {
        s_box_output <<= 4;
        s_box_output |= check_s_box((char)((s_input >> (42 - 6 * i)) & 0b111111), i);
    }

    uint32_t f_result = 0;
    for (int i = 0; i < 32; i++)
    {
        f_result <<= 1;
        f_result |= (s_box_output >> (32 - P_REPLACEMENT[i])) & DES32BITMASK;
    }
    return f_result;
}

uint64_t process_block(const uint64_t& block, const std::vector<uint64_t>& keys, const bool mode)
{
    uint64_t initial_permuation_result = 0;
    for (int i = 0; i < 64; i++)
    {
        initial_permuation_result <<= 1;
        initial_permuation_result |= (block >> (64 - INITIAL_PERMUTATION[i])) & DES64BITMASK;
    }

    uint32_t left_block =  (uint32_t) (initial_permuation_result >> 32) & 0x00000000ffffffff;
    uint32_t right_block = (uint32_t) (initial_permuation_result & 0x00000000ffffffff);

    for (int i = 0; i < 16; i++)
    {
        uint32_t right_after;
        if(mode == MODE_ENCRYPT)
            right_after = f_function(right_block, keys[i]);
            
        else
            right_after = f_function(right_block, keys[15 - i]);

        left_block = left_block ^ right_after;

        if(i != 15)
        {
            uint32_t temp = right_block;
            right_block   = left_block;
            left_block    = temp;
        } 
    }

    uint64_t after = (((uint64_t) left_block) << 32) | (uint64_t) right_block;
    uint64_t result = 0;

    for (int i = 0; i < 64; i++)
    {
        result <<= 1;
        result |= (after >> (64 - FINAL_PERMUTATION[i])) & DES64BITMASK;
    }
    return result;
}

#ifndef __DES__
#define __DES__

class _DES
{
    public:
        uint64_t encrypt(uint64_t block);
        uint64_t decrypt(uint64_t block);
        bool     set_key(uint64_t key);

    private:
        std::vector<uint64_t> key_chain;
};

uint64_t _DES::encrypt(uint64_t block)
{
    return process_block(block, this->key_chain, MODE_ENCRYPT);
}

uint64_t _DES::decrypt(uint64_t block)
{
    return process_block(block, this->key_chain, MODE_DECRYPT);
}

bool _DES::set_key(uint64_t key)
{
    this->key_chain = key_generation(key); 
    return true;
}

#endif

BOOST_PYTHON_MODULE(_des)
{
    using namespace boost::python;

    class_<std::vector<uint64_t> >("key_chain")
    .def(vector_indexing_suite<std::vector<uint64_t> >())
    ;

    class_<_DES>("_DES")
    .def("encrypt", &_DES::encrypt)
    .def("decrypt", &_DES::decrypt)
    .def("set_key", &_DES::set_key)
    ;
}