#p164.py

L = [False]*1000

def sum_digits(n):
    res = 0
    while (n != 0):
        res += n%10
        n = n//10
    return res

print(sum_digits(123))
print(sum_digits(126))
print(sum_digits(999))
print(sum_digits(123456789))

total = 0
for i in range(100, 1000):
    if sum_digits(i) <= 9:
        total += 1
print(total)

total = 0
for i in range(1000):
    if sum_digits(i) <= 9:
        total += 1
print(total)