# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:39:15 2013

@author: guillermo
"""
cont = 0

def gcd(n, m):
    global cont
    cont += 1
    if n == m:
        return
    elif m > n:
        return gcd(m, n)
#    elif m == 1:
#        return
    elif n%m != 0:
        return gcd(n, n%m)

benchmark = 11000
for i in range(1, benchmark):
    for j in range(1, benchmark):
        gcd(i, j)
        
print cont       