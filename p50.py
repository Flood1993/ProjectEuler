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
    
def numprimes(n):
    '''given an integer, returns the number of primes summed, starting by 2, so that X < n is maximum'''
    num = 0
    sum = 0
    while sum + primes[num] < n:
        sum = sum + primes[num]
        num = num+1
    return num
    
primes = []
for i in range(2, 1000000):
    if isprime(i):
        primes.append(i)


primthou = numprimes(1000000)
#24 numeros necesarios para que la suma de primos empezando en 2 sea menor que 1000

maxterms = 0
maxsum = 0
for i in range(0, primthou):
    sum = 0
    terms = 0
    j = i
    while j < primthou + i and sum < 1000000:
        sum = sum + primes[j]
        terms = terms + 1
        if isprime(sum) and terms > maxterms:
            maxterms = terms
            maxsum = sum
        j = j+1
        
print maxsum
print maxterms