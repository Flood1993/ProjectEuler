# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:02:05 2013

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
    
def howmanyprimedivs(n):
    """returns how many different prime divisors has n"""
    res = 0
    for i in range (2, int(n**0.5)+1):
        if isprime(i) and n%i == 0:
            res = res + 1
        if n%i == 0 and isprime(n/i) and n/i != i:
            res = res + 1
    return res

n1 = 0
n2 = 0
n3 = 0
n4 = 0

cont = 300
found = False
while not found:
    n1 = cont
    n2 = cont+1
    n3 = cont+2
    n4 = cont+3
    
    D1 = howmanyprimedivs(n1)
    D2 = howmanyprimedivs(n2)
    D3 = howmanyprimedivs(n3)
    D4 = howmanyprimedivs(n4)
    
    if D1 == 4:
        if D1 == D2 and D1 == D3 and D1 == D4:
            found = True
            
    cont = cont+1
    
print n1