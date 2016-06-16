# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:22:55 2013

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
    

valores = [3]
def actvalores(n):
    for i in range (0,n):
        x = valores[i]
        valores.append(int(x) + 8*(i+2) - 6)
    

def valor(n):
    #da el valor de la esquina menor de la iteracion n
    return valores[n]


nprimos = []
ntotal = [1]

def addnumbers(n):
    #añade los correspondientes numeros a las listas para la iteracion n
        x = valor(n)
        if (isprime(x)):
            nprimos.append(x)
        if (isprime(x + 2*(n+1))):
            nprimos.append(x + 2*(n+1))
        if (isprime(x + 4*(n+1))):
            nprimos.append(x + 4*(n+1))
        if (isprime(x + 6*(n+1))):
            nprimos.append(x + 6*(n+1))
            
        ntotal.append(x)
        ntotal.append(x+2*n)
        ntotal.append(x+4*n)
        ntotal.append(x+6*n)



actvalores(20000)
#valores contiene los 20000 primeros valores menores de las esquinas
#number obtained by bruteforcing

addnumbers(0)
cont = 1
while double(len(nprimos))/double(len(ntotal)) > 0.1:
    addnumbers(cont)
    cont = cont + 1
    
print 2*cont + 1