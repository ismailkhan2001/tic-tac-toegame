import random
def print_board(board,rows,cols):
    print("-"*(6*3))
    for i in range(rows):
        for j in range(cols):
            print(" ",board[i][j],end=" | ") if j==1 or j==2 else print("| ",board[i][j],end=" | ")
        print("\n" + "-" * (6*3))

def check_winner(board,rows,cols,player):
    for i in range(rows):
        if all(board[i][j]==player for j in range(cols)):
            return True
    for j in range(cols):
        if all(board[i][j]==player for i in range(rows)):
            return True
    if all(board[i][i]==player for i in range(min(rows,cols))):
        return True
    if all(board[i][cols-1-i]==player for i in range(min(rows,cols))):
        return True
    return False

def is_board_full(board,rows,cols):
        if all(board[i][j]!=" " for i in range(rows) for j in range(rows)):
            return True
        else:
            return False
        

            
def player_move(board,rows,cols):
    while True:
        try:
            row,col=map(int,input(f"enter the row from(0-{rows-1},columns from(0-{cols-1}):").split(" "))
            if row<0 or col<0 or row>=rows or col>=cols:
                print("invalid input,please enter value from 0-2")
                continue
            if(board[row][col]!=" "):
                print("this spot is already taken,please take another position")
                continue
            return row,col
        except ValueError:
            print("invalid input,please enter the above numbers")

def computer_move(board,rows,cols):
    while True:
        row,col=random.randint(0,rows-1),random.randint(0,cols-1)
        if board[row][col]==" ":
            return row,col

def play_game(rows,cols):
    board=[[" " for _ in range(rows)] for _ in range(cols)]
    current_player="X"
    while True:
        print_board(board,rows,cols)
        if current_player=="X":
            print(f"Player {current_player} turn")
            row,col=player_move(board,rows,cols)
        else:
            print(f"Plater {current_player} turn")
            row,col=computer_move(board,rows,cols)

        board[row][col]=current_player

        if check_winner(board,rows,cols,current_player):
            print_board(board,rows,cols)
            if current_player=="x":
                print(f"{current_player} wins")
            else:
                print(f"{current_player} wins")
        

        if is_board_full(board,rows,cols):
            print_board(board,rows,cols)
            print("match is tie")
            break
        current_player="O" if current_player=="X" else "X"

rows=3
cols=3
play_game(rows,cols)