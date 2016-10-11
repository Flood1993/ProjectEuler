N = 64000000

def is_sq(n):
    tmp = int(n**0.5)
    return tmp*tmp == n

sums = [1] * N

for i in range(2, N):
    sq = i*i
    for j in range(i, N, i):
        sums[j] += sq

print("Finished")

res = 0

for i in range(1, N):
    if (is_sq(sums[i])):
        res += i

print(res)

# 1922364685. Takes a long time to obtain the solution.