"""
The triangle 5,5,6 is a triangle in which there is a pythagorean triplet such that 3,4,5 in which there is a number n in [3,4] (not the diagonal) such that 5-2n == 1 or 5-2n == -1

Therefore, we want to generate Pythagorean triplets in which mm + nn - min(mm - nn, 2mn) == 1 or -1

We are only interested in primitive ones because the difference is increased by a factor of d.

Also, the perimeter is 2mm + 2mn
"""
from functions import pythTriplet, gcd

total_perimeter = 0

for m in range(2, 20000):
    for n in range(1, m):
        if (m + n)%2 == 0:
            continue
        if gcd(m, n) != 1:
            continue
        t = pythTriplet(m, n)
        if abs(t[2] - 2*t[1]) == 1 or abs(t[2] - 2*t[0]) == 1:
            total_perimeter += 2*(t[2] + min(t[0], t[1]))
            print(t, 'PER', total_perimeter)




