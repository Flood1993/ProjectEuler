LIMIT = 3 # Maximum digits of the number. If set to 3, we will calculate the numbers of up to 3 digits.

# Generate all increasing numbers
# Generate all drecreasing numbers
# Count constant numbers: 111, 11, 1, 2222222, 22222, 22...
# Result = increasing + decreasing - constant

increasing = [-1]*1000
decreasing = [-1]*1000

def get_increasing(last_digit, digits=1):
    tmp = 0

    hash = last_digit*100 + (digits - 1)

    if increasing[hash] != -1:
        return increasing[hash]

    if digits == LIMIT:
        increasing[hash] = 1
        return increasing[hash]

    for i in range(last_digit, 10):
        tmp += get_increasing(i, digits + 1)

    return tmp

def get_all_increasing():
    res = 0
    for i in range(10):
        res += get_increasing(i)
    return res

inc = get_all_increasing()
inc_dec = 2*inc
non_bouncy = inc_dec - (1 + 9*LIMIT)
print(inc)
print(non_bouncy)

tmp_res = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
                if b > a and c < b or b < a and c > b:
                    tmp_res += 1
print(tmp_res)