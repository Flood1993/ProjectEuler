# -*- coding: utf-8 -*-
"""
Created on Wed May 15 01:44:38 2013

@author: guillermo
"""

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    


cont = 0
last = 0

i = 2;
while (cont <= 10000):
    if isprime(i):
        cont = cont+1
        last = i
    i = i+1
    
print str(i-1)