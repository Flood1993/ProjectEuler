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

def almdigits(n):
    '''returns a list containing the number of appareances of each digit, counting all except the last one'''
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    aux1 = str(n)
    
    for i in range(0, len(aux1) - 1):
        A[int(aux1[i])] = A[int(aux1[i])] + 1
    return A
    
def family(n):
    '''returns the number of prime elements in a number family according to the specification'''
    D = almdigits(n)
    '''una vez encontrado el numero de apariciones de cada digito, sin contar el ultimo, habra que cambiar
    los digitos que aparecen mas de una vez (hasta len(n)-1) por cada digito, y despues mirar si es primo'''
    
    total = 0

#    print D
    
    for dig in range(0, len(D)):
        #for each digit
        
#        print "We are currently checking digit: " + str(dig)
        
        count = 0
        #we need a count for every digit        
        
        if D[dig] > 1:
            for replace in range(0, 10):
                #if it appears more than once, we replace it with all possible values

#                print "we replace it with: " + str(replace)                
                
                aux = n
                #auxiliar number
                
                saux = str(aux)
                #auxiliar string
                
#                print "saux: " + saux
                
                for num in range(0, len(saux)-1):
                    #for every digit in auxiliar string (number), if it matches the digit, we replace it
#                    print saux[num]
#                    print saux[num] == str(dig)
                    if saux[num] == str(dig):
                        saux = saux.replace(str(dig), str(replace))
                        break
                
#                print "after replacing all digits with " + str(replace) + ", we get the number: " + saux
#                print "is it prime? " + str(isprime(int(saux)))
                
                if isprime(int(saux)):
                    #for count number, we check how many of a family are prime
                    count += 1
                
                if count > total:
                    #if it is greater than our actual result, we update it
                    total = count
                
#                print "and we get a total of: " + str(count) + "\n"
                
#    print total  
    return total
    
flag = False
num = 56003
while not flag:
    if family(num) == 8:
        print num
        break
    num += 2 