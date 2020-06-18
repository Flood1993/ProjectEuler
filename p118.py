# step 1: I need to generate all primes with different digits under 999999999
# so basically, 
#find all primes below sqrt(999999999) = 31622

import pickle
from functions import primes_up_to

# print(999999999**0.5)

# then, generate all possible numbers with different digits with 5, 6, 7, 8, 9 digits.

# have a set with all primes with different numbers



def all_characters_different(string):
    length = len(string)

    if length > 0:
        return length == len(set(string))

    return False








# # SAVE PICKLE PART
# primes_to_check = primes_up_to(int(999999999**0.5))

# print(len(primes_to_check))

# def digit_count(n):
#     return len(str(n))

# def all_digits_different(n):
#     return all_characters_different(str(n))

# print(all_digits_different(1234))

# primes_with_no_repeated_digits = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]

# primes_below_1_000_000 = primes_up_to(1_000_000)

# for p in primes_below_1_000_000:
#     if all_digits_different(p):
#         primes_with_no_repeated_digits[digit_count(p)].add(p)

# def is_prime(n):
#     global primes_to_check

#     sqrt_n = int(n**0.5) + 1

#     for prime in primes_to_check:
#         if prime > sqrt_n:
#             break
        
#         if n%prime == 0:
#             return False

#     return True

# for a in range(1, 10):
#     for b in range(1, 10):
#         if b == a:
#             continue
#         for c in range(1, 10):
#             if c == b or c == a:
#                 continue
#             for d in range(1, 10):
#                 if d == c or d == b or d == a:
#                     continue
#                 for e in range(1, 10):
#                     if e == d or e == c or e == b or e == a:
#                         continue
#                     for f in range(1, 10):
#                         if f == e or f == d or f == c or f == b or f == a:
#                             continue
#                         for g in range(1, 10):
#                             if g == f or g == e or g == d or g == c or g == b or g == a:
#                                 continue
#                             number_7 = int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g))
#                             if (is_prime(number_7)):
#                                 primes_with_no_repeated_digits[7].add(number_7)
#                             for h in range(1, 10):
#                                 if h == g or h == f or h == e or h == d or h == c or h == b or h == a:
#                                     continue
#                                 number_8 = int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h))
#                                 if (is_prime(number_8)):
#                                     primes_with_no_repeated_digits[8].add(number_8)
#                                 for i in range(1, 10):
#                                     if i == h or i == g or i == f or i == e or i == d or i == c or i == b or i == a:
#                                         continue
#                                     number_9 = int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i))
#                                     if (is_prime(number_9)):
#                                         primes_with_no_repeated_digits[9].add(number_9)

# pickle.dump(primes_with_no_repeated_digits, open("primes.pickle", "wb"))

# print(len(_set) for _set in primes_with_no_repeated_digits)


def has_zero(n):
    return '0' in str(n)

#LOADING
primes_with_no_repeated_digits = pickle.load(open( "primes.pickle", "rb" ))

print(type(primes_with_no_repeated_digits))
for i in range(0, 10):
    primes_with_no_repeated_digits[i] = sorted(list(primes_with_no_repeated_digits[i]))
    for j in range(len(primes_with_no_repeated_digits[i]) - 1, -1, -1):
        if has_zero(primes_with_no_repeated_digits[i][j]):
            primes_with_no_repeated_digits[i].pop(j)

    print(i, len(primes_with_no_repeated_digits[i]))

memo = {}

def check_pandigital_prime_sets(digits_so_far_as_string, last_prime):
    global primes_with_no_repeated_digits
    global memo
    digits_sorted = ''.join(sorted(digits_so_far_as_string))

    # If result previously memoized
    # if digits_sorted in memo:
    #     return memo[digits_sorted]

    if not all_characters_different(digits_so_far_as_string):
        return 0

    length = len(digits_so_far_as_string)
    if length > 9:
        raise Exception('Length greater than 9: {} {}', digits_so_far_as_string, last_prime)
    if length == 9:
        return 1

    length_last_prime = len(str(last_prime))

    result = 0
    # Only check "downwards"
    for length_to_check in range(1, min(9 - length + 1, length_last_prime + 1)):
        for p in primes_with_no_repeated_digits[length_to_check]:
            if p >= last_prime:
                break
            result = result + check_pandigital_prime_sets(digits_so_far_as_string + str(p), p)

    # Memoize result
    # memo[digits_sorted] = result

    return result

TOTAL = 0

for i in range(9, 0, -1):
    print(i)
    for p in primes_with_no_repeated_digits[i]:
        TOTAL = TOTAL + check_pandigital_prime_sets(str(p), p)

print('Solution:', TOTAL)


# Had so many problems with this problem
# At first, I was counting duplicates, by looking always to fill up the string with any primes. Then, I switched to start from prime N and then try to fill it only with smaller primes
# Then, I overlooked that the primes I was using less than 1 million could contain zeroes. So I had to remove them.
# Then, I was mistakingly using memoization, when I can't, because for each prime we only use the smallers from it, and memoizing it does not respect this condition.