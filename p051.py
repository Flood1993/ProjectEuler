from functions import optimised_sieve

LIMIT = 1000000
family_count = 8

primes = optimised_sieve(LIMIT)

def detect_duplicate_numbers(n):
    """
    We want to find only numbers with a repeated digit (excluding the 
    last one) three times at least (because of %3 problems).
    """

    for i in range(len(primes)):
        if primes[i]:
            p = 2*i + 1
            p_str = str(p)
            head = p_str[:-1]
            tail = p_str[-1]

            for elmt in ('01234567890'):
                if head.count(elmt) == 3 or head.count(elmt) == 6:
                    cnt = []
                    for i in range(0, 10):
                        candidate = int(head.replace(elmt, str(i)) + tail)
                        if primes[candidate//2]:
                            cnt.append(candidate)
                    if len(cnt) >= family_count:
                        if len(str(cnt[0])) == len(str(cnt[1])):
                            print(cnt)



detect_duplicate_numbers(LIMIT)
