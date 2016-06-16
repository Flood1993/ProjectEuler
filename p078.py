# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:58:24 2013

@author: guillermo
"""
scope = 70000
numbers = range(1,scope)

ways = [1]+[0]*scope
 
for number in numbers:
    for i in range(number, scope+1):
        ways[i] += ways[i-number]
#        if ways[i] % 1000000 == 0:
#            print ways[i]
#            break
i = 0
while i < len(ways):
    if ways[i] % 1000000 == 0:
        print i
        print ways[i]
        break
    i = i+1
    
#Se puede hacer mas rapido con la Euler's generating function, que relacion    
    
#55374
#Tarda la puta vida en verso en acabar