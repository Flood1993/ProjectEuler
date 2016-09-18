from functions import optimised_sieve

LIMIT = 10**8 + 1000

primes = optimised_sieve(LIMIT)

print("Primes up to {} generated".format(str(LIMIT)))

def check_values(i, j):
    a = int(str(i) + str(j))
    b = int(str(j) + str(i))
    return primes[a//2] and primes[b//2]

for i in range(3, 10000, 2):
    if not primes[i//2]:
        continue
    for j in range(3, i, 2):
        if not primes[j//2]:
            continue
        if not check_values(i, j):
            continue
        for k in range(3, j, 2):
            if not primes[k//2]:
                continue
            if not check_values(i, k):
                continue
            if not check_values(j, k):
                continue
            for m in range(3, k, 2):
                if not primes[m//2]:
                    continue
                if not check_values(i, m):
                    continue
                if not check_values(j, m):
                    continue
                if not check_values(k, m):
                    continue
                for n in range(3, m, 2):
                    if not primes[n//2]:
                        continue
                    if not check_values(i, n):
                        continue
                    if not check_values(j, n):
                        continue
                    if not check_values(k, n):
                        continue
                    if not check_values(m, n):
                        continue
                    print(i, j, k, m, n, i+j+k+m+n)

print("Finished execution")
                    
# All primes are under 10000, therefore, they have 4 digits at max.

# By concatenating them, they could form an 8 digit number. Therefore,
# we must generate primes up to 100000000


