def phi(n): 
    # returns the totient function of n
    result = n
    i = 2
    while i*i <= n:
        if n%i == 0:
            result -= result/i
        while n%i == 0:
            n /= i
        i += 1
    if n > 1:
        result -= result / n
    return result           
  
total = 0

for i in range(2, 1000001):
    total += phi(i)
    
print total

#303963552391