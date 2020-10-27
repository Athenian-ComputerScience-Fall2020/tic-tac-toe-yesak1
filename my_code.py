# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Megan helped
#help with quit() https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
# A note on style: Dictionaries can be defined before or after functions.

gb = {'TL': ' ', 'ML': ' ', 'BL': ' ', 'TM': ' ', 'MM': ' ', 'BM': ' ', 'TR': ' ', 'MR': ' ', 'BR': ' '} #dictionary with all space names

def ttt(gb):
    print("\n")
    print ((gb["TL"]) + '|' + (gb["TM"]) + '|' + (gb["TR"]))
    print ('-+-+-')
    print ((gb["ML"]) + '|' + (gb["MM"]) + '|' + (gb["MR"]))#this function creates the board and assigns values.
    print ('-+-+-')
    print ((gb['BL']) + '|' + (gb["BM"]) + '|' + (gb["BR"]))
    print("\n")
    winnercheck(gb)
    tie(gb)
    
    
        

    
        
    
    
def player1():

    print("player 1 is X. Player 2 is O")
    player1=input('Player 1, choose your spot to place X \n (TL, ML, BL, TM, MM, BM, TR, MR, BR ) ')
    
    
    if player1!='TL' and player1!='ML' and player1!='BL' and player1!='TM' and player1!='MM' and player1!='BM' and player1!='TR' and player1!='MR' and player1!='BR':
        print("invalid input, skip your turn")
        ttt(gb)
        player2()
    
    if gb[player1]!=" ":
        print ("space already filled, skip your turn")
        ttt(gb) #if theres already a space taken, it's invalid
        player2()
    
   
    else: 
        gb[player1]="X"
        ttt(gb) #if the input is correct, the game continues
        player2()
     
    
    

   
    
    

def player2():
    print("Player 2, it's your turn!")
    player2=input('Player 2, choose your spot to place O, but keep in mind that you must choose a different space than the last one. \n (TL, ML, BL, TM, MM, BM, TR, MR, BR ) ')
    
    if player2!='TL' and player2!='ML' and player2!='BL' and player2!='TM' and player2!='MM' and player2!='BM' and player2!='TR' and player2!='MR' and player2!='BR':
        print("invalid input, skip your turn")
        ttt(gb)
        player1()
    
    if gb[player2]!=" ":
        print ("space already filled, skip your turn")
        ttt(gb) #if theres already a space taken, it's invalid
        player1()
    
   
    else: 
        gb[player2]="O"
        ttt(gb) #if the input is correct, the game continues
        player1()


    
    
#this function checks the winners
def winnercheck(gb):
    import sys
    if gb["TL"] == gb["TM"] == gb["TR"]:
        if gb["TM"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!") 
            quit()
                
    if gb["TL"]==gb["TM"]==gb["TR"]:
        if ["TM"] == "O":#if 3 x's or o's are in a row, the game ends.
            print("player 2 is the winner!")
            quit()

            

    if gb["ML"]==gb["MM"]==gb["MR"]:
        if gb["MM"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()
                

    if gb["ML"]==gb["MM"]==gb["MR"]:
        if gb["MM"] == "O":#if 3 x's or o's are in a row, the game ends.
            print("player 2 is the winner!")
            quit()
                

    if gb["BL"]==gb["BM"]==gb["BR"]:
        if gb["BM"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()

    if gb["BL"]==gb["BM"]==gb["BR"]:
        if gb["BM"] == "O":#if 3 x's or o's are in a row, the game ends.
            print("player 2 is the winner!")
            quit()
                
        
            #vertical winners:
    if gb["TR"]==gb["MR"]==gb["BR"]:
        if gb["MR"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()
                
    if gb["TR"]==gb["MR"]==gb["BR"]:
        if gb["MR"] == "O":#if 3 x's or o's are in a row, the game ends.
            print("player 2 is the winner!")
            quit()    

    if gb["TM"]==gb["MM"]==gb["BM"]:
        if gb["MM"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()
                
    if gb["TM"]==gb["MM"]==gb["BM"]:
        if gb["MM"] == "O":#if 3 x's or o's are in a row, the game ends.
            print("player 2 is the winner!")
            quit()
                

    if gb["TL"]==gb["ML"]==gb["BL"]:
        if gb["ML"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()
                
    if gb["TL"]==gb["ML"]==gb["BL"]:
        if gb["ML"] == "O":#if 3 x's or o's are in a row, the game ends.
            print("player 2 is the winner!")
            quit()
                

            #diagonal winners:
    if gb["TL"]==gb["MM"]==gb["BR"]:
        if gb["MM"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()
                
    if gb["TL"]==gb["MM"]==gb["BR"]:
        if gb["MM"] == "X":#if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()
    if gb["TR"]==gb["MM"]==gb["BL"]:
        if gb["MM"] == "O": #if 3 x's or o's are in a row, the game ends.
            print("player 2 is the winner!")
            quit()
                
    if gb["TR"]==gb["MM"]==gb["BL"]:
        if gb["MM"] == "X": #if 3 x's or o's are in a row, the game ends.
            print("player 1 is the winner!")
            quit()

    # if a tie occurs, the game stops 
def tie(gb):
    import sys
    if gb['TL']!=' ' and gb['ML']!=' ' and gb['BL'] !=' ' and gb['TM'] != ' ' and gb['MM'] != ' ' and gb['BM']!= ' ' and gb['TR'] != ' ' and gb['MR'] != ' ' and gb['BR'] != ' ':
        print("game over. Tie.")
        quit()

    
                
    



    
    

    
        
        

ttt(gb)
player1()


