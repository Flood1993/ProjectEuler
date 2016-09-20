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

S = 10**7

primes = prime_sieve(S//2)

tmp = []
for i in range(len(primes)):
    if primes[i]:
        tmp.append(i)

primes = tmp

print("Primes OK")

total = 0

sq = int(S**0.5)

for i in range(len(primes)):
    if primes[i] > sq:
        break
    
    exp = 1
    tmp_prod = primes[i]
    while tmp_prod <= S:
        tmp_prod *= primes[i]
        exp += 1

    for j in range(i+1, len(primes)):
        _max = 0
        prod = primes[i] * primes[j]
        if prod > S:
            break
        # These two primes are valid.
        
        for k in range(exp, 0, -1):
            for m in range(exp, 0, -1):
                cur = (primes[i]**k) * (primes[j]**m)
                if cur <= S:
                    if cur > _max:
                        _max = cur
                    else:
                        break

        total += _max

print(total)
