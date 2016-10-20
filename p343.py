from functions import gcd

LIMIT = 100

def f(y, x=1):
    while y > 1:
        _gcd = gcd(x, y)
        if _gcd != 1:
            x //= _gcd
            y //= _gcd
        else:
            x += 1
            y -= 1

    return x

assert f(20) == 6

res = 0

for i in range(1, LIMIT + 1):
    res += f(i**3)

print(res)