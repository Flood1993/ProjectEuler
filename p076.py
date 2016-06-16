# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:28:41 2013

@author: guillermo
"""
target = 100
numbers = [i for i in range(1, 100)]
ways = [1]+[0]*target
 
for number in numbers:
  for i in range(number, target+1):
    ways[i] += ways[i-number]
 
print ways[target]