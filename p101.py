import numpy as np

A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X = np.linalg.inv(A).dot(B)

print(X)

def u_n(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

seq = [u_n(i) for i in range(1, 12)]

print(seq)

# OP(1, n) = 1
# OP(2, n) = 683 + 682
# OP(10, n)...

# Let's focus on case for k = 3 (2 degree polynomial)
# We have to construct the points, solve it, find the 2 degree equation, and then pass to it n = 3
# So we will have [[1, 1, 1], [4, 2, 1], [9, 3, 1]] and then solve it for seq[:3]. k = 3. 3 elements. 
def create_A(k):
    A_list = []
    for i in range(1, k+1):
        A_list.append(create_equation(i, k))

    return A_list


def create_equation(i, k):
    res = []
    for val in range(k-1, -1, -1):
        res.append(i**val)

    return res

print(create_A(3))

def create_B(k):
    return seq[:k]

print(create_B(3))

def solve(k):
    A = np.array(create_A(k))
    B = np.array(create_B(k))
    X = np.linalg.inv(A).dot(B)

    return X

def find_bop(k):
    solution = solve(k)

    bop = 0
    for i in range(k-1, -1, -1):
        inverse_index = k-1 - i
        bop = bop + (k+1)**i * solution[inverse_index]

    return bop

a = solve(3)
print(a, type(a), a[0])

print(find_bop(3))

bop_sum = 0
for i in range(3, 11):
    bop_sum = bop_sum + find_bop(i)

print(bop_sum + 683 + 682 + 1)

# result rounds to 7 even though the actual solution is 6, due to floating precision errors