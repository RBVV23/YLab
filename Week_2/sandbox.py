from math import log10, ceil

LOOSE_CONDITION = 5
SIZE_BOARD = 10
PLAY_BOARD = [str(num) for num in range(1, 1+SIZE_BOARD**2)]
PLAYERS_MARKS = ['X', 'O']


CELL_BOARD = '-'*ceil(2*log10(SIZE_BOARD))
CELL_WIDTH = int(2*log10(SIZE_BOARD)+2)
# print(f'width = {CELL_WIDTH}')
# print(f'cell_border = {CELL_BOARD}')

def my_display_board(board_list):
    """Prints the game board."""

    for y in range(SIZE_BOARD):
        for x in range(y*SIZE_BOARD, (y+1)*SIZE_BOARD-1):
            if x != (y+1)*SIZE_BOARD-2:
                print(f'{board_list[x]:^{CELL_WIDTH}}', end='|')
            else:
                print(f'{board_list[(y+1)*SIZE_BOARD-1]:^{CELL_WIDTH}}')
        if y != (SIZE_BOARD-1):
            for x in range(y*SIZE_BOARD, (y+1)*SIZE_BOARD-1):
                if x != (y+1)*SIZE_BOARD-2:
                    print(f'{CELL_BOARD:^{CELL_WIDTH}}', end='|')
                else:
                    print(f'{CELL_BOARD:^{CELL_WIDTH}}')

def horizontal_chek(board, mark, position):
    in_line = 1

    left_board = (position // SIZE_BOARD) * SIZE_BOARD
    left_stop = position - LOOSE_CONDITION + 1
    to_left = max(left_stop, left_board)

    for pos in reversed(range(to_left, position)):  # to left
        print(f'\tLEFT: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    right_board = (position // SIZE_BOARD) * SIZE_BOARD + (SIZE_BOARD - 1)
    right_stop = position + LOOSE_CONDITION - 1
    to_right = min(right_stop, right_board)

    for pos in range(position + 1, to_right + 1):  # to right
        print(f'\tRIGHT: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break
    if in_line >= LOOSE_CONDITION:
        return True, in_line
    else:
        return False, in_line

def vertical_check(board, mark, position):
    in_line = 1

    up_board = position % SIZE_BOARD
    up_stop = position - SIZE_BOARD * (LOOSE_CONDITION - 1)
    to_up = max(up_stop, up_board)

    for pos in reversed(range(to_up, position, SIZE_BOARD)):  # to up
        print(f'\tUP: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    down_board = position % SIZE_BOARD + SIZE_BOARD * (SIZE_BOARD - 1)
    down_stop = position + SIZE_BOARD * (LOOSE_CONDITION - 1)
    to_down = min(down_stop, down_board)

    for pos in range(position + SIZE_BOARD, to_down + SIZE_BOARD, SIZE_BOARD):  # to down
        print(f'\tDOWN: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    if in_line >= LOOSE_CONDITION:
        return True, in_line
    else:
        return False, in_line

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
board = ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', '10']

board = ['1',  '2',  '3',  '4',  '5',  '6', '7',  '8',  '9',  '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', 'X', '26', '27', '28', '29', '30',
         '31', '32', '33', '34', 'X', '36', '37', '38', '39', '40',
         '41', '42', '43', '44', 'O', '46', '47', '48', '49', '50',
         '51', '52', '53', '54', 'X', '56', '57', '58', '59', '60',
         '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
         '71', '72', '73', '74', 'X', '76', '77', '78', '79', '80',
         '81', '82', '83', '84', 'X', '86', '87', '88', '89', '90',
         '91', '92', 'O', 'X', 'X', 'X', 'X', 'X', 'X', '100',]
mark = 'X'
input_pos = 89
position= input_pos - 1

print(horizontal_chek(board, mark, position))

my_display_board(PLAY_BOARD)

# position=65
print(f'position = {position}')
up_board = position % SIZE_BOARD
down_board = position % SIZE_BOARD + SIZE_BOARD*(SIZE_BOARD-1)
up_stop = position - SIZE_BOARD*(LOOSE_CONDITION-1)
down_stop = position + SIZE_BOARD*(LOOSE_CONDITION-1)
left_board = (position // SIZE_BOARD) * SIZE_BOARD
left_stop = position - LOOSE_CONDITION + 1
to_up = max(up_stop, up_board)
to_down = min(down_stop, down_board)
# print(f'{up_board}-{down_board}')
# print(f'{up_stop}-{down_stop}')
# print(f'{to_up}-{to_down}')
# print(list(range(to_up, to_down, SIZE_BOARD)))


left_up_stop = position - (SIZE_BOARD+1)*(LOOSE_CONDITION-1)
right_down_stop = position + (SIZE_BOARD+1)*(LOOSE_CONDITION-1)
n_column = position % SIZE_BOARD
n_string = position // SIZE_BOARD
diagonal_back_steps = min(n_string, n_column)
left_up_board = position - (SIZE_BOARD+1)*diagonal_back_steps
diagonal_forward_steps = SIZE_BOARD - max(n_string, n_column) - 1
right_down_board = position + (SIZE_BOARD+1)*diagonal_forward_steps

to_left_up = max(left_up_board, left_up_stop)
to_right_down = min(right_down_board, right_down_stop)

print(f'n_string = {n_string}')
print(f'n_column = {n_column}')
print(f'{left_up_stop}-{right_down_stop}')
print(f'{left_up_board}-{right_down_board}')
print(f'{to_left_up}-{to_right_down}')
print(list(range(to_left_up, position, SIZE_BOARD+1)))
print(list(range(position+SIZE_BOARD+1, to_right_down+SIZE_BOARD+1, SIZE_BOARD+1)))

def down_right_diagonal_check(board, mark, position):
    in_line = 1
    for pos in range(to_left_up, position, SIZE_BOARD+1): # from left-up to position
        print(f'\tL-D: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

down_right_diagonal_check(board, mark, position)