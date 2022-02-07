"""
Tic-Tac-Toe game.
"""
import random
from math import log10, ceil

SIZE_BOARD = 10
LOOSE_CONDITION = 5
PLAY_BOARD = [str(num) for num in range(1, 1+SIZE_BOARD**2)]
PLAYERS_MARKS = ['X', 'O']


CELL_BOARD = '-'*ceil(2*log10(SIZE_BOARD))
CELL_WIDTH = int(2*log10(SIZE_BOARD)+2)
print(f'width = {CELL_WIDTH}')
print(f'cell_border = {CELL_BOARD}')

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



my_display_board(PLAY_BOARD)

def my_player_input():
    """Gets player's input string to choose the game mark to play."""
    player_first = ''
    while player_first not in PLAYERS_MARKS:
        player_first = input(f'Please, choose your marker: {PLAYERS_MARKS[0]} or {PLAYERS_MARKS[1]}: ').upper()

    if player_first == PLAYERS_MARKS[0]:
        player_second = PLAYERS_MARKS[1]
    else:
        player_second = PLAYERS_MARKS[0]

    return player_first, player_second

my_player_input()

def place_marker(board, marker, position):
    """Puts a player mark to appropriate position."""
    board[position] = marker


def horizontal_chek(board, mark, position):
    in_line = 1

    left_board = (position // SIZE_BOARD) * SIZE_BOARD
    left_stop = position - LOOSE_CONDITION + 1
    to_left = max(left_stop, left_board)

    for pos in reversed(range(to_left, position)): # to left
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break

    right_board = (position // SIZE_BOARD) * SIZE_BOARD + (SIZE_BOARD - 1)
    right_stop = position + LOOSE_CONDITION - 1
    to_right = min(right_stop, right_board)

    for pos in range(position+1, to_right+1): # to right
        if board[pos] == mark:
            in_line += 1
            continue
        else:
            break
    if in_line >= LOOSE_CONDITION:
        return True
    else:
        return False


def vertical_chek(board, mark, cell):
    ...

def horizontal_chek(board, mark, cell):
    ...


def win_check(board, mark):
    """Returns boolean value whether the player wins the game."""
    return (board[0] == board[1] == board[2] == mark) or \
           (board[5] == board[4] == board[3] == mark) or \
           (board[8] == board[7] == board[6] == mark) or \
           (board[0] == board[5] == board[8] == mark) or \
           (board[1] == board[4] == board[7] == mark) or \
           (board[2] == board[3] == board[6] == mark)


def my_choose_first():
    """Randomly returns the player's mark that goes first."""
    return PLAYERS_MARKS[random.choice((0, 1))]


def space_check(board, position):
    """Returns boolean value whether the cell is free or not."""
    return board[position] not in PLAYERS_MARKS


def full_board_check(board):
    """Returns boolean value whether the game board is full of game marks."""
    return len(set(board)) == 2


def player_choice(board, player_mark):
    """Gets player's next position and check if it's appropriate to play."""
    position = 0

    while position not in [num for num in range(1, 10)]:
        try:
            position = \
                int(input(f'Player "{player_mark}", choose your next position from 1 to 9: '))
        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')

    position -= 1
    if space_check(board, position):
        return position

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


def switch_player(mark):
    """Switches player's marks to play next turn."""
    return 'O' if mark == 'X' else 'X'


def check_game_finish(board, mark):
    """Return boolean value is the game finished or not."""
    if win_check(board, mark):
        print(f'The player with the mark "{mark}" wins!')
        return True

    if full_board_check(PLAY_BOARD):
        print('The game ended in a draw.')
        return True

    return False

#
# print('Welcome to Tic Tac Toe!')
#
# PLAYER_MARKS = player_input()
# CURRENT_PLAYER_MARK = choose_first()
#
# print(f'Player with mark "{CURRENT_PLAYER_MARK}" goes first.')
#
# while True:
#     display_board(PLAY_BOARD)
#
#     print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')
#
#     PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
#     place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, PLAYER_POSITION)
#
#     if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK):
#         display_board(PLAY_BOARD)
#         if not replay():
#             break
#         else:
#             PLAY_BOARD = [str(num) for num in range(1, 10)]
#             PLAYER_MARKS = player_input()
#             CURRENT_PLAYER_MARK = choose_first()
#     else:
#         CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)
#     clear_screen()
