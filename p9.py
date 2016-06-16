# -*- coding: utf-8 -*-
"""
Created on Wed May 15 02:18:04 2013

@author: guillermo
"""
res = 0

for a in range(1, 999):
    for b in range(2,999-a):
        c = 1000-b-a
        
        if a**2 + b**2 == c**2:
            res = a*b*c
        
print str(res)