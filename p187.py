from functions import optimised_sieve

limit = 10**8

primes_boolean = optimised_sieve(limit)

print("Finished generating prime numbers")

primes = [2]

for i in range(len(primes_boolean)):
    if primes_boolean[i]:
        primes.append(2*i + 1)

res = 0

for i in range(len(primes)):
    for j in range(i, len(primes)):
        if primes[i] * primes[j] >= limit:
            break
        res += 1

print(res)
