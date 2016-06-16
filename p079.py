# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:31:18 2013

@author: guillermo
"""

f = open('keylog.txt', 'r')
res = 0
for line in f:
    res = res+int(line)
print res