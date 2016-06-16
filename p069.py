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
    
    if isprime(n):
        A.append([n, 1])
        
    else:
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
   
#print double(7)/double(totient(7))
n = 0
maximum = 0
for i in range(30030, 1000001, 30030):
    x = double(i)/double(totient(i))
    if x > maximum:
        maximum = x
        n = i

print n