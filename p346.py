"""
Any number n is repunit when expressed in n-1.

For example, 7 in base 6 is 11, 5124 in base 5123 is also 11.

Question is: how many numbers are repunit in a different base than n-1 below 10**12?

We start with base 2. Which numbers are repunit apart from 3? 
    111 which is 7 (2**2 + 2 + 1)
    1111 which is 15 (7*2 + 1)
    11111 which is 31 (15*2 + 1)
    111111 which is 63 (31*2 + 1)

Then, for base 3:
    111 which is 13 (3**2 + 3 + 1)
    1111 which is 40 (13*3 + 1)
    11111 which is 121 (40*3 + 1)
"""

LIMIT = 10**12

total = set() # Start on 1 because 1 is repunit in all bases
total.add(1)

for i in range(2, int(LIMIT**0.5) + 1):
    value = i**2 + i + 1
    while value < LIMIT:
        total.add(value)
        value = value*i + 1

print(sum(total))
