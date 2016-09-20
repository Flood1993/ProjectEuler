from functions import pythTriplet, gcd

LIMIT = 100000000

solutions = 0

for m in range(2, int(LIMIT**0.5) + 1):
    for n in range(1, m):
        if (m + n) % 2 == 0:
            continue
        if gcd(m, n) != 1:
            continue
        t = pythTriplet(m, n)

        # Reorder triplet
        if t[0] > t[1]:
            t[0] , t[1] = t[1], t[0]

        if (t[2] % (t[1]-t[0])) == 0:
            perimeter = sum(t)
            solutions += LIMIT//perimeter

print(solutions)
