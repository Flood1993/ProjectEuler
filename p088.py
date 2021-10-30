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

print('First attempt unit tests OK, even tho it does not scale well')


class Memo:
    def __init__(self):
        self._memo = dict()

    def get(self, key):
        return self._memo.get(key)

    def memo(self, key, value):
        self._memo[key] = value

    def memo_if_lower(self, key, value):
        current_value = self.get(key)

        if current_value is None or value < current_value:
            self.memo(key, value)

memo2 = Memo()

def f(prod_til_now, sum_til_now, ones_left, not_ones_so_far):
    global memo2
    for i in range(2, 12001):
        new_prod = prod_til_now * i
        new_sum = sum_til_now + i
        new_ones_left = ones_left - 1
        new_not_ones_so_far = not_ones_so_far + 1 

        if new_prod == new_sum:
            solution = new_prod  # or new_sum since they are equal
            memo2.memo_if_lower(new_not_ones_so_far, solution)

        if new_prod > new_sum + new_ones_left:
            break

        memo2.memo_if_lower(new_not_ones_so_far + (new_prod - new_sum), new_prod)

        f(new_prod, new_sum, new_ones_left, new_not_ones_so_far)

def sum_f_k2(n):
    """
    Return the sum of f(k) for k in 2 <= k <= n
    """
    answers = set()
    for k in range(2, n + 1):
        if k % 100 == 0:
            print(f'Getting solution for {k}')
        answers.add(memo2.get(k))

    return sum(answers)

f(1, 0, 12000, 0)

assert memo2.get(2) == 4, memo2.get(2)
assert memo2.get(3) == 6, memo2.get(2)
assert memo2.get(4) == 8, memo2.get(2)
assert memo2.get(5) == 8, memo2.get(2)
assert memo2.get(6) == 12, memo2.get(2)

assert sum_f_k2(6) == 30, sum_f_k2(6)
assert sum_f_k2(12) == 61, sum_f_k2(12)

print(sum_f_k2(12000))
