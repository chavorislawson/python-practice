'''
Created on Jan 27, 2020

@author: clawson
'''
import random

#TicTacToe game using Python
#Summary of steps needed
#1. Create board. 
#2. Display the board
#3. Player chooses 'X' or 'O' and computer chooses opposite / two ways to play: random generated comp or play vs self
#4. Decide who goes first
#5. Whoever goes first inputs their character
#6. Whoever is next inputs their character
#7. Repeat.
#8. Winner is decided if a there are three characters in a row. The one who doesn't is the loser
#9. If there is no winner when all spaces of the board are, then a tie is drawn.
#10. Ask to play again



#class TicTacToe

board = [['','',''],['','',''],['','','']]

#createBoard method creates a 3x3 sized board
#board should look like
'''
 ___ ___ ___
 
| 1 | 2 | 3 |
 ___ ___ ___
 
| 4 | 5 | 6 |
 ___ ___ ___
 
| 7 | 8 | 9 |
 ___ ___ ___
 
 '''
 
#Right now I'm just focusing on getting the numbers in the list and displaying that.
def createBoard():
    value = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j]= str(value+1)
            
            
#displayBoard method displays the board
def displayBoard():
    print(" ___ ___ ___")
    print()
    for i in range(len(board)):             #basically a for loop in java to get the numbers I want.
        for j in range(len(board[i])):
            print("| "+board[i][j],end=" ") #what does end mean? is seems that this is how you do println though.
        print("|")
        print(" ___ ___ ___\n")
            
            
def play():
    pOne = input("Enter a number between 1 and 10 to decide who goes first: ")
    pTwo = input("Enter a number between 1 and 10 to decide who goes first: ")
    print(pOne)
    #winningNum = random.randint
    winningNum = 1
    if int(pOne) == winningNum:
        print("Player one goes first!")
    elif int(pTwo) == winningNum:
        print("Player two goes first!")
    
    
    createBoard()
    displayBoard()
#    while(not checkWinner()):
    place= input("Enter a number to place make your first move!")
    loc =board.index(int(place))
    type(loc)
    print(loc)


def checkWinner():
    return True;
    
        
def main():
    play()
    print("success")
    
    

if __name__ == "__main__":
    main()