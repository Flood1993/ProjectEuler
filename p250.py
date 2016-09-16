L = [0]*250

for i in range(1, 250251):
    L[pow(i, i, 250)] += 1

for i in range(len(L)):
    if L[i] != 0:
        print(i, L[i])
