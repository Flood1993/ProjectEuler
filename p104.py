fib = []
fib.append(1)
fib.append(1)

def digits(n):
    '''returns a list containing the number of appareances of each digit'''
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    string = str(n)
    for i in range(0, len(string)):
        A[int(string[i])] = A[int(string[i])] + 1
    return A
    
def ndig(n):
    return len(str(n))    

def pandigital(n):
    x = digits(n)
    for i in range(1, 10):
        if x[i] != 1:
            return False
    return True

#found = False
#i = 2
#while not found:
#    fib.append(fib[i-2] + fib[i-1])
#    if pandigital(int(str(fib[i])[0:9:1])):
#    #if pandigital(int(str(fib[i])[0:10:1])) and pandigital(int(str(fib[i])[0:-10:-1])):
#        # and pandigital(str(fib[i])[0:-10:-1])
#        print 'first' + str(i+1)
##        found = True
##        break
#    if pandigital(fib[i] % 1000000000):
#        print 'last' + str(i+1)
#    i = i+1


#
#x = '123456789abcdefghi'
#print x[:-10:-1] #last 9 digits
#print x[0:9:1] #first nine digits

def fibwhat(n):
    return (1.0/(5**0.5)) * ((1.0 + 5.0**0.5) / 2.0)**n - (1.0/(5.0**0.5)) * ((1.0 - 5.0**0.5) / 2.0)**n
    
print fibwhat(10)