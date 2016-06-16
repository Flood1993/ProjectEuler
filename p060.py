import random, time

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
	
    for repeat in xrange(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

A = []
     
B = [3, 7, 109, 673]
a = 675

while True:
    if miller_rabin(a):
        if miller_rabin(int(str(a) + '3')) and miller_rabin(int('3' + str(a))) and miller_rabin(int(str(a) + '7')) and miller_rabin(int('7' + str(a))) and miller_rabin(int(str(a) + '109')) and miller_rabin(int('109' + str(a))) and miller_rabin(int(str(a) + '673')) and miller_rabin(int('673' + str(a))):
            B.append(a)
            break
    a += 2
    
print B