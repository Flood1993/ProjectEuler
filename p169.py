# 2**84 > 10**25. We need 86 for counting the power of 0 and having 1 spare due to the way we calculate it, i.e., we use powers[x+1].
N = 86

powers = [2**i for i in range(0, N)]
memoization = {}

def f(x, y):
    """
    Params
    ======
        x: Powers available. We assume we have available always 2 of the powers. So if x = 4, we have 2 of each: 2**0, 2**1, 2**2, and 2**3.
        y: Target number which we want to calculate with the available powers.
    """
    key = (x, y)
    if (key in memoization):
        return memoization[key]

    if y < 0:
        return 0
    if y == 0:
        return 1
    if x == 0:
        return 0

    if (y > 2*(powers[x+1] - 1)):
        return 0

    res = 0
    for i in range(0, x):
        res = res + f(i, y - powers[i]) + f(i, y - 2*powers[i])

    memoization[key] = res

    return res

def F(x, y):
    result = f(x, y)
    print(f"f({x}, {y}):", result)
    return result

assert F(4, 10) == 5

F(84, 10**25)