
def printBoard(board):
    i = 0
    for row in board:
        i += 1
        print(' | '.join(row))
        if i < 3:
            print("-" * 9)
def makeMove(board, col, row, player):
    if col < 0 or col > 2 or row < 0 or row > 2:
        return False
    
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def checkWin(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return False

def checkDraw(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        printBoard(board)
        row = int(input(f'Player {current_player} choose your col: '))
        col = int(input(f'Player {current_player} choose your row: '))
        if makeMove(board, row, col, current_player):
            if checkWin(board):
                print(f"{current_player} Wins!")
                break
            if checkDraw(board):
                print("The game is a Draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move. Please try again!')
        
        


if __name__ == '__main__':
    main()
