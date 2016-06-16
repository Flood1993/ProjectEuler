from sets import Set

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
    
def squarefree(n):
    A = primedivs(n)
    for i in range(0, len(A)):
        if A[i][1] != 1:
            return False
    return True    
    
facts = [1]
#facts contiene todos los valores de los factoriales en el intervalo [0,51]
for i in range(1, 52):
    facts.append(i * facts[i-1])
    
A = Set()
#A contiene todos los elementos del triangulo de pascal en las 51 primeras filas (sin repetir)
for n in range(0, 52):
    for k in range(0, (n/2) + 1):
        A.add(facts[n]/(facts[k] * facts[n-k]))
   
res = 0     
for i in A:
    if squarefree(i):
        res += i

print res