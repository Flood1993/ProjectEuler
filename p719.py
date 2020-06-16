def number_can_be_achieved_by_splitting(number, to_be_splitted, total_sum=0, splitted=False):
    if number == to_be_splitted + total_sum and splitted:
        return True

    if number > to_be_splitted + total_sum:
        return False
        
    if to_be_splitted // 10 == 0 and splitted:
        # Just one digit
        return total_sum + to_be_splitted == number

    split_factor = 10
    while to_be_splitted // split_factor != 0:
        if number_can_be_achieved_by_splitting(number, to_be_splitted // split_factor, total_sum + (to_be_splitted % split_factor), True):
            return True

        split_factor = split_factor * 10



total = 0

for i in range(1, 10**6 + 1):
    if i % 10000 == 0:
        print(i)

    if number_can_be_achieved_by_splitting(i, i**2):
        total += i**2

print(total)
# n = 9801**0.5
# print(number_can_be_achieved_by_splitting(n, n**2))