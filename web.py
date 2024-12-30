# Libraries to import (if any)
import random

'''

# Game menu function which will be revoked during the game 

'''
def game_menu():                        
    print('''
    1) Start a Game
    2) Print the Board
    3) Place a Stone
    4) Reset the game
    5) Exit the game''')

# 
# game_menu()
size = 9

# Board

'''
Function creates a lists of lists and it takes size as a parameter

'''
def create_board(size):
    # Creating a list of list with size and " " with a space charachter
    board = [[' ' for _ in range(size)] for _ in range(size)]   
    return board

# Storing the board in variable 'board'
board = create_board(size) 

'''
Function checks if the position on board is occupied or not and takes board and position that needs to be checked  as a parameter 

'''
def is_occupied(board, position):
    # Defining parameter position is made of two values
    row_value, colum_value = position
    # Converting row value to integer
    row_value = int(row_value)                                    
    
    # Calculating the integer value of column Index
    
    colum_value = (ord(colum_value.upper()) - ord('A'))
    if board[row_value][colum_value] != " " : 
        # Returns True if position in board is occupied
        return True                                                
    else:
        # Returns False if postion is unoccupied
        return False                                               

'''
Function places a stone on board and takes board , color of stone or stone and position
 as a input parameter

'''
def place_on_board(board, stone, position):
    # Defining parameter position is made of two value
    row_value, colum_value = position 
    # Converting row value to integer
    row_value = int(row_value)                             
    
    #Calculate the integer value of column Index
    
    colum_value = (ord(colum_value.upper()) - ord('A'))
    
    if board[row_value][colum_value] == ' ' :             # Checks if target position only has a space character
        board[row_value][colum_value] = stone             # Places the value of stone on that board postion
        return True                                       # Returns True if Move was successful
    else:
        return False                                      # Return False if move was unsuccessfull

'''
The function prints the current state of board and takes the parameter as board, the one which is created above
'''
def print_board(board):                       
    for row in board:
        print('|'.join(row))                   # Adding '|' in every row element  
        print('-' * (len(board)*2 - 1))        # Adding '--' between the space of two rows
board = create_board(size)                     # Assigns the printed board to a variable which can be called in other functions


'''
The function returns all the available moves on the board and takes board as a parameter

'''



def check_available_moves(board):
    moves = []                        # Creats a empty list to store all available values                                        
    
    for row in range(len(board)):
        for colum in range(len(board[0])):
            if board[row][colum] == " ":
                moves.append(f"{row}{chr(colum + 65)}")
       
        #for x in range(len(moves)):
    #         print(moves[x])
    return moves




'''
The function checks for 5 stone in a line, horizontally / vertically and Diagonally by taking board as a parameter
'''

def check_for_winner(board):
    
    if check_available_moves(board) != 0:                  #Checks if available moves are not 0
        
        # Checks the win horizontally
  
        for colum in range(size-4):
            for row in range(size):
                if board[row][colum] == "●" and board[row][colum + 1] == "●" and board[row][colum + 2] == "●" and board[row][colum + 3] == "●" and board[row][colum + 4] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row][colum + 1] == "o" and board[row][colum + 2] == "o" and board[row][colum + 3] == "o" and board[row][colum + 4] == "o":
                    return "o"
                
        # Checks the win Vertically
        
        for colum in range(size):
            for row in range(size-4):
                if board[row][colum] == "●" and board[row + 1][colum] == "●" and board[row + 2][colum] == "●" and board[row + 3][colum] == "●" and board[row + 4][colum] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row + 1][colum] == "o" and board[row + 2][colum] == "o" and board[row + 3][colum] == "o" and board[row + 4][colum] == "o":
                    return "o"
                
        # Checks the Win Diagonally
        #negetive slope
        
        for colum in range(size-4):
            for row in range(size-4):
                if board[row][colum] == "●" and board[row + 1][colum + 1] == "●" and board[row + 2][colum + 2] == "●" and board[row + 3][colum + 3] == "●" and board[row + 4][colum + 4] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row + 1][colum + 1] == "o" and board[row + 2][colum + 2] == "o" and board[row + 3][colum + 3] == "o" and board[row + 4][colum + 4] == "o":
                    return "o"

        #positive slope
        
        for row in range(size-4):
            for colum in range(size-4):
                if board[row][colum] == "●" and board[row - 1][colum + 1] == "●" and board[row - 2][colum + 2] == "●" and board[row - 3][colum + 3] == "●" and board[row - 4][colum + 4] == "●":
                    return "●"
                elif board[row][colum] == "o" and board[row - 1][colum + 1] == "o" and board[row - 2][colum + 2] == "o" and board[row - 3][colum + 3] == "o" and board[row - 4][colum + 4] == "o":
                    return "o"
                
                
    elif check_available_moves(board) == 0:             # Checks if no moves available and result is Draw
        return "Draw"
    
    else:
        return "None"

'''
This function creates a computer player which can play with a player in main game and takes board and the respective player move as parameters
'''
def random_computer_player(board, player_move):
    comp_moves =[]                                                            # Creating a Empty list
    
    
    for r in [-1,0,1]:                                                        # Creates a 3 x 3 Matrix
        for c in [-1,0,1]:
            if r == 0 and c == 0:                                             # Takes care of boundary conditions
                continue
            
            row = int(player_move[0]) + r
            colum = (ord(player_move[1].upper()) - 65) + c                   # Changes row and colum into integer and checks all the values in 3 x 3 matrix
            
            if 0<= row < size and 0<= colum < size and [row,colum] != " ":
                colum = chr(65 + colum)
                
                comp_moves.append((str(row), str(colum)))                   # Adds all the possible possible positions in string
             
    
#     print(comp_moves)
    if len(comp_moves) != 0:                                               
        random_comp_move = random.choice(comp_moves)                        # Takes a random value from all possible moves
#         print(random_comp_move)
    else:
        random_comp_move = random.choice(check_available_moves(board))      # If no possible values in 3 x 3, takes a random value from available moves function
#         print("This is:", random_comp_move)
        
    return random_comp_move 
#     place_on_board(board, stone, random_computer_player())                 # Places that stone on board
    
    
#place_on_board(board, "o", random_computer_player(board, ))
                
    
'''
This functions calls all the function together and players can play the game
'''
# print_board(board)

# def undo_last_move(board, position):
#     row_value, colum_value = position
#     row_value = int(row_value)
#     #Calculate the integer value of column Index
#     colum_value = (ord(colum_value.upper()) - ord('A'))
#     board[row_value][colum_value] = " "
#     return board

# def call_menu():
#     dist = int(input())
#     if dist == 1:
#         play_game()
#     elif dist == 2:
#         undo_last_move(board, position)
#         continue
#     else: 
#         break


# This function brings all the function together and make user play the game
    
def play_game():
    print('''
    
                 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
                ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
                ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
                ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          
                ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
                ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
                ▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
                ▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
                ▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
                ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
                 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 

                                ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                                   
                               ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                                  
                                ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌                                                  
                                    ▐░▌     ▐░▌       ▐░▌                                                  
                                    ▐░▌     ▐░▌       ▐░▌                                                  
                                    ▐░▌     ▐░▌       ▐░▌                                                  
                                    ▐░▌     ▐░▌       ▐░▌                                                  
                                    ▐░▌     ▐░▌       ▐░▌                                                  
                                    ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌                                                  
                                    ▐░▌     ▐░░░░░░░░░░░▌                                                  
                                     ▀       ▀▀▀▀▀▀▀▀▀▀▀                                                   

                 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄         ▄                   
                ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░▌       ▐░▌                  
                ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░▌       ▐░▌                  
                ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌       ▐░▌                  
                ▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌░▌   ▐░▌       ▐░▌                  
                ▐░▌▐░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░░▌    ▐░▌       ▐░▌                  
                ▐░▌ ▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌░▌   ▐░▌       ▐░▌                  
                ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌       ▐░▌                  
                ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌                  
                ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌                  
                 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀    
    
    
    
    
                                            ''')
    
    #initiating infinite while loop
    
    while(True):
        
        game_menu()                                                           # Calling game menu function
        print(" Please select Option 1, then option 3")
        user_input = int(input())  
        if user_input == 1:                                                   # Option 1 in game menu function
#             global size 
            size = int(input("Please enter the Board Size, eg: 9,13,15: "))  # Takes size as in input
            player_mode = int(input(''' 
                                        Please select from below
                                        1) Press "1" for Player Vs Player Mode
                                        2) Press "2" for Player Vs Computer Mode
                                        
                                    '''))
            create_board(size)
            continue                                                            # Breaks the loops and user need to go to 2nd and 3rd option

        elif user_input == 2:                                                   # Option 2 in game menu function
            print_board(board)
            continue

        elif user_input == 3:                                                  # Option 3 in game menu function

                print('''
                                        "●: Black Will Start the Game"
                                        
                    ''')
                print("Position Should be in a format num , alphabet, for eg: 1, F")
    


                if player_mode == 1:                                             # Game mode Player vs Player 
                    print(''' 
                    
                                        This is Player Vs Player Mode
                                        
                                        
                    
                    ''')
                    num = 1        
                    while(True):                                                 # Infinte while loop
                        if num == 1:                                             # Player 1 begins
                            stone = "●"
                            print('''
                                        " ● : Following Moves are Valid"
                                        
                                 ''')
                            print(check_available_moves(board))                  # Prints available moves
                            place = tuple(input("Enter the position Value : "))  # Taking input for stone placement
                            a = place[0]                                         # Fetches cordinates different values from position
                            b = place[1]
                            
                            
                            
                            if a.isnumeric() == True and b.isalpha() == True:    # Checks if the entered value is num and alpha also it is between 0 and 8 and alpha is a possible value
                                if 0 <= int(a) <= 8 and b in ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i']:
        
                                
                                
                                    if (is_occupied(board, place)) == False:     # Checks the available position on board

                                        place_on_board(board, stone, place)      # Places the Black stone on board 


                                        if check_for_winner(board) == "●":       # Checks for winning condition
                                            print('''
                                            
                                                        " ● Won"
                                            
                                                                     ''')
                                            
                                            for i in range(len(board)):         # Resets the board
                                                for j in range(len(board)):
                                                    board[i][j] = " "
                                                    
                                            break


                                        elif check_for_winner(board) == "Draw":
                                            print("Draw")

                                        print_board(board)

                                        num = 2
                                        continue
                                    else:
                                        print('''

                                        "Position is already occupied, please select a new position from list"

                                            ''')
                                        num = 1
                                        continue
                                
                                else:
                                    print('''

                                        "Invalid input, row can be from 0-8 and column can be A - I"

                                    ''')
                            else:
                                print('''
                                
                                    "Invalid input, Please enter a input numeric and alphabet eg: 1F"
                                
                                ''')
                                

                        elif num == 2:                                                              # Player 2, "o" ' s turn'
                            stone = "o"
                            print('''
                                        " o : Following Moves are Valid"
                                        
                                ''')
                            print(check_available_moves(board))                                     # Checks available moves on board
                            place = tuple(input("Enter the position Value : "))                     # Takes a position input 
                            a = place[0]                                                            # Resolves the position into board coordinates
                            b = place[1]
                            
                            if a.isnumeric() == True and b.isalpha() == True:                       # Checks if the input is in correct format
                                if 0 <= int(a) <= 8 and b in ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i']:


                                    if (is_occupied(board, place)) == False:                        # If the position entered not occupied, place stone
                                        place_on_board(board, stone, place)                         # Places the stone on board

                                        if check_for_winner(board) == "o":                          # Checks for winner conditions
                                            print('''
                                                    
                                                    "o Won"
                                                    
                                                    ''')
                                            for i in range(len(board)):                              # Clears the board if someone wins
                                                for j in range(len(board)):
                                                    board[i][j] = " "
                                                    
                                            break
                                            
                                        elif check_for_winner(board) == "Draw":
                                            print("Game Draw")


                                        num = 1
                                        print_board(board)
                                    else:
                                        print('''

                                            "Position is already occupied, please select a new position from list"

                                            ''')
                                        num = 2
                                        continue


                                else:
                                    print('''

                                        "Invalid input, row can be from 0-8 and column can be A - I"

                                ''')
                            else:
                                print('''

                                    "Invalid input, Please enter a input numeric and alphabet eg: 1F"

                                     ''')

                
                elif player_mode == 2:                                              # Mode 2, Player vs Computer
                    print('''
                                            This is Player Vs Computer mode,
                                    First Turn will be of player and it will start with Black
                                    
                            ''')
                    num = 1        
                    while(True):                                                     # Infinite While loop
                        if num == 1:                                                 # PLyer 1 begins wth black
                            stone = "●"
                            print('''
                            
                                        " ●: Following Moves are Valid"
                                
                                ''')
                            print(check_available_moves(board))                     # Prints available moves to the player 
                            place = tuple(input("Enter the position Value : "))     # Takes input to place the stone
                            
                            a = place[0]                                            # Extracts coordinates from position
                            b = place[1]
                            
                            if a.isnumeric() == True and b.isalpha() == True:       # Checks if the input is in correct format
                                if 0 <= int(a) <= 8 and b in ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i']:
                                    if (is_occupied(board, place)) == False:        # Checks if the board position is avaialble
                                        
                                        place_on_board(board, stone, place)         # Places the stone
                                        
                                        if check_for_winner(board) == "●":          # Checks for winning conditions
                                            print('''

                                                "Congratulations, You Won"

                                                ''')
                                            for i in range(len(board)):             # Clears the board 
                                                for j in range(len(board)):
                                                    board[i][j] = " "
                                            break
                                            
                                        elif check_for_winner(board) == "Draw":
                                            print("Game Draw")
                                        print_board(board)

                                        num = 2
                                        continue
                                    else:
                                        print('''
                                        
                                            "Position is already occupied, please select a new position from list"
                                                
                                                ''')
                                        num = 1
                                        continue
                                else:
                                    print('''

                                    "Invalid input, row can be from 0-8 and column can be A - I"

                                ''')
                            else:
                                print('''
                                
                                    "Invalid input, Please enter a input numeric and alphabet eg: 1F"
                                    
                                        ''')

                        elif num == 2:                                        # Computer player starts
                            stone = "o"
                            place_on_board(board, stone, random_computer_player(board, place)) # PLaces a stone at the computer generated position
#                             print("This is place:", place)
                            if check_for_winner(board) == "o":               # Check for winning conditions
                                print("Computer Won")
                                
                                for i in range(len(board)):                    # Clears the board
                                    for j in range(len(board)):
                                        board[i][j] = " "
                                break
                            elif check_for_winner(board) == "Draw":
        
                                print("Game Draw")
                            print("Computer Move")
                            print_board(board)
                            num = 1
                            
                   
                            
#             break
            
        elif user_input == 4:                                              # Resets the game
            print('''
            
                "You have Reseted the Game"
                
                ''')
            for i in range(len(board)):
                for j in range(len(board)):
                    board[i][j] = " "
            
            
            
            
        elif user_input == 5:                                            # Exit the game
            
            print('''  
            
            
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄    ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄       ▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌  ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░▌ ▐░▌      ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌░▌        ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░▌         ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌
     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌░▌         ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌▐░▌            ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌      ▀ 
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░▌ ▐░▌           ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌      ▄ 
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌  ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌
      ▀       ▀         ▀  ▀         ▀  ▀        ▀▀  ▀    ▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀ 
            ''')
            break
                    

            

                    # Need to do error handling
                        
                        
                

play_game()          
                    
                    
                
            
    
    
    
    
        