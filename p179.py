def howmanydiv(n):
    """returns the number of divisors of a number"""
    limit = n
    number = 0
    i = 1
    while i < limit:
        if n%i == 0:
            limit = n/i
            if limit != 1:
                number = number+1
            number = number+1
        i = i+1
    return number
    
#res = 0
#actual = 1
#siguiente = 0
#for i in range(1, 100):
#    siguiente = howmanydiv(i+1)
#    if siguiente == actual:
#        res += 1
#    actual = siguiente
print howmanydiv(4)