def solve_pell(n):
    """
    This function solves the Pell equation of the form:
    a*a - n * b*b = 1

    Input
    -----
    n - Integer
        Value of n. >= 2

    Output
    ------
    None
        If n is a perfect square (it has no solution)
    (a, b) - Tuple of integers
        Solutions for which the Pell equation is checked

    This function has been taken from the p066 solution forum
    https://projecteuler.net/thread=66
    """

    n1, d1 = 0, 1
    n2, d2 = 1, 0
    # These are the two bounding fractions

    while True:
        a = n1 + n2
        b = d1 + d2
        # a/b is the new candidate somewhere in the middle

        t = a*a - n*b*b  # See how close a^2/b^2 is to n 
        if t == 1: # You have your pell solution (a,b)
            return (a, b)
        elif t == 0: # N was a square = (a/b)^2
            return None;
        else: # Not there yet - adjust low or hi bound
            if t > 0:
                n2 =a
                d2 =b
            else:
                n1 =a
                d1 =b

max_D = 0
max_x = 0
for i in range(2, 1001):
    sol = solve_pell(i)
    if sol is None:
        continue
    if sol[0] > max_x:
        max_D, max_x = i, sol[0]

print(max_D)

solve_pell(-13)
    
