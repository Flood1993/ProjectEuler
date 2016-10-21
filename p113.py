LIMIT = 100

# x represents the increasing values
x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(LIMIT)]

for i in range(len(x[0])):
	x[0][i] = 1
x[0][0] = 0

for i in range(1, len(x)):
	for j in range(len(x[i])):
		for k in range(j + 1):
			x[i][j] += x[i-1][k]

# y represents the decreasing values
y = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(LIMIT)]

for i in range(len(y[0])):
	y[0][i] = 1
y[0][0] = 0

for i in range(1, len(y)):
	for j in range(len(y[i])):
		for k in range(j, len(y[i])):
			y[i][j] += y[i-1][k]

if LIMIT <= 6:
	print(x)
	print(y)

"""
Increasing numbers of 2 digit having 0 as the last digit:
"""

total = 0
for i in range(len(x)):
	total += sum(x[i])
	total += sum(y[i])
print(total - LIMIT*9) # TODO: Substract values which are at the same time increasing and decreasing, that is, numbers with all equal digits.

"""
If len was 3, we should take out:
1, 11, 111
2, 22, 222
3, 33, 333
4, 44, 444
5, 55, 555
6, 66, 666
7, 77, 777
8, 88, 888
9, 99, 999

Number of increasing numbers of 2 digits ending with
0 - 0
1 - 1 (11)
2 - 2 (12, 22)
3 - 3 (13, 23, 33)
4 - 4 (14, 24, 34, 44)
...

Number of increasing numbers of 3 digits ending with
0 - 0
1 - 1 (111)
2 - 3 (112, 122, 222)
3 - 6 (113, 123, 133, 223, 233, 333)
"""