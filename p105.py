with open('p105_sets.txt', 'r') as f:
    lines = f.readlines()

sets = []

for line in lines:
    sets.append(sorted([int(n) for n in line.split(",")]))

print(sets[:5])

def condition_i(number_set):
    A = []
    B = []

    return recursively_check_condition_i(A, B, number_set)

def recursively_check_condition_i(A, B, numbers_unused):
    if not numbers_unused:
        if A and B:
            if sum(A) == sum(B):
                return False
        return True

    A_copy = [el for el in A]
    B_copy = [el for el in B]
    numbers_unused_copy = [el for el in numbers_unused]

    next_number = numbers_unused_copy.pop()
    A_copy_with_new_element = [el for el in A_copy]
    A_copy_with_new_element.append(next_number)
    B_copy_with_new_element = [el for el in B_copy]
    B_copy_with_new_element.append(next_number)

    return recursively_check_condition_i(A_copy_with_new_element, B_copy, numbers_unused_copy) \
            and recursively_check_condition_i(A_copy, B_copy_with_new_element, numbers_unused_copy) \
            and recursively_check_condition_i(A_copy, B_copy, numbers_unused_copy)

def condition_ii(number_set):
    total_elems = len(number_set)

    small_subset_size = 1
    while 2*small_subset_size + 1 <= total_elems:
        bigger_subset_size = small_subset_size + 1

        if sum(number_set[:bigger_subset_size]) < sum(number_set[-small_subset_size:]):
            return False

        small_subset_size = small_subset_size + 1
    
    return True

TOTAL = 0

for _set in sets:
    if condition_i(_set) and condition_ii(_set):
        TOTAL = TOTAL + sum(_set)

print(TOTAL)
