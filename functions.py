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


def optimised_sieve(n):
    """
    Returns a prime sieve with the numbers up to n, only containing the odd
    numbers

    res[k] corresponds to the number 2*k + 1
    e.g: res[3] = 2*3 + 1 = 7 = True (prime)

    To check if an ODD integer k is prime, we have to look at index k//2
    Be careful becase number TWO is not included in the sieve
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
    sieve = optimised_sieve(n)
    res = [2]
    for i in range(len(sieve)):
        if sieve[i]:
            res.append(2*i + 1)

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
