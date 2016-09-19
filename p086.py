"""
Buscamos pythagorean triplets con lados pequeños <= M

Generate all discting pythagorean triplets such that the big side <= M

The box can be arranged so that the bigger side is the one to be splitted???
"""

from functions import pythTriplet, gcd
import sys

M = int(sys.argv[1])
total_sols = 0

already_tested = set()

for i in range(2, M//2):
    for j in range(1, i):
        #if (i+j) % 2 == 0:
        #    continue
        #if gcd(i, j) != 1:
        #    continue
        p = pythTriplet(i, j)
        #inverted = False
        if p[0] > p[1]: # p2 is guaranteed not to be smaller than p1/p2
            p[0], p[1] = p[1], p[0]
            #inverted = True
        p0, p1, p2 = p[0], p[1], p[2]
        while max(p[0], p[1], p[2]) <= M:
            if not (p[0], p[1], p[2]) in already_tested:
                #if inverted:
                #    total_sols += p[1] - 1
                #else:
                #    total_sols += p[0] - 1
                total_sols += p[0] - 1

                already_tested.add((p[0], p[1], p[2]))
            p[0] += p0
            p[1] += p1
            p[2] += p2

print(total_sols)