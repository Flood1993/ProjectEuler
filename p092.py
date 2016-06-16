# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:09:44 2013

@author: guillermo
"""
#Para los números menores que 10.000.000
#Valor maximo = 9^2 * 7 = 567
#Necesitamos mirar para todos esos números si acaban en 89
array = [False]*567

def endsin89(n):
    while n != 89 and n != 1:
        st = str(n)
        n = 0
        
        for i in range(0, len(st)):
            n = n + int(st[i])**2
            
        if n == 89:
            return True
        elif n == 1:
            return False

res = 0

#Inicializamos array
for i in range(0, len(array)):
    if endsin89(i):
        array[i] = True
        
def checkarray(n):
    global array
    aux = 0
    st = str(n)
        
    for i in range(0, len(st)):
        aux = aux + int(st[i])**2
    return array[aux]
    
res = 0
for i in range(0, 10000000):
    if checkarray(i):
        res += 1
        
print res