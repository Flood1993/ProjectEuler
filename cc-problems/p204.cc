#include <stdio.h>
#include <math.h>

/*
PYTHON CODE I USED FOR GETTING THE VALUES:

ps = [True] * 101
ps[0] = False
ps[1] = False

primes = []

for i in range(2, len(ps)):
    if ps[i]:
        primes.append(i)
        for j in range(2*i, len(ps), i):
            ps[j] = False

print(primes)
print(len(primes))

def find_exponent(base, limit):
    res = 0
    t = base
    while t <= limit:
        t = t*base
        res += 1
    return res

base_exp = []

for p in primes:
    base_exp.append((p, (find_exponent(p, 10**9))))
"""
[(2, 29), (3, 18), (5, 12), (7, 10), (11, 8), (13, 8), (17, 7), 
(19, 7), (23, 6), (29, 6), (31, 6), (37, 5), (41, 5), (43, 5), 
(47, 5), (53, 5), (59, 5), (61, 5), (67, 4), (71, 4), (73, 4), 
(79, 4), (83, 4), (89, 4), (97, 4)]
"""
*/

int main() {
    int res = 0;

    int LIMIT = pow(10, 9);

    for (int n2 = 0; n2 < 30; n2++) {
        long a1 = pow(2, n2);
        for (int n3 = 0; n3 < 19; n3++) {
            long a2 = a1 * pow(3, n3);
            if (a2 > LIMIT)
                break;
            for (int n5 = 0; n5 < 13; n5++) {
                long a3 = a2 * pow(5, n5);
                if (a3 > LIMIT)
                    break;
                for (int n7 = 0; n7 < 11; n7++) {
                    long a4 = a3 * pow(7, n7);
                    if (a4 > LIMIT)
                        break;
                    for (int n11 = 0; n11 < 9; n11++) {
                        long a5 = a4 * pow(11, n11);
                        if (a5 > LIMIT)
                            break;
                        for (int n13 = 0; n13 < 9; n13++) {
                            long a6 = a5 * pow(13, n13);
                            if (a6 > LIMIT)
                                break;
                            for (int n17 = 0; n17 < 8; n17++) {
                                long a7 = a6 * pow(17, n17);
                                if (a7 > LIMIT)
                                    break;
                                for (int n19 = 0; n19 < 8; n19++) {
                                    long a8 = a7 * pow(19, n19);
                                    if (a8 > LIMIT)
                                        break;
                                    for (int n23 = 0; n23 < 7; n23++) {
                                        long a9 = a8 * pow(23, n23);
                                        if (a9 > LIMIT)
                                            break;
                                        for (int n29 = 0; n29 < 7; n29++) {
                                            long a10 = a9 * pow(29, n29);
                                            if (a10 > LIMIT)
                                                break;
                                            for (int n31 = 0; n31 < 7; n31++) {
                                                long a11 = a10 * pow(31, n31);
                                                if (a11 > LIMIT)
                                                    break;
                                                for (int n37 = 0; n37 < 6; n37++) {
                                                    long a12 = a11 * pow(37, n37);
                                                    if (a12 > LIMIT) 
                                                        break;
                                                    for (int n41 = 0; n41 < 6; n41++) {
                                                        long a13 = a12 * pow(41, n41);
                                                        if (a13 > LIMIT)
                                                            break;
                                                        for (int n43 = 0; n43 < 6; n43++) {
                                                            long a14 = a13 * pow(43, n43);
                                                            if (a14 > LIMIT)
                                                                break;
                                                            for (int n47 = 0; n47 < 6; n47++) {
                                                                long a15 = a14 * pow(47, n47);
                                                                if (a15 > LIMIT)
                                                                    break;
                                                                for (int n53 = 0; n53 < 6; n53++) {
                                                                    long a16 = a15 * pow(53, n53);
                                                                    if (a16 > LIMIT)
                                                                        break;
                                                                    for (int n59 = 0; n59 < 6; n59++) {
                                                                        long a17 = a16 * pow(59, n59);
                                                                        if (a17 > LIMIT)
                                                                            break;
                                                                        for (int n61 = 0; n61 < 6; n61++) {
                                                                            long a18 = a17 * pow(61, n61);
                                                                            if (a18 > LIMIT)
                                                                                break;
                                                                            for (int n67 = 0; n67 < 5; n67++) {
                                                                                long a19 = a18 * pow(67, n67);
                                                                                if (a19 > LIMIT)
                                                                                    break;
                                                                                for (int n71 = 0; n71 < 5; n71++) {
                                                                                    long a20 = a19 * pow(71, n71);
                                                                                    if (a20 > LIMIT)
                                                                                        break;
                                                                                    for (int n73 = 0; n73 < 5; n73++) {
                                                                                        long a21 = a20 * pow(73, n73);
                                                                                        if (a21 > LIMIT)
                                                                                            break;
                                                                                        for (int n79 = 0; n79 < 5; n79++) {
                                                                                            long a22 = a21 * pow(79, n79);
                                                                                            if (a22 > LIMIT)
                                                                                                break;
                                                                                            for (int n83 = 0; n83 < 5; n83++) {
                                                                                                long a23 = a22 * pow(83, n83);
                                                                                                if (a23 > LIMIT)
                                                                                                    break;
                                                                                                for (int n89 = 0; n89 < 5; n89++) {
                                                                                                    long a24 = a23 * pow(89, n89);
                                                                                                    if (a24 > LIMIT)
                                                                                                        break;
                                                                                                    for (int n97 = 0; n97 < 5; n97++) {
                                                                                                        long a25 = a24 * pow(97, n97);
                                                                                                        if (a25 > LIMIT)
                                                                                                            break;
                                                                                                        res += 1;
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    printf("%i\n", res);

    return 0;
}