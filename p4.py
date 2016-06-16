# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/guillermo/.spyder2/.temp.py
"""
found = False
res = 0

for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        
        aux = i*j
        string = str(aux)
        inv = string[::-1]
        
        if string == inv and aux > res:
            res = int(string)

print str(res)