board=["-","-","-",
       "-","-","-",
       "-","-","-",]
game_still_going=True
winner=None
current_player="X"
def display_board():
    print(board[0]+ "|"+board[1]+ "|"+board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():

    display_board()
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner=="x"or winner=="o":
        print(winner+ " won")
    elif winner==None:
        print("tie")

def handle_turn(player):
    print(player,"turn")
    valid=True
    while valid:

        while True:
            position = input("choose a position from one to 9")
            if position not in ["1","2","3","4","5","6","7","8","9"]:
                print("try again")
                continue
            else:
                break

        position=int(position)-1
        if board[position] =="-":
           valid=False
        else:
            print("go again")


    if player=="X":
        board[position]="x"
    else:
        board[position]="o"
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner=check_rows()
    column_winner=check_column()
    diagonal_winner=check_diag()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner
    return
def check_rows():
    global game_still_going
    row1= board[0]==board[1]==board[2]!="-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3 :
        game_still_going=False

    if row1:
        return board[0]
    elif row2:
        return board[5]
    elif row3:
        return board[6]
    return
def check_column():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_still_going = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return
def check_diag():
    global game_still_going
    dig1= board[0] == board[4] == board[8] != "-"
    dig2 = board[2] == board[4] == board[6] != "-"
    if dig1 or dig2:
        game_still_going = False

    if dig1:
        return board[0]
    elif dig2:
        return board[4]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False

    return
def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"
    return
play_game()



