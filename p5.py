found = False
res = 180

while found == False:
	if (res%19 == 0 and res%17 == 0 and res%16 == 0 and res%14 == 0 and res%13 == 0 and res%11 == 0):
        	found = True

	else:
		res = res+180

print str(res)
