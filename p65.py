# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:22:42 2013

@author: guillermo
"""
from fractions import Fraction

A = [2.0, 1.0, 2.0, 1.0, 1.0, 4.0, 1.0, 1.0, 6.0, 1.0, 1.0, 8.0, 1.0, 1.0, 10.0, 1.0, 1.0, 12.0, 1.0, 1.0, 14.0, 1.0, 1.0, 16.0, 1.0, 1.0, 18.0, 1.0, 1.0, 20.0, 1.0, 1.0, 22.0, 1.0, 1.0, 24.0, 1.0, 1.0, 26.0, 1.0, 1.0, 28.0, 1.0, 1.0, 30.0, 1.0, 1.0, 32.0, 1.0, 1.0, 34.0, 1.0, 1.0, 36.0, 1.0, 1.0, 38.0, 1.0, 1.0, 40.0, 1.0, 1.0, 42.0, 1.0, 1.0, 44.0, 1.0, 1.0, 46.0, 1.0, 1.0, 48.0, 1.0, 1.0, 50.0, 1.0, 1.0, 52.0, 1.0, 1.0, 54.0, 1.0, 1.0, 56.0, 1.0, 1.0, 58.0, 1.0, 1.0, 60.0, 1.0, 1.0, 62.0, 1.0, 1.0, 64.0, 1.0, 1.0, 66.0, 1.0]

aux = 99

fraction = Fraction (1.0/A[aux])
for i in range(aux-1, -1, -1):
    fraction = fraction + Fraction(A[i])
    if i != 0:
        fraction = Fraction(1/fraction)

print fraction

num = fraction.numerator
strnum = str(num)

result = 0
for i in range(0, len(strnum)):
    result += int(strnum[i])

print result