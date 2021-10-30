memo = dict()

def get_solution(ones_left, sum_so_far, prod_so_far, original_k):
    """
    Returns
        int: Minimal solution, if at least 1 solution is found
        int: -1 if the prod "overflows" the sum, meaning no solution found
        None: If no solution was found 
    """
    key = (ones_left, sum_so_far, prod_so_far)
    if key in memo:
        return memo[key]

    # If they are equal, we have a solution, which might not be minimal
    if sum_so_far == prod_so_far:
        return sum_so_far

    # If the prod is higher, we "overflowed" the solution, 
    # meaning we can stop bruteforcing this subspace
    if prod_so_far > sum_so_far:
        memo[key] = -1
        return -1  # -1 means overflow to us

    min_solution = None

    for i in range(2, original_k + 1):  # I think this limit could be tighter
        partial_sol = get_solution(
            ones_left - 1, 
            sum_so_far + (i - 1),  # We substract one since we are removing a one from the list 
            prod_so_far * i,
            original_k
        )

        if partial_sol is not None:
            if partial_sol == -1:
                break
            if min_solution is None:
                min_solution = partial_sol
            else:
                if partial_sol < min_solution:
                    min_solution = partial_sol
        
    memo[key] = min_solution

    return min_solution
        

def f(k):
    # Note we are brute forcing here
    return get_solution(k, k, 1, k)

def sum_f_k(n):
    """
    Return the sum of f(k) for k in 2 <= k <= n
    """
    answers = set()
    for k in range(2, n + 1):
        if k % 100 == 0:
            print(f'Getting solution for {k}')
        answers.add(f(k))

    return sum(answers)

assert f(2) == 4, f(2)
assert f(3) == 6, f(3)
assert f(4) == 8, f(4)
assert f(5) == 8, f(5)
assert f(6) == 12, f(6)

assert sum_f_k(6) == 30
assert sum_f_k(12) == 61

print('Unit tests OK')

print(sum_f_k(12000))
