CHECKS_NEEDED = 0

# For this problem we only care about the subsets B and C with equal size
# Furthermore, if the size is 1, we don't need to compare because they are strictly increasing, i.e., different
def how_many_need_check(subset_size):
    numbers = [i for i in range(1, 13)]
    B = []
    C = []

    fill_B_and_C(B, C, subset_size, numbers)

def fill_B_and_C(B, C, subset_size, numbers):
    global CHECKS_NEEDED
    B_full = len(B) == subset_size
    C_full = len(C) == subset_size

    if B_full and C_full:
        if (needs_check(B, C)):
            CHECKS_NEEDED = CHECKS_NEEDED + 1
        return

    if not numbers:
        return

    B_copy = [el for el in B]
    C_copy = [el for el in C]
    numbers_copy = [el for el in numbers]

    next_number = numbers_copy.pop()

    B_copy_with_new_element = [el for el in B_copy]
    B_copy_with_new_element.append(next_number)
    C_copy_with_new_element = [el for el in C_copy]
    C_copy_with_new_element.append(next_number)

    if not B_full:
        fill_B_and_C(B_copy_with_new_element, C_copy, subset_size, numbers_copy)
    if not C_full:
        fill_B_and_C(B_copy, C_copy_with_new_element, subset_size, numbers_copy)

    fill_B_and_C(B_copy, C_copy, subset_size, numbers_copy)

def needs_check(B, C):
    has_decrement = False
    has_increment = False

    for i in range(len(B)):
        if B[i] < C[i]:
            has_increment = True
        if B[i] > C[i]:
            has_decrement = True

    return has_increment and has_decrement

# print('Solution for 2', how_many_need_check(2))
# print('Solution for 3', how_many_need_check(3))

for i in range(2, 7):
    how_many_need_check(i)

# Divide by two since for each two subsets we will be comparing both B = S1, C = S2 and B = S2, C = S1
print(CHECKS_NEEDED//2)