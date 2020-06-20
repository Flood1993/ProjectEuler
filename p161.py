
def first_empty_pos(board):
    return board.find('0')

memo = {}

def find_ways(board):
    global memo
    fep = first_empty_pos(board)

    if fep == -1:
        return 1

    if board in memo:
        return memo[board]

    result = 0

    if can_place_horizontal_3(board, fep):
        result = result + find_ways(place_horizontal_3(board, fep))

    if can_place_vertical_3(board, fep):
        result = result + find_ways(place_vertical_3(board, fep))

    if can_place_type_1(board, fep):
        result = result + find_ways(place_type_1(board, fep))
    
    if can_place_type_2(board, fep):
        result = result + find_ways(place_type_2(board, fep))
    
    if can_place_type_3(board, fep):
        result = result + find_ways(place_type_3(board, fep))
    
    if can_place_type_4(board, fep):
        result = result + find_ways(place_type_4(board, fep))
    
    memo[board] = result
    return result

def can_place_horizontal_3(board, pos):
    if pos%9 > 6:
        return False

    return board[pos] == '0' and board[pos+1] == '0' and board[pos+2] == '0'

def place_horizontal_3(board, pos):
    board_list = list(board)
    board_list[pos] = '1'
    board_list[pos+1] = '1'
    board_list[pos+2] = '1'
    return ''.join(board_list)

def can_place_vertical_3(board, pos):
    if pos > 89:
        return False

    return board[pos] == '0' and board[pos+9] == '0' and board[pos+18] == '0'

def place_vertical_3(board, pos):
    board_list = list(board)
    board_list[pos] = '1'
    board_list[pos+9] = '1'
    board_list[pos+18] = '1'
    return ''.join(board_list)

"""
##
#
"""
def can_place_type_1(board, pos):
    if pos%9 == 8 or pos > 98:
        return False

    return board[pos] == '0' and board[pos+1] == '0' and board[pos+9] == '0'

def place_type_1(board, pos):
    board_list = list(board)
    board_list[pos] = '1'
    board_list[pos+1] = '1'
    board_list[pos+9] = '1'
    return ''.join(board_list)

"""
##
 #
"""
def can_place_type_2(board, pos):
    if pos%9 == 8 or pos > 98:
        return False

    return board[pos] == '0' and board[pos+1] == '0' and board[pos+10] == '0'

def place_type_2(board, pos):
    board_list = list(board)
    board_list[pos] = '1'
    board_list[pos+1] = '1'
    board_list[pos+10] = '1'
    return ''.join(board_list)

"""
#
##
"""
def can_place_type_3(board, pos):
    if pos%9 == 8 or pos > 98:
        return False

    return board[pos] == '0' and board[pos+9] == '0' and board[pos+10] == '0'

def place_type_3(board, pos):
    board_list = list(board)
    board_list[pos] = '1'
    board_list[pos+9] = '1'
    board_list[pos+10] = '1'
    return ''.join(board_list)

"""
 #
##
"""
def can_place_type_4(board, pos):
    if pos%9 == 0 or pos > 98:
        return False

    return board[pos] == '0' and board[pos+8] == '0' and board[pos+9] == '0'

def place_type_4(board, pos):
    board_list = list(board)
    board_list[pos] = '1'
    board_list[pos+8] = '1'
    board_list[pos+9] = '1'
    return ''.join(board_list)

print(find_ways('0'*(9*12)))