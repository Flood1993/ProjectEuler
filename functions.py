def prime_sieve(n):
    """
    Returns a prime sieve with the numbers up to n
    """
    m = n+1
    res = [True]*m # for i in range(m)
    res[0] = False
    res[1] = False

    for i in range(2, int(n**0.5) + 1):
        if res[i]:
            for j in range(i*i, m, i):
                res[j] = False
    return res

def optimised_sieve(n):
    """
    Returns a prime sieve with the numbers up to n, only containing the odd numbers

    res[k] corresponds to the number 2*k + 1
    e.g: res[3] = 2*3 + 1 = 7 = True (prime)

    To check if an ODD integer k is prime, we have to look at index k//2
    Be careful becase number TWO is not included in the sieve
    """
    sieve_bound = (n-1)//2
    res = [True]*sieve_bound
    res[0] = False
    crosslimit = int(((n**0.5) - 1)//2)
    for i in range(1, crosslimit):
        if res[i]:
            for j in range(2*i*(i+1), sieve_bound, 2*i + 1):
                res[j] = False
    return res

import time
start = time.time()
my_primes2 = optimised_sieve(10**8)
print(time.time() - start)

"""
Sieve:
10**5   0.01563s
10**6   0.14063s
10**7   1.77516s -> 0.7
10**8   8.28
"""