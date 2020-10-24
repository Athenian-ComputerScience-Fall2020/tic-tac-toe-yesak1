# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Megan 
# help for ties on https://dev.to/jamesshah/the-classic-tictactoe-game-in-python-cpi
# A note on style: Dictionaries can be defined before or after functions.

gb = {'TL': ' ', 'ML': ' ', 'BL': ' ', 'TM': ' ', 'MM': ' ', 'BM': ' ', 'TR': ' ', 'MR': ' ', 'BR': ' '}

def ttt(gb):
    print ((gb["TL"]) + '|' + (gb["TM"]) + '|' + (gb["TR"]))
    print ('-+-+-')
    print ((gb["ML"]) + '|' + (gb["MM"]) + '|' + (gb["MR"]))
    print ('-+-+-')
    print ((gb['BL']) + '|' + (gb["BM"]) + '|' + (gb["BR"]))
    #winnercheck(gb)
    
    
        

    
        
    
    
def player1():
    print("player 1 is X. Player 2 is O")
    player1=input('Player 1, choose your spot to place X (TL, ML, BL, TM, MM, BM, TR, MR, BR ) ')
    if gb["TL"] =='X' and gb["TM"] == 'X' and gb["TR"]=='X':
        print('winner')
    elif gb["ML"]=='X' and gb["MM"]=='X' and gb["MR"]=="X":
        print("player 1 is the winner!")
    else:
        gb[player1]="X"
        ttt(gb)
        player2() 
    if gb[player1]!=" ":
        print ("space already filled, skip your turn")
        ttt(gb)
        player2()  
    else:
        gb[player1]="X"
        ttt(gb)
        player2()   
    
    

def player2():
    print("Player 2, it's your turn!")
    player2=input('Player 2, choose your spot to place O, but keep in mind that you must choose a different space than the last one. (TL, ML, BL, TM, MM, BM, TR, MR, BR ) ')
    
    
    if gb[player2]!=" ":
        print ("space already filled, skip your turn")
        ttt(gb) 
        player1()
    
   
    else: 
        gb[player2]="O"
        ttt(gb)
        player1()

    
    
    

'''def winnercheck(gb):
    if gb["TL"] == gb["TM"] == gb["TR"]:
        if gb["TM"] == "X":
            print("player 1 is the winner!")
                
    elif gb["TL"]==gb["TM"]==gb["TR"]:
        if ["TM"] == "O":
            print("player 2 is the winner!")
            

    elif gb["ML"]==gb["MM"]==gb["MR"]:
        if gb["MM"] == "X":
            print("player 1 is the winner!")
                

    elif gb["ML"]==gb["MM"]==gb["MR"]:
        if gb["MM"] == "O":
            print("player 2 is the winner!")
                

    elif gb["BL"]==gb["BM"]==gb["BR"]:
        if gb["BM"] == "X":
            print("player 1 is the winner!")
                

    elif gb["BL"]==gb["BM"]==gb["BR"]:
        if gb["BM"] == "O":
            print("player 2 is the winner!")
                
        
            #vertical winners:
    elif gb["TR"]==gb["MR"]==gb["BR"]:
        if gb["MR"] == "X":
            print("player 1 is the winner!")
                
    elif gb["TR"]==gb["MR"]==gb["BR"]:
        if gb["MR"] == "O":
            print("player 2 is the winner!")
                

    elif gb["TM"]==gb["MM"]==gb["BM"]:
        if gb["MM"] == "X":
            print("player 1 is the winner!")
                
    elif gb["TM"]==gb["MM"]==gb["BM"]:
        if gb["MM"] == "O":
            print("player 2 is the winner!")
                

    elif gb["TL"]==gb["ML"]==gb["BL"]:
        if gb["ML"] == "X":
            print("player 1 is the winner!")
                
    elif gb["TL"]==gb["ML"]==gb["BL"]:
        if gb["ML"] == "O":
            print("player 2 is the winner!")
                

            #diagonal winners:

    elif gb["TL"]==gb["MM"]==gb["BR"]:
        if gb["MM"] == "X":
            print("player 1 is the winner!")
                
    elif gb["TL"]==gb["MM"]==gb["BR"]:
        if gb["MM"] == "X":
            print("player 1 is the winner!")
    elif gb["TR"]==gb["MM"]==gb["BL"]:
        if gb["MM"] == "O":
            print("player 2 is the winner!")
                
    elif gb["TR"]==gb["MM"]==gb["BL"]:
        if gb["MM"] == "X":
            print("player 1 is the winner!")'''

    #tie
  #if 'TL'!='  ' and 'ML'!='  ' and 'BL' !='  ' and 'TM' != '  ' and 'MM' != '  ' and 'BM' != '  ' and 'TR' != '  ' and 'MR' != '  ' and 'BR' != '  ':
       # print("game over. Tie.")

    
                
    



    
    

    
        
        

ttt(gb)
player1()


