def print_board(board):
    for row in board:
        print(row)

def move(board, location, player):
    # print(f'The player is {player}')
    row_number = location[0]
    col_number = location[1]
    # print(f'They want to move to row {row_number}')
    # print(f'They want to move to column {col_number}')
    board[row_number][col_number] = player
    # print(board)
    print_board(board)
    return board

    pass

game_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
player = 'O'
loc = (0, 0)
game_board = move(game_board, loc, player)


player = 'X'
loc = (0, 1)
game_board = move(game_board, loc, player)