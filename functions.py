import random

def prime_sieve(n):
    """
    Returns a prime sieve with the numbers up to n
    """
    m = n+1
    res = [True]*m
    res[0] = False
    res[1] = False

    for i in range(2, int(n**0.5) + 1):
        if res[i]:
            for j in range(i*i, m, i):
                res[j] = False
    return res

# TODO: For 1000 this returns 961 as prime?
def optimised_sieve(n):
    """
    Returns a prime sieve with the numbers up to n, only containing the odd
    numbers

    res[k] corresponds to the number 2*k + 1
    e.g: res[3] = 2*3 + 1 = 7 = True (prime)

    To check if an ODD integer k is prime, we have to look at index k//2
    Be careful because number TWO is not included in the sieve
    """
    sieve_bound = n//2
    res = [True]*sieve_bound
    res[0] = False
    crosslimit = int(((n**0.5) - 1)//2)
    for i in range(1, crosslimit):
        if res[i]:
            for j in range(2*i*(i+1), sieve_bound, 2*i + 1):
                res[j] = False
    return res


def primes_up_to(n):
    """
    Returns a list containing all primes up to n
    """
    sieve = prime_sieve(n)
    res = [2]
    for i in range(len(sieve)):
        if sieve[i]:
            res.append(i)

    return res


def pythTriplet(m, n, d = 1):
    """
    Returns a Pythagorean triplet obtained from the values m and n.

    It will be primitive if and only if exactly one of m, n is even and
    gcd(m, n) = 1.
    """
    if m < n:
        m, n = n, m
    return [(m*m - n*n)*d, (2*m*n)*d, (m*m + n*n)*d]


def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers.

    a is assumed to be greater than b
    """
    while b != 0:
       a, b = b, a%b
    return a


def prime_factorization(n):
    """
    Returns a list containing the prime factorization of a given number n

    [[prime1, exp1], [prime2, exp2], ... [primeN, expN]]
    """
    res = []

    if n%2 == 0:
        lastFactor = 2
        n = n//2
        cnt = 1
        while n%2 == 0:
            n = n//2
            cnt += 1
        res.append([lastFactor, cnt])
    else:
        lastFactor = 1

    factor = 3
    maxFactor = int(n**0.5)
    while n > 1 and factor <= maxFactor:
        if n%factor == 0:
            n = n//factor
            lastFactor = factor
            cnt = 1
            while n%factor == 0:
                n = n//factor
                cnt += 1
            res.append([lastFactor, cnt])
            maxFactor = int(n**0.5)
        factor += 2
    if n != 1:
        res.append([n, 1])

    return res


def number_of_divisors(n):
    """
    Returns the number of divisors of n
    """
    prime_fac = prime_factorization(n)
    res = 1

    for fac in prime_fac:
        res *= (fac[1] + 1)

    return res


def totient(n):
    """
    Returns the Euler's totient function of n, that is, the count of the
    positive integers up to n that are relatively prime to it
    """
    prime_fac = prime_factorization(n)
    res = n

    for fac in prime_fac:
        res = int(res*(fac[0] - 1)/fac[0])

    return res


def ap_sqrt(n, steps):
    """
    Approximates the sqrt values of some number following some magic algorithm
    Only displays digits
    """
    a, b = 5*n, 5

    for i in range(steps):
        if a >= b:
            a, b = a-b, b+10
        else:
            a, b = 100*a, 10*b - 45

    return b

def continued_fraction(x):
    """
    Returns the continued fraction of x as a list of tuples (a,b,c),
    where:

        a + (sqrt(x)+b / c)

    represents each step.
    
    If we are interested on the notation of the form [4;(1,3,1,8)],
    we must take the first value from each tuple.

    Note: Be careful if the value passed is a perfect square.
    """
    res = []

    a = floor(x**0.5)
    b = -floor(x**0.5)
    c = 1    

    t = (a,b,c)
    res.append(t)

    while True:
        a, b, c = res[-1][0], res[-1][1], res[-1][2]
        a1 = floor(c*(x**0.5 - b)/(x - b*b))
        b1 = -b * c
        c1 = x - b*b
        b1 -= a1*c1

        _gcd = gcd(b1, c1)
        _gcd = gcd(_gcd, c)
        b1 //= _gcd
        c1 //= _gcd
        
        t = (a1, b1, c1)
        
        if t in res: # All continued fractions are periodic
            res.append(t)
            break

        res.append(t)
    
    return res

def solve_pell(n):
    """
    This function solves the Pell equation of the form:
    a*a - n * b*b = 1

    Input
    -----
    n - Integer
        Value of n. >= 2

    Output
    ------
    None
        If n is a perfect square (it has no solution)
    (a, b) - Tuple of integers
        Solutions for which the Pell equation is checked

    This function has been taken from the p066 solution forum
    https://projecteuler.net/thread=66
    """

    n1, d1 = 0, 1
    n2, d2 = 1, 0
    # These are the two bounding fractions

    while True:
        a = n1 + n2
        b = d1 + d2
        # a/b is the new candidate somewhere in the middle

        t = a*a - n*b*b  # See how close a^2/b^2 is to n 
        if t == 1: # You have your pell solution (a,b)
            return (a, b)
        elif t == 0: # N was a square = (a/b)^2
            return None;
        else: # Not there yet - adjust low or hi bound
            if t > 0:
                n2 =a
                d2 =b
            else:
                n1 =a
                d1 =b
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """

    _mrpt_num_trials = 5 # number of bases to test
    
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
