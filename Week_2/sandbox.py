LOOSE_CONDITION = 5
SIZE_BOARD = 10

def horizontal_chek(board, mark, position):
    in_line = 1
    print('position', position)
    print('steps_to_right: ', SIZE_BOARD - position%SIZE_BOARD-1)
    print('steps_to_left: ', position%SIZE_BOARD)
    for i in range(1, LOOSE_CONDITION): #left
        print(i)
        if board[position - i] == mark:
            # print('continue')
            in_line += 1
            continue
        else:
            # print('break')
            break

    for i in range(1, LOOSE_CONDITION): #right
        if board[position + i] == mark:
            in_line += 1
            continue
        else:
            break
    print('end ', in_line)

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
board = ['X', 'X', '3', 'O', 'O', 'O', 'O', 'O', 'X', '10']
mark = 'O'
input_pos = 9
position= input_pos - 1

# horizontal_chek(board, mark, position)
position=12
print(f'position = {position}')
right_board = (position // SIZE_BOARD) * SIZE_BOARD + (SIZE_BOARD - 1)
right_stop = position + LOOSE_CONDITION - 1
left_board = (position // SIZE_BOARD) * SIZE_BOARD
left_stop = position - LOOSE_CONDITION + 1
to_right = min(right_stop, right_board)
to_left = min(left_stop, left_board)
print(f'{left_board}-{right_board}')
print(f'{left_stop}-{right_stop}')
