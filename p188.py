values = []

a = 1777
LIMIT = 1855
m = 10**8

values.append(0)
values.append(a) # a^^1

for i in range(2, LIMIT + 1):
	values.append(pow(a, values[-1], m)) # a^^n+1 = a^(a^^n)

print(values[-1])