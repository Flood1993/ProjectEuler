# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:57:40 2013

@author: guillermo
"""

def numdig(n):
    x = str(n)
    return len(x)

def odddig(n):
    x = str(n)
    for i in range(0, len(x)):
        if int(x[i])%2 == 0:
            return False
    return True
    
def rev(n):
    if numdig(n) != numdig(int(str(n)[::-1])):
        return False
    aux = n + int(str(n)[::-1])
    return odddig(aux)
    
#res = 0
#for i in range(0, 1000):
#    if odddig(i + int(str(i)[::-1])):
#        res = res+1
#        
#print res

res = 0
for i in range(100000000,1000000001):
    if rev(i):
        res = res+1
#        print i
print res
