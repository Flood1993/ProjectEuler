"""
b = blue discs
r = red discs
t = total discs

We know: t = b + r

We are looking for values such as:
b   b-1   1
- * --- = -
t   t-1   2

b * (b-1) * 2 == t * (t-1)

We are looking for the least value of b and t that satisfy that equation, with t >= 10**12

2 * (b**2 - b) == t**2 - t

2b**2 - t**2 - 2b + t == 0

x0 = 15
y0 = 21
"""

x = [15]
y = [21]

for i in range(20):
    x_add = 3*x[-1] + 2*y[-1] - 2
    y_add = 4*x[-1] + 3*y[-1] - 3
    x.append(x_add)
    y.append(y_add)

for i in range(len(y)):
    if y[i] > 10**12:
        print(x[i])
        break
