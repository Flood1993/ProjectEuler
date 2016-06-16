# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:13:01 2013

@author: guillermo
"""

def isprime(n):
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
    
A = []

for i in range(2, 1000000):
    if isprime(i):
        A.append(i)
        
for pos in range(0, len(A)):
    if ( (A[pos]-1)**pos + (A[pos]+1)**pos ) % A[pos]**2 > 10000000000:
        print pos
        print A[pos]
        print ( (A[pos]-1)**pos + (A[pos]+1)**pos ) % A[pos]**2 
        break
#10000000000 = 10^10

#La respuesta obtenida con este código es 21033, pero la real es 21035