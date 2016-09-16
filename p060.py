from functions import optimised_sieve, prime_sieve

'''
We are looking for a number abc such that:
    abc is prime
    abc3, abc7, abc109 and abc673 are prime
    3abc, 7abc, 109abc and 673abc are prime

'''
all_primes_boolean = optimised_sieve(100000000)
print('Big sieve generated')

to_check_primes_boolean = prime_sieve(10000)
print('Small sieve generated')
primes = []
for i in range(len(to_check_primes_boolean)):
    if to_check_primes_boolean[i]:
        primes.append(i)

print('Big loop')

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        for k in range(j + 1, len(primes)):
            for l in range(k + 1, len(primes)):
                for m in range(l + 1, len(primes)):
                    c1 = primes[i]
                    c2 = primes[j]
                    c3 = primes[k]
                    c4 = primes[l]
                    c5 = primes[m]


print('Finished execution')


# All primes are under 10000, therefore, they have 4 digits at max.

# By concatenating them, they could form an 8 digit number. Therefore,
# we must generate primes up to 100000000
