# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:39:45 2013

@author: guillermo
"""

f = open('poker.txt', 'r')
#Open the file poker.txt as f

P1 = []
P2 = []

def getcards():
    #modifies P1 and P2 so that they contain the next hands
    global P1, P2
    
    line = str(f.readline())
    #We read the next line
    
    P1aux = []
    P1aux.append(line[0:2])
    P1aux.append(line[3:5])
    P1aux.append(line[6:8])
    P1aux.append(line[9:11])
    P1aux.append(line[12:14])
    
    P2aux = []
    P2aux.append(line[15:17])
    P2aux.append(line[18:20])
    P2aux.append(line[21:23])
    P2aux.append(line[24:26])
    P2aux.append(line[27:29])
    
    #Modify values
    P1 = P1aux
    P2 = P2aux


def cardsvalues(A):
    #returns a list showing the value of the cards of a hand
       # 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A.
    n = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]
    for i in A:
        #for every card, we check their value
        if i[0] == '2':
            n[0] = n[0]+1
        if i[0] == '3':
            n[1] = n[1]+1
        if i[0] == '4':
            n[2] = n[2]+1
        if i[0] == '5':
            n[3] = n[3]+1
        if i[0] == '6':
            n[4] = n[4]+1
        if i[0] == '7':
            n[5] = n[5]+1
        if i[0] == '8':
            n[6] = n[6]+1
        if i[0] == '9':
            n[7] = n[7]+1
        if i[0] == 'T':
            n[8] = n[8]+1
        if i[0] == 'J':
            n[9] = n[9]+1
        if i[0] == 'Q':
            n[10] = n[10]+1
        if i[0] == 'K':
            n[11] = n[11]+1
        if i[0] == 'A':
            n[12] = n[12]+1
    return n
    
#ASSUMING WE ALWAYS CHECK FROM HIGHER TO LOWER

def royalflush(A):
    #returns whether a hand is a royal flush
    if not flush(A):
        return False
    else:
        B = cardsvalues(A)
        return B[12] == 1 and B[11] == 1 and B[10] == 1 and B[9] == 1 and B[8] == 1
        
def straightflush(A):
    #returns whether a hand is a straight flush
    return straight(A) and flush(A)
    
def fourofakind(A):
    #returns whether a hand is a four of a kind
    B = cardsvalues(A)
    for i in B:
        if i == 4:
            return True
    return False
    
def fullhouse(A):
    #returns whether a hand is a full house
    two = False
    three = False
    B = cardsvalues(A)
    for i in B:
        if i == 2:
            two = True
        elif i == 3:
            three = True
    return two and three
    
def flush(A):
    #returns whether a hand is a flush
    suit = A[0][1]
    #suit to compare
    for i in A:
        #for every card, we check if all suits match the first one
        if i[1] != suit:
            return False
    return True
    
def straight(A):
    #returns whether a hand is a straight
    B = cardsvalues(A)
    for i in range(0, len(B)-4):
        if B[i] == 1 and B[i+1] == 1 and B[i+2] == 1 and B[i+3] == 1 and B[i+4] == 1:
            return True
    return False
    
def threeofakind(A):
    #returns whether a hand is a three of a kind
    B = cardsvalues(A)
    for i in B:
        if i == 3:
            return True
    return False
    
def twopairs(A):
    #returns whether a hand is two pairs
    one = False
    two = False
    B = cardsvalues(A)
    for i in B:
        if i == 2 and not one:
            one = True
        elif i == 2:
            two = True
    return one and two
    
def onepair(A):
    #returns whether a hand is a one pair
    B = cardsvalues(A)
    for i in B:
        if i == 2:
            return True
    return False
    
def highcard(A):
    #returns THE VALUE of the highest card in A
    B = cardsvalues(A)
    first = 0
    
    i = len(B)-1
    while i >= 0 and first == 0:
        if B[i] != 0:
            first = i+2
        i = i-1
            
#    if i == 10:
#        return T
#    elif i == 11:
#        return J
#    elif i == 12:
#        return Q
#    elif i == 13:
#        return K
#    elif i == 14:
#        return A
    return first

#def whichhighcard(A, B):
#    #Given 2 hands, returns 1 if A has a greatest higher card than B, 2 in the other case
#    cardsa = cardsvalues(A)
#    cardsb = cardsvalues(B)
#    
#    one = False
#    two = False
#    three = False
#    four = False
#    
#    i = len(A)-1
#    
#    while i >= 0:
#        while not one:
#            while not two:
#                while not three:
#                    while not four:
#                        if cardsa[i] == 1 and cardsb[i] == 1:
#                            i = i-1
#                            four = True
#                            break
#                        elif cardsa[i] == 1 and cardsb[i] != 1:
#                            return 1
#                        elif cardsa[i] != 1 and cardsb[i] == 1:
#                            return 2
#                        i = i-1
#                    if cardsa[i] == 1 and cardsb[i] == 1:
#                        i = i-1
#                        three = True
#                        break
#                    elif cardsa[i] == 1 and cardsb[i] != 1:
#                        return 1
#                    elif cardsa[i] != 1 and cardsb[i] == 1:
#                        return 2
#                    i = i-1
#                if cardsa[i] == 1 and cardsb[i] == 1:
#                    i = i-1
#                    two = True
#                    break
#                elif cardsa[i] == 1 and cardsb[i] != 1:
#                    return 1
#                elif cardsa[i] != 1 and cardsb[i] == 1:
#                    return 2
#                i = i-1
#            if cardsa[i] == 1 and cardsb[i] == 1:
#                i = i-1
#                one = True
#                break
#            elif cardsa[i] == 1 and cardsb[i] != 1:
#                return 1
#            elif cardsa[i] != 1 and cardsb[i] == 1:
#                return 2
#            i = i-1
#        if cardsa[i] == 1 and cardsb[i] != 1:
#                return 1
#        elif cardsa[i] != 1 and cardsb[i] == 1:
#                return 2
#        i = i-1
    

def valhand(A):
    '''returns a number according to the corresponding hand: 
    High Card: 9
    One Pair: 8
    Two Pairs: 7
    Three of a Kind: 6
    Straight: 5
    Flush: 4
    Full House: 3
    Four of a Kind: 2
    Straight Flush: 1
    Royal Flush: 0       '''
    if royalflush(A):
        return 0
    elif straightflush(A):
        return 1
    elif fourofakind(A):
        return 2
    elif fullhouse(A):
        return 3
    elif flush(A):
        return 4
    elif straight(A):
        return 5
    elif threeofakind(A):
        return 6
    elif twopairs(A):
        return 7
    elif onepair(A):
        return 8
    else:
        return 9
        
def comp(p1, p2):
    #returns 1 if p1 is a better hand than p2
    if valhand(p1) < valhand(p2):
        return 1
    elif valhand(p1) > valhand(p2):
        return 2
        
    #at this point, it has been a tie, so we have to check again
    return desempate(p1, p2)
        
def desempate(A, B):
    #We dont need to check the royal flush since there is a clear winner
    
    if valhand(A) == 1:
        #it's a straight flush
        if highcard(A) > highcard(B):
            return 1
        return 0
            
    elif valhand(A) == 2:
        #it's a fourofakind
        cardsa = cardsvalues(A)
        cardsb = cardsvalues(B)
        i = len(cardsa)-1
        while i >= 0:
            if cardsa[i] == 4:
                return 1
            if cardsb[i] == 4:
                return 2
            i = i-1
            
    elif valhand(A) == 3:
        #it's a full house
        three = False
        cardsa = cardsvalues(A)
        cardsb = cardsvalues(B)
        i = len(cardsa)-1
        while i >= 0:
            if not three:            
                if cardsa[i] == 3 and cardsb[i] == 3:
                    i = i-1
                    three = True
                    continue
                elif cardsa[i] == 3 and cardsb[i] != 3:
                    return 1
                elif cardsa[i] != 3 and cardsb[i] == 3:
                        return 2
            else:
                if cardsa[i] == 2 and cardsb[i] != 2:
                    return 1
                elif cardsa[i] != 2 and cardsb[i] == 2:
                    return 2
            i = i-1
            
    elif valhand(A) == 4:
        #it's a flush
        if highcard(A) > highcard(B):
            return 1
        return 0
        
    elif valhand(A) == 5:
        #it's a straight
        if highcard(A) > highcard(B):
            return 1
        return 0
        
    elif valhand(A) == 6:
        #it's a three of a kind
        cardsa = cardsvalues(A)
        cardsb = cardsvalues(B)
        i = len(cardsa)-1
        while i >= 0:
            if cardsa[i] == 3:
                return 1
            if cardsb[i] == 3:
                return 2
            i = i-1
            
    elif valhand(A) == 7:
        #it's a two pairs
        two = False
        cardsa = cardsvalues(A)
        cardsb = cardsvalues(B)
        i = len(cardsa)-1
        while i >= 0:
            if not two:            
                if cardsa[i] == 2 and cardsb[i] == 2:
                    i = i-1
                    two = True
                    continue
                elif cardsa[i] == 2 and cardsb[i] != 2:
                    return 1
                elif cardsa[i] != 2 and cardsb[i] == 2:
                        return 2
            else:
                if cardsa[i] == 2 and cardsb[i] != 2:
                    return 1
                elif cardsa[i] != 2 and cardsb[i] == 2:
                        return 2
            i = i-1
    
    elif valhand(A) == 8:
        #it's a pair
        cardsa = cardsvalues(A)
        cardsb = cardsvalues(B)
        i = len(cardsa)-1
        while i >= 0:
            if cardsa[i] == 2:
                return 1
            if cardsb[i] == 2:
                return 2
            i = i-1
            
    else:
        #its a high card
        if highcard(A) > highcard(B):
            return 1
        return 0
    
    
res = 0
#hands won by player 1
for i in range(0, 1000):
    getcards()
    if comp(P1, P2) == 1:
        print i+1
        res = res+1
        
#print res

#hand1 = ['3S', '5C', '6C', '7C', '9C']
#hand2 = ['4S', '5C', '6C', '7C', '9C']
#print whichhighcard(hand1, hand2)

#DA 377, la respuesta es 376
#El fallo esta en la linea 25.
# 6D 7C 5D 5H 3S 5C JC 2H 5S 3D
#Pareja por desempate a carta alta, tener cuidado
'''HAY QUE ARREGLAR QUE SI ES A CARTA MAS ALTA, SI LA MAS ALTA ES IGUAL, COMPRUEBE LA SEGUNDA, ETC'''