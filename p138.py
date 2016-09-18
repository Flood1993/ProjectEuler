"""
We are looking for the first 12 pythagorean triplets such that for the non diagonal terms, abs(big - 2*small) == 1

Given a number m, we want to generate the pythagorean triplet closes to:

t = (t0, t1, t2),
with
t0 = m*m - n*n
t1 = 2*m*n
We want to get abs(max(t0, t1) - 2*min(t0, t1)) = 1

abs(m*m - n*n - 2(2*m*n)) == 1
abs(2(m*m - n*n) - (2*m*n)) == 1

There are 4 cases:

a) m*m - n*n - 2(2*m*n) == 1
b) m*m - n*n - 2(2*m*n) == -1
c) 2(m*m - n*n) - (2*m*n) == 1
d) 2(m*m - n*n) - (2*m*n) == -1

For each m, we need to check all of them

a) 
mm - nn - 4mn = 1
mm - 1 = nn - 4mn
mm - 1 = nn - 4mn + 4mm - 4mm
mm - 1 = (n - 2m)**2 - 4mm
5mm - 1 = (n - 2m)**2
sqrt(5mm - 1) = n - 2m
n = sqrt(5mm - 1) + 2m

b)
mm - nn - 4mn = -1
mm + 1 = nn - 4mn
mm + 1 = nn - 4mn + 4mm - 4mm
mm + 1 = (n - 2m)**2 - 4mm
5mm + 1 = (n - 2m)**2
sqrt(5mm + 1) = n - 2m
n = sqrt(5mm + 1) + 2m

c) 
2(mm - nn) - 2mn = 1
2mm - 2nn - 2mn = 1
2mm - 1 = 2nn + 2mn
2mm - 1 = 2nn + 2mn + mm/2 - mm/2      # a = sqrt(2)*n    b = m/sqrt(2)
2mm - 1 = (sqrt(2)n + m/sqrt(2))**2 - mm/2
2mm - 1 + mm/2 = (sqrt(2)n + m/sqrt(2))**2
(5mm - 2)/2 = (sqrt(2)n + m(sqrt(2))**2
n = (sqrt(5mm - 2) - m)/2

d)
n = (sqrt(5mm + 2) - m)/2


First example:
m = 4, n = 1 gives (15, 8, 17)

Second example:
What gives  (136, 273, 305)?

n = 

m = 17, n = 4
"""

from functions import pythTriplet, gcd
import sys
from math import ceil, floor
"""
LIMIT = int(sys.argv[1])

for m in range(2, LIMIT):
    n = m*(2**0.5) - m
    n1 = floor(n)
    n2 = ceil(n)
    if (n1 + m) % 2 == 1:
        t = pythTriplet(m, n1)
        small = min(t[0], t[1])
        big = max(t[0], t[1])
        if abs(big - 2*small) == 1:
            print(t)

    if (n2 + m) % 2 == 1:
        t = pythTriplet(m, n2)
        small = min(t[0], t[1])
        big = max(t[0], t[1])
        if abs(big - 2*small) == 1:
            print(t)
"""


# LIMIT = int(sys.argv[1])

"""
def pos(m):
    # Returns a set with all possible n values, given m
    res = set()

    n1 = (5*m*m + 1)**0.5 - 2*m
    n2 = (5*m*m - 1)**0.5 - 2*m
    n3 = ((5*m*m - 2)**0.5 - m)/2
    n4 = ((5*m*m + 2)**0.5 - m)/2

    res.add(floor(n1))
    res.add(ceil(n1))
    res.add(floor(n2))
    res.add(ceil(n2))
    res.add(floor(n3))
    res.add(ceil(n3))
    res.add(floor(n4))
    res.add(ceil(n4))

    return res

def check_condition(m):
    c = pos(m)
    for n in c:
        t = pythTriplet(m, n)
        if abs(max(t[0], t[1]) - 2*min(t[0], t[1])) == 1:
            print(t)

for i in range(2, LIMIT):
    check_condition(i)

# Yields the series http://oeis.org/A007805
"""

hypotenuses = [17, 305, 5473, 98209, \
1762289, 31622993, 567451585, 10182505537, \
182717648081, 3278735159921, 58834515230497, 1055742538989025]

print(sum(hypotenuses))

"""
182717648081
1055742538989025

"""



