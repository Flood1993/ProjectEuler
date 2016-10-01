s = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"

assert len(s) == 81

L = [[] for i in range(81)]

print(L)

for i in range(len(s)):
    if s[i] != '0':
        L[i] = int(s[i])

def get_pos(p):
    """
    Returns the pos of p in format row, column.
    """
    return (p//9, p%9)

def check_candidates(s, p):
    """
    Note that the position p in the real sudoku is (p//9, p%9),
    being 0,0 (s[0]) the topleft most cell and 8,8 (s[80]) the
    bottomright cell.
    """
    candidates = [True for i in range(10)] # Each position represents whether the i number can be placed there
    candidates[0] = False

    # Check rows.
    cur_pos = get_pos(s, p)
    for i in range(81):
        if get_pos(s, i)[0] == cur_pos[0] and not isinstance(s[i], List):
            candidates[s[i]] = False
    
    # Check columns.

    # Check square.

print(L)
