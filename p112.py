# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:09:53 2013

@author: guillermo
"""


def bouncy(n):
    #returns whether a number is bouncy
    
    string = str(n)
    pos = 0
    isinc = False
    isdec = False
    found = False
    
    #While we haven't found it, we check all digits from 0 to len(string)-1
    while pos < len(string) - 1 and not found:
        #If any digit is greater than the next, it will be dec
        if int(string[pos]) > int(string[pos+1]):
            isdec = True
        #If any digit is lesser than the next, it will be inc
        if int(string[pos]) < int(string[pos+1]):
            isinc = True
        
        #If it is dec and inc, it is bouncy
        if isinc and isdec:
            found = True
            
        pos += 1
    
    #Is it bouncy?
    return found
    
cont = 100
bouncies = 0.0
total = 99.0
lastb = 0.0
target = 0.99

while bouncies / total != target:
    if bouncy(cont):
        bouncies += 1
        lastb = cont
    
    total += 1
    
    cont += 1
    
print lastb