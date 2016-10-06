"""
01
04
0*
1*
25
3*
4*
*4
81

Restricciones:
- En un cubo tiene que haber un 0 y en el otro un 1
- En un cubo tiene que haber un 0 y en el otro un 4
- En un cubo tiene que haber un 0 y en el otro un *
- En un cubo tiene que haber un 1 y en el otro un *
- En un cubo tiene que haber un 1 y en el otro un 8
- En un cubo tiene que haber un 2 y en el otro un 5
- En un cubo tiene que haber un 3 y en el otro un *
- En un cubo tiene que haber un 4 y en el otro un *

Tengo que distribuir 0, 1, 2, 3, 4, 5, 8, *
"""

possible_dices = []

for a in range(0, 10):
	for b in range(a+1, 10):
		for c in range(b+1, 10):
			for d in range(c+1, 10):
				for e in range(d+1, 10):
					for f in range(e+1, 10):
						possible_dices.append((a,b,c,d,e,f))

print(len(possible_dices))

def check_cross_containment(a, b, el1, el2):
	if (el1 in a and el2 in b) or (el1 in b and el2 in a):
		return True
	return False

cnt = 0

for i in range(len(possible_dices)):
	dice_A = possible_dices[i]

	for j in range(i, len(possible_dices)):
		dice_B = possible_dices[j]

		if (check_cross_containment(dice_A, dice_B, 0, 1)
				and check_cross_containment(dice_A, dice_B, 0, 4)
				and (check_cross_containment(dice_A, dice_B, 0, 6) or check_cross_containment(dice_A, dice_B, 0, 9))
				and (check_cross_containment(dice_A, dice_B, 1, 6) or check_cross_containment(dice_A, dice_B, 1, 9))
				and check_cross_containment(dice_A, dice_B, 1, 8)
				and check_cross_containment(dice_A, dice_B, 2, 5)
				and (check_cross_containment(dice_A, dice_B, 3, 6) or check_cross_containment(dice_A, dice_B, 3, 9))
				and (check_cross_containment(dice_A, dice_B, 4, 6) or check_cross_containment(dice_A, dice_B, 4, 9))
				):
			cnt += 1

print(cnt)