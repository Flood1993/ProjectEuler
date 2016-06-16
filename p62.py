def digits(n):
    '''returns a list containing the number of appareances of each digit'''
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    string = str(n)
    for i in range(0, len(string)):
        A[int(string[i])] = A[int(string[i])] + 1
    return A

lowlimit = 4642
upperlimit = 10000

#A = []
#for i in range(lowlimit, upperlimit):
#    A.append(digits(i**3))
#    
#pos = lowlimit
#for a in A:
#    cont = 0
#    for b in A:
#        if a == b:
#            cont += 1
#            
#    if cont == 5:
#        print pos
#    pos += 1

#print 1000000000000**0.33333333333
print 5027**3