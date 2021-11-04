from functions import primes_up_to
from collections import defaultdict

LIMIT = 120000

primes = primes_up_to(LIMIT)

factors = defaultdict(set)

rads = dict()

for p in primes:
    current = p
    while current <= LIMIT:
        factors[current].add(p)
        current = current + p

def get_factors(n):
    return factors[n]

def rad(n):
    factors = get_factors(n)
    result = 1
    for f in factors:
        result = result * f
    return result

rads[1] = 1
for i in range(2, LIMIT):
    rads[i] = rad(i)

def sort_rads(element):
    return element[1]

rads_list = [(k, v) for k, v in rads.items()]
rads_list.sort(key=sort_rads)  # list of tuples (n, rad(n)), sorted by rad(n)

print('Generated factors for odd numbers, EASY')


def coprimes(factors_x, factors_y):
    factors_x_y = set()
    for factor in factors_x:
        factors_x_y.add(factor)
    for factor in factors_y:
        factors_x_y.add(factor)
    return len(factors_x) + len(factors_y) == len(factors_x_y)


abc_hit_count = 0
result = 0
for idx_b, (b, rad_b) in enumerate(rads_list):
    if idx_b == 0:
        continue
    if rad_b >= LIMIT//2:
        break
    factors_b = get_factors(b)
    for idx_a, (a, rad_a) in enumerate(rads_list):
        if a >= b:
            continue
        if rad_a >= LIMIT//2:
            continue
        rad_ab = rad_a * rad_b
        if rad_ab >= LIMIT:
            break
        factors_a = get_factors(a)
        if not coprimes(factors_a, factors_b):
            continue

        c = a + b
        if c >= LIMIT:
            continue
        
        factors_c = get_factors(c)

        if not coprimes(factors_a, factors_c) or not coprimes(factors_b, factors_c):
            continue

        rad_c = rads[c]
        if rad_ab * rad_c < c:
            result = result + c
            abc_hit_count = abc_hit_count + 1
print(abc_hit_count, result)
