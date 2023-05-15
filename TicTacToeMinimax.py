board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = 'O'
bot = 'X'


def print_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}\n{board[4]} | {board[5]} | {board[6]}"
          f"\n{board[7]} | {board[8]} | {board[9]}")


def is_space_free(position):
    if board[position] == ' ':
        return True
    return False


def insert_move(position, letter):
    if is_space_free(position):
        board[position] = letter
        print_board(board)
        if check_win():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        if check_draw():
            print("Draw!")
            exit()
        return
    else:
        position = int(input("Please enter a valid position: "))
        insert_move(position)
        return


def check_win():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    else:
        return False


def player_move():
    position = int(input("Enter a position for 'O': "))
    insert_move(position, player)
    return


def computer_move():
    position = int(input("Enter a position for 'X': "))
    insert_move(position, bot)
    return


def check_draw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


while not check_win():
    player_move()
    computer_move()
