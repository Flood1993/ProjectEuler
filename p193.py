from functions import optimised_sieve
import time

start = time.time()

x = optimised_sieve(2**13) # 4 seconds to generate the sieve

print(time.time() - start)
print("Generated sieve")

start = time.time()

def div_sq(n):
	tmp = set()
	k = 4
	for j in range(4, n+1, 4): # add the multiples of 4 (2**2)
		tmp.add(j)

	# for each prime, get its square and add its multiples
	for i in range(len(x)):
		if x[i]:
			prime = 2*i + 1
			k = prime*prime
			for j in range(k, n+1, k):
				tmp.add(j)
	return (n - len(tmp))

"""
possible optimizations: 
	the number of multiples of 4 up to n is n//4
	the number of multiples of 9 up to n is n//9
	the number of multiples of 25 up to n is n//25
	problem: we will be counting the multiples of 4*9 = 36 twice...
"""

print(div_sq(15000000))
print(time.time() - start)

"""
Correct results:
15000000: 9118889
40000000: 24317053
"""


"""
15000000: 6 seconds
40000000: 10 seconds
100000000:
"""
