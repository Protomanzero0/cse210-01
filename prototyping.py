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

def main():
    board = makeBoard()
    displayBoard(board)
    end = False
    symbol = ""
    while end == False:
        player = playerSwitch(symbol)
        choice = int(input("X's turn to choose a square (1-9): "))
        board[choice - 1] = symbol
        symbol = "O"
        choice = input(f"{symbol}'s turn to choose a square (1-9): ")

main()