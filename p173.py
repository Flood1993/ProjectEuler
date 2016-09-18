LIMIT = 1000000

h2 = [4*x for x in range(3, (LIMIT//4) + 1, 2)]
h1 = [4*x for x in range(2, (LIMIT//4) + 1, 2)]

S = 0

for i in range(len(h2)):
    t = h2[i]
    if t <= LIMIT:
        S += 1
    for j in range(i + 1, len(h2)):
        t += h2[j]
        if t > LIMIT:
            break
        S += 1

for i in range(len(h1)):
    t = h1[i]
    if t <= LIMIT:
        S += 1
    for j in range(i + 1, len(h1)):
        t += h1[j]
        if t > LIMIT:
            break
        S += 1

print(S)
