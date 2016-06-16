# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:46:40 2013

@author: guillermo
"""
import math

def sumatorio(n):
    #devuelve el valor del sumatorio de 1 a n
    return (n*(n+1))/2
    
def mindifsumatorio(n):
    #devuelve el valor x para el cual la diferencia del sumatorio de 1 a (x-1) con el sumatorio de (x+1) a n es mínima
    val = math.floor(n/2)
    
    res = sumatorio(n)
    
    while val <= n:
        if sumatorio(n) - 
