import math

N = 10**25

limit = int(math.log(N, 2))

pows = []

for i in range(0, limit + 1):
    pows.append(2**i)
    pows.append(2**i)

print(pows, len(pows)) # 168 elements