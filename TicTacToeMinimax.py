board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def print_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}\n{board[4]} | {board[5]} | {board[6]}"
          f"\n{board[7]} | {board[8]} | {board[9]}")


def is_space_free(position):
    if board[position] == ' ':
        return True
    return False


