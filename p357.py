"""
Lets say n checks all conditions.

-- RESTRICTIONS --

n cannot be odd because 1 + n/1 would be even
n cannot be of the form 4k because 2 + 4k/2 = even

if d is a divisor of n:
    if d is even, n/d must be odd
    if d is odd, n/d must be even
    -> square numbers are excluded

since d + n/d is reciprocal for each d < sqrt(30), we only need to check if d + n/d is prime for d < sqrt(30)

-- CONDITIONS --

n must be of the form: (2 + 4k)
n can't be a square number
if n ends with a '0', the second rightmost digit must be odd
since 1 is a divisor of all numbers, n+1 must be a prime.
since 2 is a divisor of all of our candidates, 2 + n/2 must be a prime
"""

from functions import optimised_sieve

LIMIT = 10**8 + 5
primes = optimised_sieve(LIMIT)

print("Finished generating the sieve")

total = 0

for i in range(2, LIMIT, 4):
    if primes[i//2] and primes[1 + i//4]:
        # i is a candidate. We must check for all divisors d < sqrt(i) if d + i//d is a prime

        sq = int(i**0.5)
        for j in range(3, sq):
            if i%j == 0:
                if not primes[j//2]:
                    break
            total += i

print(total)
