from collections import defaultdict

from functions import prime_factorization
from functions import primes_up_to


PRIMES = primes_up_to(50)

# LIMIT, INITIAL_SOLUTION = 1_000, [2, 3, 5, 7, 11, 13, 17]
LIMIT, INITIAL_SOLUTION = 4_000_000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
GLOBAL_RESULT = None

INITIAL_SOLUTION.reverse()


def prod(iter):
    result = 1
    for el in iter:
        result = result * el
    return result


def is_prime(n):
    return n in PRIMES


def number_of_solutions(iter):
    prime_exponent_counter = defaultdict(int)
    
    for number in iter:
        factors = prime_factorizations_up_to_50[number]
        for base, exponent in factors:
            prime_exponent_counter[base] = prime_exponent_counter[base] + exponent

    result = 1
    for base, exponent in prime_exponent_counter.items():
        result = result * (3 + 2*(exponent - 1))

    return result


def try_reducing_number(iter):
    global GLOBAL_RESULT
    solution_count = number_of_solutions(iter)

    if solution_count < 2*LIMIT:
        return None, None, None

    min_solution = prod(iter)
    initial_sol = iter.copy()

    # TODO: Do not do this, but only try replacing the highest/first element
    for idx, el in enumerate(iter):
        some_sol_worked = False
        if idx != 0:
            break
        for candidate in range(2, iter[1]):  # iter[1] or el?
            new_list_candidate = iter.copy()
            new_list_candidate.remove(el)
            new_list_candidate.append(candidate)
            new_list_candidate.sort(reverse=True)

            (new_solution_count, new_min_solution, new_solution) = try_reducing_number(new_list_candidate)

            if (new_solution_count, new_min_solution, new_solution) != (None, None, None):
                if new_solution_count >= 2*LIMIT:
                    some_sol_worked = True
                    if new_min_solution < min_solution:
                        solution_count = new_solution_count
                        min_solution = new_min_solution
                        initial_sol = new_solution
        if not some_sol_worked:
            break

    if min_solution < GLOBAL_RESULT:
        # Luckily first result printed by this is the correct result, even though recursion does not seem to end...
        print(f'New global result found: {GLOBAL_RESULT} - {min_solution})')
        GLOBAL_RESULT = min_solution

    return solution_count, min_solution, initial_sol


if __name__ == '__main__':
    # pre-compute prime factorizations of numbers up to 50
    prime_factorizations_up_to_50 = dict()

    for i in range(2, 51):
        prime_factorizations_up_to_50[i] = prime_factorization(i)

    if LIMIT == 1_000:
        assert number_of_solutions(INITIAL_SOLUTION) == 2187
    if LIMIT == 4_000_000:
        assert number_of_solutions(INITIAL_SOLUTION) == 14348907
    GLOBAL_RESULT = prod(INITIAL_SOLUTION)

    print(try_reducing_number(INITIAL_SOLUTION))
