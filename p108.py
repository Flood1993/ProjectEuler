# yn + xn = xy

# given some n, how do we calculate how many solutions are there?

# n = xy / (x+y)

# Let's say n = 4

# there are 3 solutions

# 5,20
# 6,12
# 8,8

# x, y, n >= 0



# n=6. how many solutions?

# how many x, y, exist so that x*y/(x+y) == 6?

# x*y must be a multiple of n


# How many are there for n=7?

# I have to start with k=8, up to 15

# 7 = 8*1 / (8+1)
# 7 = 8*2 / (8+2)
# 7 = 8*4 / (8+4)

# given n, go from i=n+1, 2*n+1, and then, while not n*(x+y) <= x*y 


# n*(x+y) = x*y
# given n and x, the value of y is 
# nx + ny = xy
# nx = xy - ny
# nx = y(x - n)
# y = nx(x-n)

def sols(n):
    result = 0
    for x in range(n + 1, 2*n + 1):
        y = n*x // (x-n)

        if (x+y)*n == x*y:
            result = result + 1

    return result

print(sols(4))

# i = 30
# while True:
#     sol_count = sols(i)
#     # print(i, sol_count)
#     if sol_count >= 1000:
#         print('Found solution:', i)
#         break

#     i = i + 30

#     if i > 10**6:
#         break
x = 2*3
print(x, sols(x))
x = 2*3*5
print(x, sols(x))
x = 2*3*5*7
print(x, sols(x))
x = 2*3*5*7*11
print(x, sols(x))
x = 2*3*5*7*11*13
print(x, sols(x))
x = 2*3*5*7*11*13*17
print(x, sols(x))

x=502320
print(x, sols(x))


# for i in range(277198, 200000, -2):
#     s = sols(i)

#     if s >= 1000:
#         print(i, s)
#         break


# 502320 is not the solution either, even though it has more than 1000



# 120 32, 2**3 * 3 * 5, seems to be 4 * 2 * 2 = 
# 128 8, 2**7 = 8 -> 7 + 1
# 300 38, 2**2 * 3 * 5**2 

# 498960 -> 1094, 2 * 2 * 2 * 2 * 3 * 3 * 3 * 3 * 5 * 7 * 11,   2**4 * 3**4 * 5 * 7 * 11        5 primes
# 510510 -> 1094, 2 * 3 * 5 * 7 * 11 * 13 * 17,                 2 * 3 * 5 * 7 * 11 * 13 * 17    7 primes
# 502320 -> 1094, 2 * 2 * 2 * 2 * 3 * 5 * 7 * 13 * 23           2**4 * 3 * 5 * 7 * 13 * 23      6 primes
# 371280 -> 1094, 2 * 2 * 2 * 2 * 3 * 5 * 7 * 13 * 17
# 327600 -> 1013, 2 * 2 * 2 * 2 * 3 * 3 * 5 * 5 * 7 * 13
# 277200 -> 1013, 2 * 2 * 2 * 2 * 3 * 3 * 5 * 5 * 7 * 11

x = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 5 * 7 * 11
print(x, sols(x))

x = 2 * 2 * 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11
print(x, sols(x))

for two_exp in range(0, 7):
    twos = 2**two_exp
    if twos >= 277200:
        break
    for three_exp in range(0, 7):
        threes = 3**three_exp
        if twos*threes >= 277200:
            break
        for five_exp in range(0, 7):
            fives = 5**five_exp
            if twos*threes*fives >= 277200:
                break
            for seven_exp in range(0, 7):
                sevens = 7**seven_exp
                if twos*threes*fives*sevens >= 277200:
                    break
                for eleven_exp in range(0, 7):
                    elevens = 11**eleven_exp
                    if twos*threes*fives*sevens*elevens >= 277200:
                        break
                    for thirteen_exp in range(0, 7):
                        cand = twos*threes*fives*sevens*elevens*13**thirteen_exp
                        if cand >= 277200:
                            break
                        s = sols(cand)
                        if s >= 1000:
                            print(cand, s)
