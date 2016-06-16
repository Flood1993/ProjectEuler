# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:32:34 2013

@author: guillermo
"""

from fractions import Fraction

fraction = Fraction(3.0/2.0)

def nextfraction(n):
    #Returns the next fraction of the series
    return Fraction( Fraction(1.0) + ( Fraction(1.0)/(Fraction(1.0) + n) ) )


count = 0
for i in range(0, 999):
    fraction = nextfraction(fraction)
    if len(str(fraction.numerator)) > len(str(fraction.denominator)):
        count += 1
        
print count