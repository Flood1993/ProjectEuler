from functions import gcd

LIMIT = 100

memo = {}

def f(y, x=1):
    keys = set()
    found = False
    while y > 1:
        if (x, y) in memo:
            found = True
            val = memo[(x, y)]
            break
        keys.add((x, y))

        _gcd = gcd(x, y)

        if _gcd != 1:
            x //= _gcd
            y //= _gcd
        else:
            x += 1
            y -= 1

    keys.add((x, y))

    for k in keys:
        if k not in memo:
            if found:
                memo[k] = val
            else:
                memo[k] = x

    if found:
        return val

    return x

assert f(20) == 6, "ERROR: Basic case not working"

def F(n):
    res = 0

    for i in range(1, n + 1):
        res += f(i**3)

    return res

assert F(100) == 118937, "ERROR: Example not working"

print(F(1000))