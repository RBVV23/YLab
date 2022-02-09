"""
Reverse Tic-Tac-Toe game.
"""

import random
from math import log10, ceil

LOOSE_CONDITION = 5
SIZE_BOARD = 10
PLAY_BOARD = [str(num) for num in range(1, 1+SIZE_BOARD**2)]
PLAYERS_MARKS = tuple(['X','O'])


CELL_BOARD = '-'*ceil(2*log10(SIZE_BOARD))
CELL_WIDTH = int(2*log10(SIZE_BOARD)+2)


def display_board(board_list):
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


def horizontal_check(board, mark, position):
    """Returns boolean value whether a horizontal line has been collected"""
    in_line = 1

    left_board = (position // SIZE_BOARD) * SIZE_BOARD
    left_stop = position - LOOSE_CONDITION + 1
    to_left = max(left_stop, left_board)

    for pos in reversed(range(to_left, position)):  # цикл для прохода справа налево от нового маркера
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    right_board = (position // SIZE_BOARD) * SIZE_BOARD + (SIZE_BOARD - 1)
    right_stop = position + LOOSE_CONDITION - 1
    to_right = min(right_stop, right_board)

    for pos in range(position + 1, to_right + 1):  # цикл для прохода слева направо от нового маркера
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break
    return in_line >= LOOSE_CONDITION


def vertical_check(board, mark, position):
    """Returns boolean value whether a vertical line has been collected"""
    in_line = 1

    up_board = position % SIZE_BOARD
    up_stop = position - SIZE_BOARD * (LOOSE_CONDITION - 1)
    to_up = max(up_stop, up_board)

    # цикл для прохода снизу вверх от нового маркера
    for pos in reversed(range(to_up, position, SIZE_BOARD)):
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    down_board = position % SIZE_BOARD + SIZE_BOARD * (SIZE_BOARD - 1)
    down_stop = position + SIZE_BOARD * (LOOSE_CONDITION - 1)
    to_down = min(down_stop, down_board)

    # цикл для прохода сверху вниз от нового маркера
    for pos in range(position + SIZE_BOARD, to_down + SIZE_BOARD, SIZE_BOARD):
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    return in_line >= LOOSE_CONDITION


def down_right_diagonal_check(board, mark, position):
    """Returns boolean value whether a down-right diagonal line has been collected"""
    in_line = 1

    n_column = position % SIZE_BOARD
    n_string = position // SIZE_BOARD

    left_up_stop = position - (SIZE_BOARD + 1) * (LOOSE_CONDITION - 1)
    diagonal_back_steps = min(n_string, n_column)
    left_up_board = position - (SIZE_BOARD + 1) * diagonal_back_steps
    to_left_up = max(left_up_board, left_up_stop)

    # цикл для прохода налево и вверх от нового маркера
    for pos in reversed(range(to_left_up, position, SIZE_BOARD+1)):
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    right_down_stop = position + (SIZE_BOARD + 1) * (LOOSE_CONDITION - 1)
    diagonal_forward_steps = SIZE_BOARD - max(n_string, n_column) - 1
    right_down_board = position + (SIZE_BOARD + 1) * diagonal_forward_steps
    to_right_down = min(right_down_board, right_down_stop)

    # цикл для прохода направо и вниз от нового маркера
    for pos in range(position+SIZE_BOARD+1, to_right_down+SIZE_BOARD+1, SIZE_BOARD+1):
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    return in_line >= LOOSE_CONDITION


def up_left_diagonal_check(board, mark, position):
    """Returns boolean value whether a up-left diagonal line has been collected"""
    in_line = 1

    n_column = position % SIZE_BOARD
    n_string = position // SIZE_BOARD

    right_up_stop = position - (SIZE_BOARD - 1) * (LOOSE_CONDITION - 1)
    diagonal_back_steps = min(n_string, SIZE_BOARD-n_column-1)
    right_up_board = position - (SIZE_BOARD - 1) * diagonal_back_steps
    to_right_up = max(right_up_board, right_up_stop)

    # цикл для прохода вправо и вверх от нового маркера
    for pos in reversed(range(to_right_up, position, SIZE_BOARD - 1)):
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    left_down_stop = position + (SIZE_BOARD - 1) * (LOOSE_CONDITION - 1)
    diagonal_forward_steps = min(SIZE_BOARD-n_string-1, n_column)
    left_down_board = position + (SIZE_BOARD - 1) * diagonal_forward_steps
    to_left_down = min(left_down_board, left_down_stop)

    # цикл для прохода налево и вниз от нового маркера
    for pos in range(position + SIZE_BOARD - 1, to_left_down + SIZE_BOARD - 1, SIZE_BOARD - 1):
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    return in_line >= LOOSE_CONDITION


def loose_check(board, mark, position):
    """Returns boolean value whether the player loses the game."""
    return horizontal_check(board, mark, position) + \
        vertical_check(board, mark, position) + \
        down_right_diagonal_check(board, mark, position) + \
        up_left_diagonal_check(board, mark, position)


def full_board_check(board):
    """Returns boolean value whether the game board is full of game marks."""
    return len(set(board)) == 2


def space_check(board, position):
    """Returns boolean value whether the cell is free or not."""
    return board[position] not in PLAYERS_MARKS


def computer_choice(board, mark):
    """Returns position of computer's move"""
    if not full_board_check(board):
        variants = [i for i in range(SIZE_BOARD**2)]
        random.shuffle(variants)
        for position in variants:
            if space_check(board, position):
                if not loose_check(board, mark, position):
                    return position  # ход компьютера
                else:
                    last_possible = position
                continue
            else:
                continue
        return last_possible  # случай проигрыша компьютера
    else:
        return None  # случай ничейного результата


def place_marker(board, marker, position):
    """Puts a player mark to appropriate position."""
    board[position] = to_paint_marks(marker)


def mark_change(mark):
    if mark == PLAYERS_MARKS[0]:
        return PLAYERS_MARKS[1]
    else:
        return PLAYERS_MARKS[0]

def switch_player(old_player, old_mark):
    """Switches players to play next turn."""

    CURRENT_MARK = mark_change(old_mark)
    CURRENT_PLAYER = not old_player
    return CURRENT_PLAYER, CURRENT_MARK


def player_input():
    """Gets player's input string to choose the game mark to play."""
    HUMAN_MARK = ''
    while HUMAN_MARK not in PLAYERS_MARKS:
        HUMAN_MARK = input(f'Please, choose your marker: {PLAYERS_MARKS[0]} or {PLAYERS_MARKS[1]}: ').upper()

    PC_MARK = mark_change(HUMAN_MARK)

    return HUMAN_MARK, PC_MARK

def to_paint_marks(mark):
    if mark == PLAYERS_MARKS[0]:
        mark_painted = '\033[31m X  \033[00m'
    else:
        mark_painted = '\033[34m O  \033[00m'
    return mark_painted

def choose_first():
    """Randomly returns the player that goes first."""
    first_mark = PLAYERS_MARKS[random.choice((0, 1))]
    if first_mark == HUMAN_MARK:
        return False, HUMAN_MARK
    else:
        return True, PC_MARK


def player_choice(board, player_mark):
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

    return -1, False  # случай занятой клетки


def check_game_finish(board, mark, position):
    """Return boolean value is the game finished or not."""
    mark_paint = to_paint_marks(mark)
    if loose_check(board, mark_paint, position):
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


print('Welcome to Tic Tac Toe!')

HUMAN_MARK, PC_MARK = player_input()
CURRENT_PLAYER, CURRENT_PLAYER_MARK = choose_first()

print(f'Player with mark "{CURRENT_PLAYER_MARK}" goes first.')

# основной цикл программы
while True:
    display_board(PLAY_BOARD)

    print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')

    if CURRENT_PLAYER:
        POSITION = computer_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
    else:
        POSITION, check = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
        while not check:
            print(f'Player "{CURRENT_PLAYER_MARK}", this position is not empty! Try again!')
            POSITION, check = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)

    place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, POSITION)

    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK, POSITION):
        display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            clear_screen()
            PLAY_BOARD = [str(num) for num in range(1, 1 + SIZE_BOARD ** 2)]
            HUMAN_MARK, PC_MARK = player_input()
            CURRENT_PLAYER, CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER, CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER, CURRENT_PLAYER_MARK)
