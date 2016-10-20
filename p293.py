from functions import is_probable_prime

# Perhaps we should look for a recursive function to generate the
# admissible numbers...

LIMIT = 10**9

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23)

adm = set()

def generate_admissible(n, next_prime):
	if n > LIMIT:
		return

	# Add the number to the set
	adm.add(n)

	# Try multiplying by the last prime or by the next one
	# This way it is guaranteed that divisors are consecutive primes
	if next_prime < len(primes):
		generate_admissible(n*primes[next_prime], next_prime)

	if next_prime + 1 < len(primes):
		generate_admissible(n*primes[next_prime+1], next_prime+1)

generate_admissible(2, 0)

sorted_adm = sorted(list(adm))

print("Total admissible numbers below 10**9:", len(adm))
print("First twelve:", sorted_adm[0:12])
print("Highest admissible:", sorted_adm[-1])

def pfn(n):
	"""
	Returns the pseudo-fortunate number of n. That is, the smallest M > 1
	such that n+m is prime.

	Since n is an admissible number, it will be even, so we can check only
	odd values > 1.
	"""
	m = 3
	while True:
		if is_probable_prime(n+m):
			return m
		m += 2

print(pfn(16))

res = set()

for el in sorted_adm:
    res.add(pfn(el))

print(sum(res))