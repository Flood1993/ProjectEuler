import sys
from math import floor
from functions import gcd

INPUT = int(sys.argv[1])

def continued_fraction(x):
    """
    Returns the continued fraction of x as a list of tuples (a,b,c),
    where:

        a + (sqrt(x)+b / c)

    represents each step.
    
    If we are interested on the notation of the form [4;(1,3,1,8)],
    we must take the first value from each tuple.

    Note: Be careful if the value passed is a perfect square.
    """
    res = []

    a = floor(x**0.5)
    b = -floor(x**0.5)
    c = 1    

    t = (a,b,c)
    res.append(t)

    while True:
        a, b, c = res[-1][0], res[-1][1], res[-1][2]
        a1 = floor(c*(x**0.5 - b)/(x - b*b))
        b1 = -b * c
        c1 = x - b*b
        b1 -= a1*c1

        _gcd = gcd(b1, c1)
        _gcd = gcd(_gcd, c)
        b1 //= _gcd
        c1 //= _gcd
        
        t = (a1, b1, c1)
        
        if t in res: # All continued fractions are periodic
            res.append(t)
            break

        res.append(t)
    
    return res

def period_continued_fraction(x):
    cf = continued_fraction(x)
    t = cf[-1]
    total = len(cf)

    i = 0
    while i < total:
        if cf[i] == t:
            break
        i += 1

    return total - i - 1

sols = 0

for i in range(2, INPUT + 1):
    sqr = int(i**0.5)
    if sqr*sqr == i:
        continue
    l = period_continued_fraction(i)
    if l % 2 == 1:
        sols += 1

print(sols)
