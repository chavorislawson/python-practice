'''
Created on Jan 27, 2020

@author: clawson
'''
#TicTacToe game using Python
#Summary of steps needed
#1. Create board. 
#2. Display the board
#3. Player chooses 'X' or 'O' and computer chooses opposite
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
    for i in board:
        for j in i:
            board[i][j]= 'a'
    

#displayBoard method displays the board
def displayBoard():
    for i in board:
        for j in i:
            print(board[i][j])
            
            
def main():
    createBoard()
    displayBoard()
    

if __name__ == "__main__":
    main()