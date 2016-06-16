# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:12:20 2013

@author: guillermo
"""

def howmanydiv(n):
    """returns the number of divisors of a number"""
    limit = n
    number = 0
    i = 1
    while i < limit:
        if n%i == 0:
            limit = n/i
            if limit != 1:
                number = number+1
            number = number+1
        i = i+1
    return number

def triangular(n):
    """returns the nth triangular number"""
    return (n*(n+1))/2
    
x = 1

while howmanydiv(triangular(x)) < 500:
    x = x+1
    
print str(triangular(x))

#print str(triangular(x))
#print str(howmanydiv(triangular(x)))