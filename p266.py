from functions import primes_up_to

primes = primes_up_to(190)

n = 1

for p in primes:
    n *= p

print(n)
print(int(n ** 0.5))

print(primes)
print(len(primes))

"""
"""
