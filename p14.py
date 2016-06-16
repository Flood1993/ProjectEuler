# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:13:33 2013

@author: guillermo
"""

def collatzterms(n):
#    returns the number of terms produced by the collatz sequence for n
    res = 1
    while n !=1:
        if n%2 == 0: #n is even
            n = n/2
        else: #n is odd
            n = 3*n + 1
        res = res+1
    
    return res

maxterms = 0
maxnum = 0

for i in range(3, 1000000, 2):
    x = collatzterms(i)
    if (x > maxterms):
        maxnum = i
        maxterms = x
        
print str(maxnum)