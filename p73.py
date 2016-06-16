from sets import Set
from fractions import Fraction

half = 1.0/2.0
third = 1.0/3.0
A = Set()
for den in range(6001, 12001):
    for num in range(den/3, (den/2)+1):
        if double(num)/double(den) > third and half > double(num)/double(den):
            x = Fraction(num, den)
            A.add(x)
            
print len(A)