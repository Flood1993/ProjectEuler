#p124

import operator

primesToGenerate = 100001

primes = [1]*primesToGenerate
radNums = [1]*primesToGenerate

primes[0] = 0
primes[1] = 0

for i in range(len(primes)):
    if primes[i] != 0:
        k = i
        radNums[k] *= k
        k += i
        while k < primesToGenerate:
            primes[k] = 0
            radNums[k] *= i
            k += i

dict = dict(zip(range(len(radNums)), radNums))

sorted_x = sorted(dict.items(), key=operator.itemgetter(1))

#print(sorted_x)
print(sorted_x[10000])