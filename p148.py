def triangle(rows):
    triangle = []
    triangle.append([1])
    triangle.append([1, 1])

    for i in range(0, rows - 2):
        tmp = [1]
        lastRow = len(triangle) - 1
        for i in range (0, len(triangle[lastRow]) - 1):
            tmp.append((triangle[lastRow][i] + triangle[lastRow][i + 1]) % 7)
        tmp.append(1)
        triangle.append(tmp)
    return triangle


def pretty_print(triangle, rows_to_print, non_divisibles_only=False):
    for i in range(rows_to_print):
        indent = " "*(rows_to_print - i - 1)
        row = triangle[i]
        if non_divisibles_only:
            row_str = [str(el) if el != 0 else ' ' for el in row]
        else:
            row_str = [str(el) for el in row]
        row = " ".join(row_str)

        if i % 7 == 0 and i != 0:
            print(f"{(i + 1):03}: {indent}{row} <-- relevant")
        else:
            print(f"{(i + 1):03}: {indent}{row}")


def total_divisible(rows):
    totalDivisible = 0

    for i in range(0, rows):
        divBySevenCount = 0
        for element in pascalTriangle[i]:
            if element % 7 == 0:
                divBySevenCount += 1
        totalDivisible += divBySevenCount
        # print("Row: " + str(i + 1) + ". Divs by 7: " + str(divBySevenCount))

    print(f"Divisible by 7 in {rows} rows: {totalDivisible}")


def total_non_divisible(rows):
    totalNonDivisible = 0

    for i in range(0, rows):
        nonDivBySevenCount = 0
        for element in pascalTriangle[i]:
            if element%7 != 0:
                nonDivBySevenCount += 1
        totalNonDivisible += nonDivBySevenCount
        # print("Row: " + str(i + 1) + ". Non-divs by 7: " + str(nonDivBySevenCount))

    print(f"Non-divisible by 7 in {rows} rows: {totalNonDivisible}")


MEMO = {1: 0}
def f(n):
    """How many entries are divisible by 7 up to row 7**n"""
    if n in MEMO:
        return MEMO[n]

    m = 7**(n - 1)

    result = int((21 * (m-1) * m) // 2) + 28*f(n - 1)
    MEMO[n] = result
    print(f"f({n}) = Divisible by 7 in the first {7**n} rows = {result}")
    return result


def decompose_in_7_powers(n):
    def split(n):
        """
        Consider the max power so n can be written as:
        `n = base * (7**power) + reminder`.

        Returns a tuple of (base, power, reminder)
        """
        power = 0
        while 7**power <= n:
            power += 1
        power = power - 1
        base = int(n // (7**power))
        reminder = n - base * (7**power)

        return (base, power, reminder)

    result = []
    r = n
    while r >= 7:
        b, p, r = split(r)
        result.append((b, p))
    if r != 0:  # Add final reminder, if any
        result.append((0, r))
    return result


def g(n):
    """Number of non-zero entries (NON-divisible by 7) in the
     first 'n' rows of the Pascal triangle"""
    powers_7 = decompose_in_7_powers(n)
    total_non_zeroes = 0
    leaves = 1
    for a, b in powers_7:
        if a != 0:
            triangles_non_full_zeroes = int((a * (a + 1)) // 2)
            zeroes_in_triangles_non_full_zeroes = f(b)
            triangles_full_zeroes = 0 if a < 2 else int(((a - 1)*a)//2)
            zeroes_in_triangles_full_zeroes = int(((7**(b) - 1) * 7**(b))//2)
            zeroes = (
                triangles_non_full_zeroes * zeroes_in_triangles_non_full_zeroes
                + triangles_full_zeroes * zeroes_in_triangles_full_zeroes
            )
            level_zeroes = zeroes
            level_entries = int((a*(7**b) * (a*(7**b) + 1))//2)
            level_non_zeroes = leaves * (level_entries - level_zeroes)
            total_non_zeroes = total_non_zeroes + level_non_zeroes
        elif a == 0:
            # These are not level_zeroes, these are level_non_zeroes
            level_non_zeroes = leaves * int((b * (b+1)) // 2)
            total_non_zeroes = total_non_zeroes + level_non_zeroes
        leaves = leaves * (a + 1)

    return total_non_zeroes


ROWS = 108
pascalTriangle = triangle(ROWS)
pretty_print(pascalTriangle, ROWS, non_divisibles_only=True)
total_divisible(ROWS)
total_non_divisible(ROWS)

f(2)
f(3)
f(10)


# 10**9 = 3*(7**10) + 3*(7**9) + 5*(7**8) + 3*(7**7) + 1*(7**6) + 6*(7**5) + 6*(7**2) + 7 + 6
print(3*(7**10) + 3*(7**9) + 5*(7**8) + 3*(7**7) + 1*(7**6) + 6*(7**5) + 6*(7**2) + 7 + 6)

print(decompose_in_7_powers(10**2))

assert g(7) == 28
assert g(100) == 2361  # From the problem description
assert g(108) == 2472
assert g(73) == 1168

print("g(10**9):", g(10**9))