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
        p = pythTriplet(i, j)

        if p[0] > p[1]: # p2 is guaranteed not to be smaller than p1 or p2
            p[0], p[1] = p[1], p[0]
        p0, p1 = p[0], p[1]
        while max(p[0], p[1]) <= M:
            if not (p[0], p[1]) in already_tested:
                #total_sols += p[0] - 1
                cnt = 0
                for i in range(1, p[1]//2 + 1):
                    if (p[0]+i)**2 + (p[1]-i)**2 >= p[2]:
                        cnt += 1
                for i in range(1, p[0]//2 + 1):
                    if (p[1]+i)**2 + (p[0]-i)**2 >= p[2]:
                        cnt += 1
                total_sols += cnt
                #total_sols += p[0]//2 + p[1]//2
                already_tested.add((p[0], p[1]))
            p[0] += p0
            p[1] += p1

print(total_sols)

"""
The cuboid measures at maximum NxNxN.

We want to find pythagorean triplets with max(a, b) <= N

Let's say our cuboid measures XxYxZ. If we found the pythagorean triplet 6, 8, 10. We are interested in 6,8. This could mean We have to check, for All the triplet of the form 6,a,8-a, how many have the shortest side integral. Also, for the triplets of 8,a,6-a.

6 1 7
6 2 6
6 3 5
6 4 4

8 1 5
8 2 4
8 3 3

-> This would up those 7 cases
"""
