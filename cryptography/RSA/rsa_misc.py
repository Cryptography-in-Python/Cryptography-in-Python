import math
import multiprocessing
import secrets
import random
import time

_known_primes = [
    2, 3
]

random.seed(time.time())

def _rand_between(lower:int, upper:int) -> int:
    num = secrets.randbelow(upper)
    while num < lower:
        num = secrets.randbelow(upper)
    return num

def _miller_rabin(number:int, accuracy:int) -> bool:
    '''
    use Miller Rabin to check whether a number is prime
    '''
    try:
        r, d = _miller_rabin_decompose(number)
        print(r, d)
    except ValueError:
        print("Error")
        return False

    for _ in range(accuracy):
        from_inner = False
        a = _rand_between(2, number - 2)
        x = (a ** d) % number 
        if x == 1 or x == number - 1:
            continue
        for _ in range(r - 1):
            x = (x ** 2) % number
            if x == number - 1:
                from_inner = True
                break
        if not from_inner:
            return False

    return True

def _miller_rabin_decompose(number:int) -> (int, int):
    '''
    a step in Miller-Rabin: decompose the number-1 to 2^n * d
    '''
    r = 0
    d = number - 1
    while d % 2 == 0:
        d, r = d >> 1, r + 1

    return d, r

def _is_prime_from_miller_rabin(number:int):
    return _miller_rabin(number, 10)

def _SPRP_is_composite(a, d, n, r):
    '''
    Referred from http://primes.utm.edu/prove/prove2_3.html
    '''
    # print(d, n, r)
    if pow(a, d, n) == 1:
        return False

    for r in range(r):
        if pow(a, 2 ** r * d, n) == n - 1:
            return False
    return True

def _query_SPRP_table(d:int, n:int, r:int, precision:int) -> bool:
    '''
    Referred from http://primes.utm.edu/prove/prove2_3.html
    '''
    if n < 1373653: 
        return not any(_SPRP_is_composite(a, d, n, r) for a in (2, 3))

    if n < 25326001: 
        return not any(_SPRP_is_composite(a, d, n, r) for a in (2, 3, 5))

    if n < 118670087467: 
        if n == 3215031751: 
            return False

        return not any(_SPRP_is_composite(a, d, n, r) for a in (2, 3, 5, 7))

    if n < 2152302898747: 
        return not any(_SPRP_is_composite(a, d, n, r) for a in (2, 3, 5, 7, 11))

    if n < 3474749660383: 
        return not any(_SPRP_is_composite(a, d, n, r) for a in (2, 3, 5, 7, 11, 13))

    if n < 341550071728321: 
        return not any(_SPRP_is_composite(a, d, n, r) for a in (2, 3, 5, 7, 11, 13, 17))

    return not any(_SPRP_is_composite(a, d, n, r) for a in _known_primes[:precision])
 
def is_prime(n, _precision_for_huge_n=16) -> bool:
    '''
    Use Millar Rabin and SPRP to check whether
    a number is primal
    '''
    if n in _known_primes or n in (0, 1):
        return True

    if any((n % p) == 0 for p in _known_primes):
        return False

    d, r = _miller_rabin_decompose(n)

    return _query_SPRP_table(d, n, r, _precision_for_huge_n)

def get_prime_number(bit_length=64) -> int:
    '''
    return a **VERY POSSIBLE** prime number with bit_length bits
    '''
    a_possible_number = random.getrandbits(bit_length)
    a_possible_number |= 1

    while not(a_possible_number % 5 != 0 and is_prime(a_possible_number)):
        a_possible_number = random.getrandbits(bit_length)
        a_possible_number |= 1
    
    return a_possible_number

def get_prime_number_multiprocessing(bit_length=64) -> int:
    pass

def preselect_numbers(file_name:str, bit_length=2048, numbers=30) -> None:
    '''
    preselect few prime numbers so that users can use them quickly
    '''
    with open(file_name, "w") as file:
        for _ in range(numbers):
            number = get_prime_number(bit_length)
            file.write(str(number) + "\n")

if __name__ == "__main__":
    # preselect_numbers("preselected_prime_numbers.txt", bit_length=2048, numbers=30)
    print(get_prime_number(bit_length=1024))

