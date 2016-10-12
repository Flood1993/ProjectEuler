DIGITS_LIMIT = 40

def step_pand(last_dig, zero, nine, cur_digits):
    tmp = 0

    if cur_digits > DIGITS_LIMIT:
        return 0
    
    hash = 0
    if zero:
        hash += 10000
    if nine:
        hash += 1000
    hash += last_dig * 100
    hash += cur_digits

    if memo[hash] != -1:
        return memo[hash]

    if zero and nine:
        tmp = 1
        
        if last_dig == 0:
            tmp += step_pand(1, True, nine, cur_digits + 1)
        elif last_dig == 9:
            tmp += step_pand(8, zero, True, cur_digits + 1)
        else:
            next_zero = (last_dig - 1 == 0)
            next_nine = (last_dig + 1 == 9)
            tmp += step_pand(last_dig - 1, zero or next_zero, nine , cur_digits + 1)
            tmp += step_pand(last_dig + 1, zero, nine or next_nine, cur_digits + 1)
        
        memo[hash] = tmp

        return tmp

    if last_dig == 0:
        tmp += step_pand(1, True, nine, cur_digits + 1)
    elif last_dig == 9:
        tmp += step_pand(8, zero, True, cur_digits + 1)
    else:
        next_zero = (last_dig - 1 == 0)
        next_nine = (last_dig + 1 == 9)
        tmp += step_pand(last_dig - 1, zero or next_zero, nine , cur_digits + 1)
        tmp += step_pand(last_dig + 1, zero, nine or next_nine, cur_digits + 1)
        
    memo[hash] = tmp
    return tmp

res = 0
memo = [-1]*12000

for i in range(1, 9):
    res += step_pand(i, False, False, 1)
res += step_pand(9, False, True, 1)

print(res)