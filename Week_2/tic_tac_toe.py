"""
Tic-Tac-Toe game.
"""
import random

PLAY_BOARD = [str(num) for num in range(1, 10)]
PLAYERS_MARKS = ['X', 'O']


def display_board(board_list):
    """Prints the game board."""
    print(board_list[8] + ' | ' + board_list[7] + ' | ' + board_list[6])
    print('- | - | -')
    print(board_list[5] + ' | ' + board_list[4] + ' | ' + board_list[3])
    print('- | - | -')
    print(board_list[0] + ' | ' + board_list[1] + ' | ' + board_list[2])


def player_input():
    """Gets player's input string to choose the game mark to play."""
    player_first = ''
    while player_first not in ('X', 'O'):
        player_first = input('Please, choose your marker: X or O: ').upper()

    if player_first == 'X':
        player_second = 'O'
    else:
        player_second = 'X'

    return player_first, player_second


def place_marker(board, marker, position):
    """Puts a player mark to appropriate position."""
    board[position] = marker


def win_check(board, mark):
    """Returns boolean value whether the player wins the game."""
    return (board[0] == board[1] == board[2] == mark) or \
           (board[5] == board[4] == board[3] == mark) or \
           (board[8] == board[7] == board[6] == mark) or \
           (board[0] == board[5] == board[8] == mark) or \
           (board[1] == board[4] == board[7] == mark) or \
           (board[2] == board[3] == board[6] == mark)


def choose_first():
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


print('Welcome to Tic Tac Toe!')

PLAYER_MARKS = player_input()
CURRENT_PLAYER_MARK = choose_first()

print(f'Player with mark "{CURRENT_PLAYER_MARK}" goes first.')

while True:
    display_board(PLAY_BOARD)

    print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')

    PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
    place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, PLAYER_POSITION)

    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK):
        display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            PLAY_BOARD = [str(num) for num in range(1, 10)]
            PLAYER_MARKS = player_input()
            CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)
    clear_screen()
