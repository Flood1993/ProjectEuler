LIMIT = 23

min_res = -1

def gen(n, cnt=1):
	global min_res

	if min_res != -1 and n > min_res:
		return

	# Limit: The number we are looking for is less than 50 digits long
	if cnt >= LIMIT:
		return

	if n%i == 0:
		if min_res == -1 or n < min_res:
			min_res = n

	gen(n*10, cnt+1)
	gen(n*10 + 1, cnt+1)
	gen(n*10 + 2, cnt+1)

"""total = 0
for i in range(1, 10001):
	if i%999 == 0:
		print("Skipping {}".format(i))
		continue

	min_res = -1

	gen(1)
	gen(2)

	if min_res == -1:
		print("Failed to find solution for {}".format(i))
		continue
	total += min_res//i

print(total)

prints 2295538033, but skips the following numbers
999, 1998, 2997, 3996, 4995, 5994, 6993, 7992, 8991, 9990, 9999
"""

"""
total = 0

for i in ((999, 1998, 2997, 3996, 4995, 5994, 6993, 7992, 8991, 9990, 9999)):
	min_res = -1

	gen(1)
	gen(2)

	if min_res == -1:
		print("Failed to find solution for {}".format(i))
		continue

	total += min_res//i

print(total)

prints 646253579358,
but skips 9999
"""

# Missing 9999...
# Based on the following:

# 999 111333555778 111222222222222
# 99 11335578 1122222222
# 9  1358 12222

# Let's assume 9999 is 11112222222222222222

# It is! Final result: 2295538033 + 646253579358 + 1111333355557778 = 1111981904675169