import math
import secrets

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
    n_value = 2

    while 2 ** n_value < number - 1:
        temp_d = (number - 1) / (2 ** n_value)
        if temp_d.is_integer() and int(temp_d) % 2 == 1:
            return n_value, int(temp_d)
        else:
            n_value += 1

    raise ValueError("This number cannot be properly decomposed")

def _atkin_sieve(limit:int) -> int:
    if limit > 2:
        yield 2
    if limit > 3:
        yield 3

    is_prime = [False for _ in range(limit + 1)]

    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            
            if y % 2 == 1:
                n = 4 * x ** 2 + y ** 2
                if n <= limit and n % 60 in (1,13,17,29,37,41,49,53):
                    is_prime[n] = not is_prime[n]

            if x % 2 == 1 and y % 2 == 0:
                n = 3 * x ** 2 + y ** 2
                if n <= limit and n % 60 in (7,19,31,43):
                    is_prime[n] = not is_prime[n]

            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                is_prime[n] = not is_prime[n]

    for n in range(5,int(math.sqrt(limit))):
        if is_prime[n]:
            for k in range(n**2,limit+1,n**2):
                is_prime[k] = False

    for n in range(5, limit):
        if is_prime[n]: 
            yield n

def _is_prime(number:int):
    results = list(_atkin_sieve(number+1))
    if not results: 
        return False
    else:
        return number == results[-1]

if __name__ == "__main__":
    print(_is_prime(50033))
