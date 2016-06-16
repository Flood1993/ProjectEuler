from decimal import *

getcontext().prec = 105

squares = [x**2 for x in range(1, 11)]

tot = 0
for i in range(2, 100):
	if i not in squares:
		x = [int(x) for x in (str(Decimal(i).sqrt()).replace('.','')[0:100])]
		tot += sum(x)

print(tot)
