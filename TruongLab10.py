# Tic tac toe!
def print_board(board):
    #print the board and the X's and O's
    for r in board:
        for c in r:
            if c == 0:
                print(". ", end="")
            elif c == 1:
                print("X ", end="")
            elif c == 2:
                print("O ", end="")
            else:
                print(c, end="")
        print()

def is_valid(r, c, board):
    #make sure the row and column are valid
    if (r >= 0 and r <= 2) and (c >= 0 and c <= 2):
        r += 1
        c += 1
        if board[r][c] == 0:
            return True
    return False

def is_winner(board):
    #check if someone has won
    if (board[1][1] == board[1][2] == board[1][3] == 1) or (board[2][1] == board[2][2] == board[2][3] == 1) or (board[3][1] == board[3][2] == board[3][3] == 1):
        return True
    elif (board[1][1] == board[2][1] == board[3][1] == 1) or (board[1][2] == board[2][2] == board[3][2] == 1) or (board[1][3] == board[2][3] == board[3][3] == 1):
        return True
    elif (board[1][1] == board[2][2] == board[3][3] == 1) or (board[1][3] == board[2][2] == board[3][1] == 1):
        return True
    elif (board[1][1] == board[1][2] == board[1][3] == 2) or (board[2][1] == board[2][2] == board[2][3] == 2) or (board[3][1] == board[3][2] == board[3][3] == 2):
        return True
    elif (board[1][1] == board[2][1] == board[3][1] == 2) or (board[1][2] == board[2][2] == board[3][2] == 2) or (board[1][3] == board[2][3] == board[3][3] == 2):
        return True
    elif (board[1][1] == board[2][2] == board[3][3] == 2) or (board[1][3] == board[2][2] == board[3][1] == 2):
        return True
    else:
        return False

def main():
    #establish the board
    board = [['- ', '0 ', '1 ', '2 '], ['0 ', 0, 0, 0], ['1 ', 0, 0, 0], ['2 ', 0, 0, 0]]
    current = 1
    #start the game
    for i in range(9):
        print_board(board)
        x = is_winner(board)
        if x == True:
            print('Winner!')
            break
        if current == 1:
            print("X's turn")
        else:
            print("O's turn")
        r = int(input("Give Row!"))
        c = int(input("Give Column!"))
        while not is_valid(r, c, board):
            r = int(input("Give Row!"))
            c = int(input("Give Column!"))

        r += 1
        c += 1

        #switch players
        board[r][c] = current
        if current == 1:
            current = 2
        else:
            current = 1
    #winner or tie game
    if x == False:
        print('Tie game')
    elif current == 1:
        print('O wins!')
    elif current == 2:
        print('X wins!')


main()