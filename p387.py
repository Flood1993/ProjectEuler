import random
 
_mrpt_num_trials = 10 # number of bases to test

LIMIT = 14 # 4 digits. We want compare numbers below 10**4 (10 000)
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
 
    >>> is_probable_prime(1)
    Traceback (most recent call last):
        ...
    AssertionError
    >>> is_probable_prime(2)
    True
    >>> is_probable_prime(3)
    True
    >>> is_probable_prime(4)
    False
    >>> is_probable_prime(5)
    True
    >>> is_probable_prime(123456789)
    False
 
    >>> primes_under_1000 = [i for i in range(2, 1000) if is_probable_prime(i)]
    >>> len(primes_under_1000)
    168
    >>> primes_under_1000[-10:]
    [937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
 
    >>> is_probable_prime(6438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    True
 
    >>> is_probable_prime(7438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    False
    """
    if n < 2:
        return False
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

L = []

L1 = [x for x in range(1, 10)]

L.append(L1)

def sum_digits(n):
    res = 0
    tmp = n
    while tmp != 0:
        res = res + tmp%10
        tmp = tmp//10
    return res

def is_harshad(n):
    """
    Returns if a number is divisible by the sum of its digits
    """
    s = sum_digits(n)

    return n%s == 0

for i in range(LIMIT - 2): # 13 for numbers less than 10**14
    tmp = []
    for x in L[-1]:
        for j in range(10):
            if is_harshad(x*10 + j):
                tmp.append(x*10 + j)
    L.append(tmp)

for i in range(len(L)):
    tmp = []
    for x in L[i]:
        if is_probable_prime(x//sum_digits(x)):
           tmp.append(x)
    L[i] = tmp

# L now contains the list of candidates for which we have to check if 
# adding 1, 3, 5, 7 or 9 at the end makes a prime

total = 0

for l in L:
    for x in l:
        for d in range(1, 10, 2):
            if is_probable_prime(x*10 + d):
                total += x*10 + d

print(total)
