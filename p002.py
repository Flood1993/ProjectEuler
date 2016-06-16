# -*- coding: utf-8 -*-
"""
Created on Wed May 15 01:35:43 2013

@author: guillermo
"""

a = 1
b = 1
c = a+b

res = 0

while c < 4000000:
    if c%2 == 0:
        res += c
    a = b
    b = c
    c = a+b

print str(res)    