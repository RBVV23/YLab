import random
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
        for x in range(y*SIZE_BOARD, (y+1)*SIZE_BOARD):
            if x != (y+1)*SIZE_BOARD-1:
                print(f'{board_list[x]:^{CELL_WIDTH}}', end='|')
            else:
                print(f'{board_list[x]:^{CELL_WIDTH}}')

        if y != (SIZE_BOARD-1):
            for x in range(y*SIZE_BOARD, (y+1)*SIZE_BOARD):
                if x != (y+1)*SIZE_BOARD-1:
                    print(f'{CELL_BOARD:^{CELL_WIDTH}}', end='|')
                else:
                    print(f'{CELL_BOARD:^{CELL_WIDTH}}')

def horizontal_chek(board, mark, position):
    in_line = 1

    left_board = (position // SIZE_BOARD) * SIZE_BOARD
    left_stop = position - LOOSE_CONDITION + 1
    to_left = max(left_stop, left_board)

    for pos in reversed(range(to_left, position)):  # to left
        # print(f'\tLEFT: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    right_board = (position // SIZE_BOARD) * SIZE_BOARD + (SIZE_BOARD - 1)
    right_stop = position + LOOSE_CONDITION - 1
    to_right = min(right_stop, right_board)

    for pos in range(position + 1, to_right + 1):  # to right
        # print(f'\tRIGHT: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break
    if in_line >= LOOSE_CONDITION:
        return True
    else:
        return False

def vertical_check(board, mark, position):
    in_line = 1

    up_board = position % SIZE_BOARD
    up_stop = position - SIZE_BOARD * (LOOSE_CONDITION - 1)
    to_up = max(up_stop, up_board)

    for pos in reversed(range(to_up, position, SIZE_BOARD)):  # to up
        # print(f'\tUP: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    down_board = position % SIZE_BOARD + SIZE_BOARD * (SIZE_BOARD - 1)
    down_stop = position + SIZE_BOARD * (LOOSE_CONDITION - 1)
    to_down = min(down_stop, down_board)

    for pos in range(position + SIZE_BOARD, to_down + SIZE_BOARD, SIZE_BOARD):  # to down
        # print(f'\tDOWN: board[{pos}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    if in_line >= LOOSE_CONDITION:
        return True
    else:
        return False

def down_right_diagonal_check(board, mark, position):
    in_line = 1

    n_column = position % SIZE_BOARD
    n_string = position // SIZE_BOARD

    left_up_stop = position - (SIZE_BOARD + 1) * (LOOSE_CONDITION - 1)
    diagonal_back_steps = min(n_string, n_column)
    left_up_board = position - (SIZE_BOARD + 1) * diagonal_back_steps
    to_left_up = max(left_up_board, left_up_stop)
    print(f'to_left_up = ', to_left_up)

    for pos in reversed(range(to_left_up, position, SIZE_BOARD+1)): # from left-up to position
        print(f'\tLeft-Up: board[{pos+1}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    right_down_stop = position + (SIZE_BOARD + 1) * (LOOSE_CONDITION - 1)
    diagonal_forward_steps = SIZE_BOARD - max(n_string, n_column) - 1
    right_down_board = position + (SIZE_BOARD + 1) * diagonal_forward_steps
    to_right_down = min(right_down_board, right_down_stop)
    print(f'to_right_down = {to_right_down}')

    for pos in range(position+SIZE_BOARD+1, to_right_down+SIZE_BOARD+1, SIZE_BOARD+1): # from position to right_down
        print(f'\tRight-Down: board[{pos+1}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    if in_line >= LOOSE_CONDITION:
        return True
    else:
        return False

def up_left_diagonal_check(board, mark, position):
    in_line = 1

    n_column = position % SIZE_BOARD
    n_string = position // SIZE_BOARD

    right_up_stop = position - (SIZE_BOARD - 1) * (LOOSE_CONDITION - 1)
    diagonal_back_steps = min(n_string, SIZE_BOARD-n_column-1)
    right_up_board = position - (SIZE_BOARD - 1) * diagonal_back_steps
    to_right_up = max(right_up_board, right_up_stop)
    print(f'to_right_up = {to_right_up}')

    for pos in reversed(range(to_right_up, position, SIZE_BOARD - 1)):  # from right-up to position
        print(f'\tRight-Up: board[{pos+1}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    left_down_stop = position + (SIZE_BOARD - 1) * (LOOSE_CONDITION - 1)
    # print(f'left_down_stop = {left_down_stop}')
    diagonal_forward_steps = min(SIZE_BOARD-n_string-1, n_column)
    left_down_board = position + (SIZE_BOARD - 1) * diagonal_forward_steps
    # print(f'left_down_board = {left_down_board}')
    to_left_down = min(left_down_board, left_down_stop)
    print(f'to_left_down = {to_left_down}')

    for pos in range(position + SIZE_BOARD - 1, to_left_down + SIZE_BOARD - 1,
                     SIZE_BOARD - 1):  # from position to right_down
        print(f'\tLeft-Down: board[{pos+1}] = {board[pos]}')
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    if in_line >= LOOSE_CONDITION:
        return True
    else:
        return False

def my_loose_check(board, mark, position):
    # """Returns boolean value whether the player wins the game."""
    if horizontal_chek(board, mark, position):
        return True
    elif vertical_check(board, mark, position):
        return True
    elif down_right_diagonal_check(board, mark, position):
        return True
    elif up_left_diagonal_check(board, mark, position):
        return True
    else:
        return False

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
board = ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', '10']

board = ['X',  '2',  '3',  '4',  '5',  '6', '7',  '8',  '9',  'X',
         '11', 'X', '13', '14', '15', '16', '17', '18', 'X', '20',
         '21', '22', 'X', '24', 'X', '26', '27', 'X', '29', '30',
         '31', '32', '33', '34', 'X', '36', 'O', '38', '39', '40',
         '41', '42', '43', '44', '45', 'O', '47', '48', '49', '50',
         '51', '52', '53', '54', 'O', 'O', '57', '58', '59', '60',
         '61', '62', '63', 'X', '65', '66', 'O', '68', '69', '70',
         '71', '72', 'X', '74', 'X', '76', '77', 'X', '79', '80',
         '81', 'X', '83', '84', 'X', '86', '87', '88', 'X', '90',
         'X', '92', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
# marker = 'X'
# input_pos = 100
# position= input_pos - 1



# position=65
# print(f'position = {position}')
# up_board = position % SIZE_BOARD
# down_board = position % SIZE_BOARD + SIZE_BOARD*(SIZE_BOARD-1)
# up_stop = position - SIZE_BOARD*(LOOSE_CONDITION-1)
# down_stop = position + SIZE_BOARD*(LOOSE_CONDITION-1)
# left_board = (position // SIZE_BOARD) * SIZE_BOARD
# left_stop = position - LOOSE_CONDITION + 1
# to_up = max(up_stop, up_board)
# to_down = min(down_stop, down_board)
# print(f'{up_board}-{down_board}')
# print(f'{up_stop}-{down_stop}')
# print(f'{to_up}-{to_down}')
# print(list(range(to_up, to_down, SIZE_BOARD)))


# left_up_stop = position - (SIZE_BOARD+1)*(LOOSE_CONDITION-1)
# right_down_stop = position + (SIZE_BOARD+1)*(LOOSE_CONDITION-1)
# n_column = position % SIZE_BOARD
# n_string = position // SIZE_BOARD
# diagonal_back_steps = min(n_string, n_column)
# left_up_board = position - (SIZE_BOARD+1)*diagonal_back_steps
# diagonal_forward_steps = SIZE_BOARD - max(n_string, n_column) - 1
# right_down_board = position + (SIZE_BOARD+1)*diagonal_forward_steps

# to_left_up = max(left_up_board, left_up_stop)
# to_right_down = min(right_down_board, right_down_stop)





def full_board_check(board):
    """Returns boolean value whether the game board is full of game marks."""
    return len(set(board)) == 2

def space_check(board, position):
    """Returns boolean value whether the cell is free or not."""
    return board[position] not in PLAYERS_MARKS

def computer_choice(board, mark):
    if not full_board_check(board):
        variants = [i for i in range(SIZE_BOARD**2)]
        random.shuffle(variants)
        for position in variants:
            # print(f'\tPC хочет [{position+1}]')
            if space_check(board, position):
                if my_loose_check(board, mark, position) != True:
                    # print(f'\tPC ставит [{position + 1}]')
                    return position
                else:
                    # print(f'\t\tPC считает ход [{position + 1}] проигрышным!')
                    last_possible = position
                continue
            else:
                # print(f'\t\tPC видит, что клетка [{position + 1}] уже занята!')
                continue
        # print('PC видит, что проиграл')
        return last_possible
    else:
        print('Нет свободных клеток - ничья')
        return None

board = PLAY_BOARD

def place_marker(board, marker, position):
    """Puts a player mark to appropriate position."""
    board[position] = marker


def switch_player(old_player, old_mark):
    """Switches player's marks to play next turn."""
    if old_mark == PLAYERS_MARKS[0]:
        CURRENT_MARK = PLAYERS_MARKS[1]
    else:
        CURRENT_MARK = PLAYERS_MARKS[0]
    CURRENT_PLAYER = not old_player
    return CURRENT_PLAYER, CURRENT_MARK

# my_display_board(PLAY_BOARD)

print('Welcome to Tic Tac Toe!')

def my_player_input():
    """Gets player's input string to choose the game mark to play."""
    HUMAN_MARK = ''
    while HUMAN_MARK not in PLAYERS_MARKS:
        # HUMAN_MARK = 'X'
        HUMAN_MARK = input(f'Please, choose your marker: {PLAYERS_MARKS[0]} or {PLAYERS_MARKS[1]}: ').upper()

    if HUMAN_MARK == PLAYERS_MARKS[0]:
        PC_MARK = PLAYERS_MARKS[1]
    else:
        PC_MARK = PLAYERS_MARKS[0]

    return HUMAN_MARK, PC_MARK

HUMAN_MARK, PC_MARK = my_player_input()

def choose_first():
    """Randomly returns the player's mark that goes first."""
    first_mark = PLAYERS_MARKS[random.choice((0, 1))]
    if first_mark == HUMAN_MARK:
        return False, HUMAN_MARK
    else:
        return True, PC_MARK

CURRENT_PLAYER, CURRENT_PLAYER_MARK = choose_first()

# CURRENT_PLAYER =

print(f'Player with mark "{CURRENT_PLAYER_MARK}" goes first.')


def my_player_choice(board, player_mark):
    """Gets player's next position and check if it's appropriate to play."""
    position = 0

    while position not in [num for num in range(1, 1+SIZE_BOARD**2)]:
        try:
            position = \
                int(input(f'Player "{player_mark}", choose your next position from {1} to {SIZE_BOARD**2}: '))
        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')

    position -= 1
    if space_check(board, position):
        return position, True

    return -1, False
def check_game_finish(board, mark, position):
    """Return boolean value is the game finished or not."""
    if my_loose_check(board, mark, position):
        print(f'The player with the mark "{mark}" loses!')
        return True
    if full_board_check(PLAY_BOARD):
        print('The game ended in a draw.')
        return True
    return False
def replay():
    """Asks the players to play again."""
    decision = ''
    while decision not in ('y', 'n'):
        decision = input('Would you like to play again? Type "y" or "n"').lower()

    return decision == 'y'
def clear_screen():
    """Clears the game screen via adding new rows."""
    print('\n' * 100)

while True:
    my_display_board(PLAY_BOARD)

    print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')

    if CURRENT_PLAYER: # ход компьютера
        POSITION = computer_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
    else: # ход человека
        POSITION = computer_choice(PLAY_BOARD, HUMAN_MARK)
        # POSITION, check = my_player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
        # while not check:
        #     print(f'Player "{CURRENT_PLAYER_MARK}", this position is not empty! Try again!')
        #     POSITION, check = my_player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)

    print(f'POSITION = {POSITION}')
    place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, POSITION)

    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK, POSITION):
        my_display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            clear_screen()
            PLAY_BOARD = [str(num) for num in range(1, 1 + SIZE_BOARD ** 2)]
            PLAYER_MARKS = my_player_input()
            CURRENT_PLAYER, CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER, CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER, CURRENT_PLAYER_MARK)
    # clear_screen()
