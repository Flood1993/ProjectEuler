memo = {}

def check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9):
    tmp = 0

    hash = (  n0 * 1000000000
            + n1 * 100000000
            + n2 * 10000000
            + n3 * 1000000
            + n4 * 100000
            + n5 * 10000
            + n6 * 1000
            + n7 * 100
            + n8 * 10
            + n9)

    if (n0 > 3 or n1 > 3 or n2 > 3 or n3 > 3 or n4 > 3 or n5 > 3 or n6 > 3
            or n7 > 3 or n8 > 3 or n9 > 3):
        return 0

    if (hash in memo):
        return memo[hash]

    if (n0 + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 == 18):
        memo[hash] = 1
        return 1

    tmp += check(n0 + 1, n1, n2, n3, n4, n5, n6, n7, n8, n9)
    tmp += check(n0, n1 + 1, n2, n3, n4, n5, n6, n7, n8, n9)
    tmp += check(n0, n1, n2 + 1, n3, n4, n5, n6, n7, n8, n9)
    tmp += check(n0, n1, n2, n3 + 1, n4, n5, n6, n7, n8, n9)
    tmp += check(n0, n1, n2, n3, n4 + 1, n5, n6, n7, n8, n9)
    tmp += check(n0, n1, n2, n3, n4, n5 + 1, n6, n7, n8, n9)
    tmp += check(n0, n1, n2, n3, n4, n5, n6 + 1, n7, n8, n9)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7 + 1, n8, n9)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8 + 1, n9)
    tmp += check(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 + 1)

    memo[hash] = tmp
    return tmp

RES = 0

RES += check(0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
RES += check(0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
RES += check(0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
RES += check(0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
RES += check(0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
RES += check(0, 0, 0, 0, 0, 0, 1, 0, 0, 0)
RES += check(0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
RES += check(0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
RES += check(0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
 
print(RES)