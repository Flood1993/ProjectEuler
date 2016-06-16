# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:50:02 2013

@author: guillermo
"""

def sumdigs(n):
    #returns the sum of the digits of a number
    string = str(n)
    res = 0
    for i in range(0, len(string)):
        res += int(string[i])
        
    return res

A = []
#A shall contain the numbers with that property
for i in range(3, 70):
    for j in range(2, 50):
        if sumdigs(i**j) == i:
            A.append(i**j)

A.sort() 
print A
        