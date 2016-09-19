"""
n /

n**2 + 1 must be prime -> n**2 must be even -> must be even
n**2 + 3 must be prime -> sum of digits of n**2 must be 1 % 3

Since none of the values of n**2 + [5, 11, 15, 17, 19, 21, 23, 25] cannot make a prime number:
n**2 will be an even number. -ON HOLD-
"""

from functions import primes_up_to

primes = primes_up_to(1000000)

for i in range(2, 1000):
    ii = i*i
    if ii + 1 in primes and \
            ii + 3 in primes and \
            ii + 7 in primes and \
            ii + 9 in primes and \
            ii + 13 in primes and \
            ii + 27 in primes:
        print(i)
