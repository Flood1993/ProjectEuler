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

def holds_conditions(number_set):
    number_set = sorted(number_set)
    return condition_ii(number_set) and condition_i(number_set)

middle_element = 20
optimal_six = [11, 18, 19, 20, 22, 25]

approximated_optimal_seven = [middle_element] + [(el + middle_element) for el in optimal_six]

approximated_sum = sum(approximated_optimal_seven)

best_sum = approximated_sum
best_set = None

print(approximated_sum, approximated_optimal_seven)

print('Takes some minutes to execute...')
for a in range(1, approximated_sum - 5):
    for b in range(a + 1, approximated_sum - a - 4):
        if (a + b) >= approximated_sum:
            continue
        for c in range(b + 1, a + b):
            if (a + b + c) >= approximated_sum:
                continue
            if not condition_ii([a, b, c]):
                continue
            for d in range(c + 1, approximated_sum - a - b - c - 2):
                if (a + b + c + d) >= approximated_sum:
                    continue
                if not condition_ii([a, b, c, d]):
                    continue
                for e in range(d + 1, approximated_sum - a - b - c - d - 1):
                    if (a + b + c + d + e) >= approximated_sum:
                        continue
                    if not condition_ii([a, b, c, d, e]):
                        continue
                    for f in range(e + 1, approximated_sum - a - b - c - d - e):
                        if (a + b + c + d + e + f) >= approximated_sum:
                            continue
                        if not condition_ii([a, b, c, d, e, f]):
                            continue
                        for g in range(f + 1, approximated_sum - a - b - c - d - e - f):
                            if (a + b + c + d + e + f + g) >= approximated_sum:
                                continue
                            candidate = [a, b, c, d, e, f, g]

                            if (holds_conditions(candidate)):
                                sum_for_candidate = sum(candidate)

                                if sum_for_candidate < best_sum:
                                    best_set = candidate
                                    best_sum = sum_for_candidate

print(best_sum, best_set)