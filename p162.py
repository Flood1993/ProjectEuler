"""
This code will not work because n0..n2 are allowed to go over 10.
"""
memo = {}

def check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS):
    tmp = 0

    hash = (  n0 * 1000000000000000
            + n1 * 100000000000000
            + n2 * 10000000000000
            + n3 * 1000000000000
            + n4 * 100000000000
            + n5 * 10000000000
            + n6 * 1000000000
            + n7 * 100000000
            + n8 * 10000000
            + n9 * 1000000
            + na * 100000
            + nb * 10000
            + nc * 1000
            + nd * 100
            + ne * 10
            + nf)

    if hash in memo:
        return memo[hash]

    total_digits = n0 + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + na + nb + nc + nd + ne + nf
    if (total_digits == DIGITS):
        if n0 > 0 and n1 > 0 and na > 0: # I'm quitting as soon as one is detected. This is wrong... 10AA... Missing cases of only 3 digits.
            memo[hash] = 1
            return 1
        else:
            memo[hash] = 0
            return 0
    
    tmp += check(n0 + 1, n1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1 + 1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2 + 1, n3, n4, n5, n6, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3 + 1, n4, n5, n6, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4 + 1, n5, n6, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5 + 1, n6, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6 + 1, n7, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7 + 1, n8, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8 + 1, n9, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 + 1, na, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, na + 1, nb, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb + 1, nc, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb, nc + 1, nd, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb, nc, nd + 1, ne, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb, nc, nd, ne + 1, nf, DIGITS)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, na, nb, nc, nd, ne, nf + 1, DIGITS)

    memo[hash] = tmp
    return tmp

RES = 0

for d in range(3, 17):
    print(d)
    st = 1
    memo = {}

    RES += check(0, st, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, st, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, st, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, st, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, st, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, st, 0, 0, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, st, 0, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, st, 0, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, st, 0, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, st, 0, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, st, 0, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, st, 0, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, st, 0, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, st, 0, d)
    RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, st, d)

print(RES, hex(RES))