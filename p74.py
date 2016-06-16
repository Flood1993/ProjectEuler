import math

def digfact(n):
    res = 0
    string = str(n)
    for i in range(0, len(string)):
        res = res + math.factorial(int(string[i]))
    return res
    

def termschain(n):
    A = []
    #metemos el primer elemento
    A.append(n)
    
    #calculamos la primera iteracion
    res = digfact(n)
    
    #si es diferente al elemento inicial
    while res != n:
        #si ya lo hemos metido en A
        if res in A:
            break
        A.append(res)
        res = digfact(res)
        
        
    return len(A)

cont = 0
for i in range(0, 1000000):
    if termschain(i) == 60:
        cont = cont+1
        
print str(cont)
