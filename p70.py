def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
def digits(n):
    '''returns a list containing the number of appareances of each digit'''
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    string = str(n)
    for i in range(0, len(string)):
        A[int(string[i])] = A[int(string[i])] + 1
    return A
    
def comparedigits(n, m):
    '''returns whether two numbers have the same digits'''
    N = digits(n)
    M = digits(m)
    
    res = True    
    i = 0
    while i < 10 and res:
        if N[i] != M[i]:
            res = False
        i = i+1
    
    return res
    
def primedivs(n):
    """returns a list of prime divisors of a number, containing [prime divisor, max exponent]"""
    A = []
    for i in range (2, n/2 + 1):
        if isprime(i) and n%i == 0:
            exp = 0
            aux = n
            while aux%i == 0:
                exp = exp + 1
                aux = aux/i
            A.append([i, exp])
    return A
    
def totient(n):
    res = 1
    
    A = primedivs(n)
    for i in range(0, len(A)):
        if A[i][1] == 1:
            res = res * (A[i][0] - 1)
        else:
            res = res * (A[i][0] - 1) * A[i][0]**(A[i][1] - 1)
    return res
    
L = []
for i in range(2000, 4000):
    #L contiene todos los primos entre 2000 y 4000
    if isprime(i):
        L.append(i)
        
i = 0
while i < len(L):
    j = i
    while j < len(L):
        if L[j]*L[i] > 10000000:
            j += 1
            continue
        elif comparedigits(L[i]*L[j], (L[i]-1)*(L[j]-1)):
            print L[i]
            print L[j]
            print L[i]*L[j]
            print (L[i]-1)*(L[j]-1)
            print double(L[i]*L[j])/double((L[i]-1)*(L[j]-1))
            print 
        
        j += 1
    i += 1
    
#NOTA: esto te devuelve una lista de valores, hay que encontrar el minimo a mano.