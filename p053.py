import math

def combinatoric(n, r):
    # r <= n, returns in how many ways it is possible to select n items from a r set
    if (r <= n):
        return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

res = 0

for i in range(1, 101):
    r = 1
    while r <= i:
        if combinatoric(i, r) > 1000000:
            res = res+1
        r = r+1
                
            
print str(res)