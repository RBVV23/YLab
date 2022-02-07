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
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    right_board = (position // SIZE_BOARD) * SIZE_BOARD + (SIZE_BOARD - 1)
    right_stop = position + LOOSE_CONDITION - 1
    to_right = min(right_stop, right_board)

    for pos in range(position + 1, to_right + 1):  # to right
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
mark = 'X'
input_pos = 3
position= input_pos - 1

# print(horizontal_chek(board, mark, position))

my_display_board(PLAY_BOARD)

position=65
print(f'position = {position}')
up_board = position % SIZE_BOARD
down_board = position % SIZE_BOARD + SIZE_BOARD*(SIZE_BOARD-1)
up_stop = position - SIZE_BOARD*(LOOSE_CONDITION-1)
down_stop = position + SIZE_BOARD*(LOOSE_CONDITION-1)
left_board = (position // SIZE_BOARD) * SIZE_BOARD
left_stop = position - LOOSE_CONDITION + 1
to_up = max(up_stop, up_board)
to_down = min(down_stop, down_board)
print(f'{up_board}-{down_board}')
print(f'{up_stop}-{down_stop}')
print(f'{to_up}-{to_down}')
print(list(range(to_up, to_down, SIZE_BOARD)))

def vertical_check(board, mark, position):
    ...
