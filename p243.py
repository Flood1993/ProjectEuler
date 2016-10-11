"""
It definetely seems that brute force does not work for this one. 

I think the solution must be a product of small primes: For example, 12 is 2*2*3

2 -> resilience 1/2
2*3 = 6 -> resilience = 6 * 1/2 * 2/3 = 2 -> 2/5
2*2*3 = 12 -> resilience = 12 * 1/2 * 2/3 = 4 -> 4/11
2*3*5 = 30 -> resilience = 30 * 1/2 * 2/3 * 4/5 = 8 -> 8/30 = 4/15
2*3*5*7*11*13*17*19 = 9699690 -> resilience = 9699690 * 1/2 * 2/3 * 4/5 * 6/7 * 10/11 * 12/13 * 16/17 * 18/19 =
                                              1658880 -> 1658880 / 9699689 = 0.1710
2*3*5*7*11*13*17*19*23 = 223092870 -> resilience = 
2*4*6*10*12*16*18*22     36495360 -> 36495360 / 223092869 = 0.163588

2*3*5*7*11*13*17*19*23*29 = 6469693230
2*4*6*10*12*16*18*22*28     1021870080 -> 1021870080 / 6469693229 = 0.157947 lower than the desired value

Totient function knowing the primes:
[2, 2, 2, 2, 3, 5, 7]
n = 2*2*2*2*3*5*7
tot = n * 1/2 * 2/3 * 4/5 * 6/7

ratio = tot / (n-1)
"""

min_den = 99999999999999999

for n2 in range(34):
    for n3 in range(22):
        ac1 = 2**n2 * 3**n3
        if ac1 > 6469693230:
            break
        for n5 in range(16):
            ac2 = ac1 * 5**n5
            if ac2 > 6469693230:
                break
            for n7 in range(13):
                ac3 = ac2 * 7**n7
                if ac3 > 6469693230:
                    break
                for n11 in range(11):
                    ac4 = ac3 * 11**n11
                    if ac4 > 6469693230:
                        break
                    for n13 in range(10):
                        ac5 = ac4 * 13**n13
                        if ac5 > 6469693230:
                            break
                        for n17 in range(9):
                            ac6 = ac5 * 17**n17
                            if ac6 > 6469693230:
                                break
                            for n19 in range(9):
                                ac7 = ac6 * 19**n19
                                if ac7 > 6469693230:
                                    break
                                for n23 in range(9):
                                    ac8 = ac7 * 23**n23
                                    if ac8 > 6469693230:
                                        break
                                    for n29 in range(8):
                                        prod = ac8* 29**n29
                                        tot = prod
                                        if n2 != 0:
                                            tot *= 1/2
                                        if n3 != 0:
                                            tot *= 2/3
                                        if n5 != 0:
                                            tot *= 4/5
                                        if n7 != 0:
                                            tot *= 6/7
                                        if n11 != 0:
                                            tot *= 10/11
                                        if n13 != 0:
                                            tot *= 12/13
                                        if n17 != 0:
                                            tot *= 16/17
                                        if n19 != 0:
                                            tot *= 18/19
                                        if n23 != 0:
                                            tot *= 22/23
                                        if n29 != 0:
                                            tot *= 28/29

                                        if prod != 1 and tot/(prod - 1) < 15499/94744 and prod < min_den:
                                            min_den = prod

print(min_den)