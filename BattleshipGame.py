"""
  Battleship game which is two player.
  Player 1 decides on the placement of the battleship
  Player 2 gets 10 tries to guess the correct placement of the battleship
"""
from random import randint#imports the randint function for the one player game to get the computer to select the position
import time #allows us to use the sleep function to pause
import os#allows for clearing the screen to keep it tidy

board = []#initialises an empty array

for i in range(5):#fills the board with O for each space
  board.append(["O"] * 5)#produces a 2D array with 5 rows, 5 columns

def print_board(board):# prints the board joining each element with a space
  for row in board:
    print (" ".join(row))
def random_row(board):#determines the row that the battleship will be on
  return randint(0, len(board) - 1)

def random_col(board):#determines the column the batteship will be in
  return randint(0, len(board[0]) - 1)


#main start to game
print("Welcome to Battleships")
selection = int(input("1 or 2 player game? "))#deals with selecting either a 2 player game or a 1 player game
if selection == 2:
  player1 = input("Player 1 name: ")#asks the players name
  player2 = input("player 2 name: ")
  print (player1+". Time to select the placement of the battleship")#the player selects the position
  time.sleep(2)
  print_board(board)
  ship_row = int(input("Enter the row number"))-1#the user selects the position of the row of the battleship
  ship_col = int(input("Enter the column number"))-1#the user selects the position of the row of the battleship
elif selection ==1:
  player2 = input("Player name: ")
  ship_row = random_row(board)#calls the function to get the row
  ship_col = random_col(board)#calls the function to get the column
else:
  print ("incorrect number of players")
  
#print_board(board)#displays the board to the screen

print (ship_row+1)#shows us the row it is on - for testing
print (ship_col+1)#shows us the column it is in - for testing

play=True #sets the play to true to begin the game
tries = 0 #sets the number of tries to 0
while tries <=10 and play==True:#will only play the game if both play is true and tries is equal or lower than 10
    print_board(board)#prints the updated state of the board where guesses have taken place.
    print(player2+" make a guess...")
    guess_row = int(input("Guess Row: "))-1#allows the user to select the row, minus one to link to array
    guess_col = int(input("Guess Col: "))-1#allows the user to select the column, minus one to link to array

    if guess_row == ship_row and guess_col == ship_col:#if both combinations match then the user wins
      print ("Congratulations! You sunk my battleship!")
      print("It took you "+str(tries+1)+" tries to guess the position.")# shows the user the number of tries they had
      time.sleep(2)#pause before clearing the screen to show the final grid
      play=False#as the user has won set the play to false to exit the game
    else:#checks the lost condition, invalid options outside the grid or if already guessed
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):#these values mean they are out of range of the array
        print ("I think you selected the land not the sea!")
      elif(board[guess_row][guess_col] == "X"):#if aleady guessed the current position
        print ("You guessed that one already.")
      else:
        print ("You missed my battleship!")
        tries+=1#increases the tries by 1 
        board[guess_row][guess_col] = "X" #puts an X to show where the guess was
        if tries ==10:#checks if the tries is 10 to display the final message before ending the game
            print("Better luck next time!")
    os.system('cls') 
        
print("The final board")
board[ship_row][ship_col] = "B"#shows the user where the battleship was
print_board(board)#prints the final state of the board .
input("Press any key to finish...")
