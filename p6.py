sumSqu = 0
squSum = 0

for i in range (1,101):
	sumSqu = sumSqu + (i**2)

for i in range (1,101):
	squSum = squSum + i

squSum = squSum**2

res = squSum - sumSqu

print str(res)
