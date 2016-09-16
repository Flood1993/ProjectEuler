numbers = []

n = 1777

counter = 0

while True:
    if n in numbers:
        break
    numbers.append(n)
    counter += 1
    n = (n * n) % 100000000

print('Repeating after', counter, 'iterations. The repeating sequence is', n) # 12503 iterations

for i in range(len(numbers)):
    if numbers[i] == n:
        print(i)
        break

# It gets to a point in which it starts repeating over again
print(n, numbers[3])
