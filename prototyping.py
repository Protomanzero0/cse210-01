def makeBoard():
    board = []
    for number in range(9):
        board.append(number + 1)
    # print(board)
    return board

def displayBoard(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def playerSwitch(symbol):
    if symbol == "" or symbol == "O":
        return "X"
    else:
        return "O"

def winCondition(board):
    if (
    board[0] == board[1] == board[2] or
    board[3] == board[4] == board[5] or
    board[6] == board[7] == board[8] or
    board[0] == board[3] == board[6] or 
    board[1] == board[4] == board[7] or
    board[2] == board[5] == board[8] or
    board[0] == board[4] == board[8] or 
    board[2] == board[4] == board[6]):
        return True
    else:
        return False

def drawCondition(turns):
    if turns >= 9:
        return True
    else:
        return False

def main():
    board = makeBoard()
    displayBoard(board)
    endGame = False
    turns = 0
    symbol = ""
    player = playerSwitch(symbol)
    endGameDraw = False
    while endGame == False and endGameDraw == False:
        print()
        choice = int(input(f"{player}'s turn to choose a square (1-9): "))
        print()
        if board[choice - 1] != "X" and board[choice - 1] != "O": 
            board[choice - 1] = player
            displayBoard(board)
            turns += 1
            endGame = winCondition(board)
            endGameDraw = drawCondition(turns)
            if endGame == False:
                player = playerSwitch(player)
        else:
            print("That square is taken! Please try again.")
    if endGame == True:
        print(f"{player} wins! Good game!")
    elif endGameDraw == True:
        print("It's a draw! Good game!")
    else:
        print("Lol wut")

main()