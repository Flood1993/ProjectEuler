#p214

from functions import optimised_sieve, totient
import time


start = time.time()

primes = optimised_sieve(40000000)
highest_tot = 0

for i in range(len(primes)):
    if primes[i]:
        tot = totient(2*i)
        if tot > highest_tot:
            highest_tot = tot

print(highest_tot)
print(time.time() - start)