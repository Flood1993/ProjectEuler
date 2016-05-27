#p051

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

print(is_prime(4547337172376300111955330758342147474062293202868155909489))
for i in range(10**5, 10**7, 2):
    if i%5 == 0:
        continue
    num1 = int(str(i) + "673")
    num2 = int("673" + str(i))
    num3 = int(str(i) + "109")
    num4 = int("109" + str(i))
    num5 = int(str(i) + "7")
    num6 = int("7" + str(i))
    num7 = int(str(i) + "3")
    num8 = int("3" + str(i))
    if (is_prime(num1) and is_prime(num2) and is_prime(num3) and is_prime(num4) and is_prime(num5) and is_prime(num6) and is_prime(num7) and is_prime(num8)):
        print(i)
