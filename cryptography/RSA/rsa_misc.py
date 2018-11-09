import multiprocessing
try:
    import secrets
    below = secrets.randbelow
except ImportError:
    import random
    below = random.randrange
import random
import struct
import time

try:
    from math import gcd
except ImportError:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

from decimal import Decimal

_known_primes = [
    2, 3
]

random.seed(time.time())

def _rand_between(lower:int, upper:int) -> int:
    num = below(upper)
    while num < lower:
        num = (upper)
    return num

def _miller_rabin(number:int, accuracy:int) -> bool:
    '''
    use Miller Rabin to check whether a number is prime
    '''
    try:
        r, d = _miller_rabin_decompose(number)
    except ValueError:
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
        a_possible_number += 2
    
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

def _get_coprime_num(num:int) -> int:
    random_num = _rand_between(1, num)
    
    while gcd(num, random_num) != 1:
        random_num = _rand_between(1, num)
    
    return random_num

def _extended_gcd(aa, bb):
    '''
    Temporarily used
    From https://rosettacode.org/wiki/Modular_inverse#Iteration_and_error-handling
    '''
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def _multiplicative_inverse(a:int, n:int) -> int:
    g, x, y = _extended_gcd(a, n)
    if g != 1:
	    raise ValueError
    return x % n

def key_generation(key_length=1024) -> int:
    prime_number_a = get_prime_number(bit_length=key_length)
    prime_number_b = get_prime_number(bit_length=key_length)

    euler_n       = prime_number_a * prime_number_b
    euler_totient = (prime_number_a - 1) * (prime_number_b - 1)

    public_key  = _get_coprime_num(euler_totient)
    private_key = _multiplicative_inverse(public_key, euler_totient)

    return public_key, private_key, euler_n


if __name__ == "__main__":
    print(get_prime_number(bit_length=1024))

