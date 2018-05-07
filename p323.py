def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def comb(n, k):
    return fac(n) / (fac(k)*fac(n-k))

assert comb(3,1) == 3

# Memoization
sols = [0]*33
sols[1] = 2 # For one bit, it is easy to see that the expected value is 2

# Idea: Suppose we have 2 bits. Let e_i denote the expected number of i-bit
# sequences we need to flip the i bits to one (in our example, i=2).
# There is a 1/4 chance that we waste a chain (00)
# There is a 2/4 chance that we still need to flip a lonely bit (01, 10)
# There is a 1/4 chance that we are done in one step (11)
# Writing this a bit more formally:
# e_2 = 1/4 (e_2 + 1) + 2/4 (1 + e_1) + 1/4 (1)
# So, we solve for e_2 and then proceed for e_3, e_4, ..., e_32
# Below there is Python code that does that, even though terms have been
# rearranged
for i in range(2,33):
    div = 2**i
    sum_ = 0
    for j in range(1, i):
        sum_ += comb(i, j) * (1 + sols[j])
    e = (1 + 1 + sum_)/(div-1)
    sols[i] = e

print(sols[32])
