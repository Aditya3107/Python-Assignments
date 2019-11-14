#tic tac toe 
#board


######global variable######
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
#display board

game_still_going = True

#who is winner

winner = None

#whos turn is it ?

current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    
#play game

def play_game():
    #display initial board
    display_board()
    
    while game_still_going:
        handle_turn(current_player)
        
        #check the game is over 
        check_if_game_over()
        
        #flip to other player
        flip_player()
    
    #game is ended 
    if winner == "X" or winner == "O":
        print(winner +"won.")
    elif winner == None:
        print("its a tie")
    
    
    
#handle a single turn of a arbitary player  
def handle_turn(player):
    
    
    print(player + "'s turn")
    
    position = input("choose a number between 1 to 9")
    
    valid = False
    while not valid :
    
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("invalid, choose from 1 to 9")
        position = int(position)- 1
        
        if board[position] == "-":
            valid = True
            print("already taken place choose different")
        
    board[position] = player
    display_board()
    
def check_if_game_over():
    check_if_win()
    check_if_tie()
 
def check_if_win():
    
    #setup a global variable
    global winner
    #check rows
    row_winner = check_rows()
    
    #check columns
    column_winner = check_columns()
    
    #diagonals
    
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    
    else :
        winner = None
    return

def check_rows():
    
    #set a global variables
    global game_still_going
    #check any row has a same value 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-" 
    
    if row_1 or row_2 or row_3 :
        game_still_going = False
    
    #return the winner X or O
    if row_1:
        return board[0]
    if row_2 :
        return board[3]
    if row_3 :
        return board[6]
    
    return
def check_columns():
    #set a global variables
    global game_still_going
    #check any column has a same value 
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-" 
    
    if column_1 or column_2 or column_3 :
        game_still_going = False
    
    #return the winner X or O
    if column_1:
        return board[0]
    if column_2 :
        return board[1]
    if column_3 :
        return board[2]
    

    return


def check_diagonals():
    
    #set a global variables
    global game_still_going
    #check any diagonal has a same value 
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
     
    
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    
    #return the winner X or O
    if diagonal_1:
        return board[0]
    if diagonal_2 :
        return board[1]
    
    return


def check_if_tie():
    
    global game_still_going
    
    if "-" not in board:
        game_still_going = False
    return
    

def flip_player():
    
    global current_player 
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
        

    
play_game()
    

