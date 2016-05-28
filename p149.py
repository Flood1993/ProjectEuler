#p149

import time

start = time.time()

def generate_table():
    res = [0]*4000000

    for i in range(1, 56):
        res[i - 1] = ((100003 - 200003*i + 300007*i*i*i)%1000000) - 500000

    for i in range(56, 4000000):
        res[i - 1] = ((res[i - 25] + res[i - 56] + 1000000))%1000000 - 500000

    return res

def check_horizontal(L, n):
    """
    Returns the maximum possible sum for row n
    """
    row = L[(2000*n):(2000*(n+1))]
    sums = [0]*2000
    sums[0] = row[0]
    for i in range(1, len(row)):
        sums[i] = max(row[i], row[i] + sums[i-1])
    return max(sums)

def check_vertical(L, n):
    """
    Returns the maximum possible sum for column n
    """
    col = L[n:len(L):2000]
    sums = [0]*2000
    sums[0] = col[0]
    for i in range(1, len(col)):
        sums[i] = max(col[i], col[i] + sums[i-1])
    return max(sums)

def check_diagonal1(L, n):
    return None

def check_diagonal2(L, n):
    return None

my_table = generate_table()
max_found = 0
for i in range(0, 2000):
    max_found = max(max_found, check_vertical(my_table, i))

print("Solution", max_found)

print(time.time() - start)