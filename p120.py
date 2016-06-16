# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 21:43:23 2013

@author: guillermo
"""

total = 0

for i in range(3, 1001):
    maxremainder = 0
    square = i**2
    minus1 = i-1
    plus1 = i+1
    for j in range(0, 2*i):
        remainder = ( minus1**j + plus1**j ) % square
        if remainder > maxremainder:
            maxremainder = remainder
    if i == 7:
        print maxremainder
    total += maxremainder
    
print total
#MAXIMUM BRUTE FORCE BITCHA