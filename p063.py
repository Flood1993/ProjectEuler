# -*- coding: utf-8 -*-
"""
Created on Thu May 16 01:43:53 2013

@author: guillermo
"""

def numcifras(n):
    return len(str(n))

#exp = 1
#while numcifras(9**exp) == exp:
#    exp = exp+1
#print exp
"""a partir de 9**22, el numero obtenido tiene una cifra menos que el exponente"""

res = 0
for i in range(1,10):
    for j in range(1, 23):
        if numcifras(i**j) == j:
            res = res+1
            
print res