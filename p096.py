def solve(s):
    if completed(s):
        return int(s[0:3])

    if violates_rules(s):
        return False

    return brute_force(s)

def violates_rules(s):
    return violates_rows(s) or violates_columns(s) or violates_squares(s)

def violates_rows(s):
    for i in range(9):
        if violates_row(s, i):
            return True

    return False

def violates_row(s, i):
    row = s[9*i : 9*(i+1)]

    return repeated_numbers(row)

def violates_columns(s):
    for i in range(9):
        if violates_column(s, i):
            return True

    return False

def violates_column(s, i):
    column = s[i : 81 : 9]

    return repeated_numbers(column)

def violates_squares(s):
    squares_top_left = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    
    for top_left in squares_top_left:
        if violates_square_with_top_left(s, top_left):
            return True

    return False

def violates_square_with_top_left(s, top_left):
    sq = s[top_left:top_left + 3] + s[top_left + 9:top_left + 12] + s[top_left + 18:top_left + 21]

    return repeated_numbers(sq)

def repeated_numbers(substring):
    preprocessed_substring = substring.replace("0", "")
    length = len(preprocessed_substring)

    if length > 0:
        return length != len(set(preprocessed_substring))

    return False

def completed(s):
    if s.find('0') == -1 and violates_rules(s):
        return False

    return s.find('0') == -1 and not violates_rules(s)

def brute_force(s):
    first_zero = s.find('0')
    s_list = list(s)
    
    if first_zero == -1:
        return False

    for i in range(1, 10):
        s_list[first_zero] = str(i)
        s_back_to_string = "".join(s_list)

        result = solve(s_back_to_string)
        if result:
            return result

    return False

total = 0

with open('p096_sudoku.txt', 'r') as f:
    for sudoku in f.readlines():
        print('solved')
        total += solve(sudoku)

print(total)