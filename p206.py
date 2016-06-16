# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:46:27 2013

@author: guillermo
"""

#1_2_3_4_5_6_7_8_9_0
'''
1010101010^2 < 1020304050607080900
1389026624^2 > 1929394959697989990
'''
def check(n):
    n2 = n**2
    n2s = str(n2)
    if n2s[0] == '1' and n2s[2] == '2' and n2s[4] == '3' and n2s[6] == '4' and n2s[8] == '5' and n2s[10] == '6' and n2s[12] == '7' and n2s[14] == '8' and n2s[16] == '9' and n2s[18] == '0':
        return True
    return False
        

#for i in range(1010101010, 1389026624, 10):
#    if check(i):
#        print i
#        break

#RESULT: 1389019170