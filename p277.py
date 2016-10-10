"""
D -> a(n+1) = an / 3
U -> a(n+1) = (4*an + 2) / 3
d -> a(n+1) = (2*an - 1) / 3

Our chain starts with UDDD. That means that our number n:
(4n + 2)/81 must be an integer number

Multiples of 81 such that -2 are multipes of 4 multiples of 162 such that -2 are divisible by 4. 162 is an ok number. Is 162*2 an ok number? 324 - 2 = 322 -> NO!
Our solution is a multiple of 162 that n - 2 % 4 == 0.

Our solution, as of now, must check: (162*n - 2) % 4 == 0

Next steps are Uddd

-------------------------------------------------------

Lets say the chain ends in a number x. x must be integer. Therefore, we want to build the starting number following an inverse process.

n = 9
n1 = 3

To reconstruct the original: n1 = 3 = n/3 -> n =3*n1 =  9

Instead of 3, now we end in x:

(3*x + 1) / 2                 d
(9*x + 3) / 2                 D
(27*x + 5)/2                  U
(81*x + 24)/8 - 2             U
"""

def D(t):
	xval, solo_val, den = t
	return (3*xval, 3*solo_val, den)

def U(t):
	xval, solo_val, den = t
	return (3*xval, 3*solo_val - 2*den, den*4)

def d(t):
	xval, solo_val, den = t
	return (3*xval, 3*solo_val + 1*den, den*2)

xval = 1
solo_val = 0
den = 1

t = (xval, solo_val, den)

chain = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
inverse = chain[::-1]
print(inverse)

for i in range(len(inverse)):
	if inverse[i] == "D":
		t = D(t)

	elif inverse[i] == "U":
		t = U(t)

	elif inverse[i] == "d":
		t = d(t)

print(t)

"""
Given x:
if (205891132094649*x + 21110037246199) % 4194304 == 0:
	(205891132094649*x + 21110037246199) / 4194304 will start with the desired chain
"""

for tmp in range(10**7 + 1, 3*10**7, 2):
#for tmp in range(10**3 + 1, 10**4, 2):
	if (t[0]*tmp + t[1]) % t[2] == 0:
		print((t[0]*tmp + t[1]) // t[2])

# 1125977393124310