def pythTriplet(m, n, d = 1):
    if m < n:
        m, n = n, m
    return [(m*m - n*n)*d, (2*m*n)*d, (m*m + n*n)*d]

def perimeter(m, n):
    return 2*m*(m+n)

sols = 0

def gcd(a, b):
    while b != 0:
       t = b
       b = a%b
       a = t
    return a

sols = 0
L = [0]*1500003
for m in range(2, 1500001, 2):
    for n in range(1, 1500001, 2):
        per = perimeter(m, n)
        step = per
        while (per <= 1500000):
            L[per] += 1
            sols += 1
            per += step
        break


print(L.count(1))