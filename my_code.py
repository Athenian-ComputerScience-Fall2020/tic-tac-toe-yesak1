# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Megan 
# A note on style: Dictionaries can be defined before or after functions.

gb = {'TL': ' ', 'ML': ' ', 'BL': ' ', 'TM': ' ', 'MM': ' ', 'BM': ' ', 'TR': ' ', 'MR': ' ', 'BR': ' '}

def ttt(gb):
    print ((gb["TL"]) + '|' + (gb["TM"]) + '|' + (gb["TR"]))
    print ('-+-+-')
    print ((gb["ML"]) + '|' + (gb["MM"]) + '|' + (gb["MR"]))
    print ('-+-+-')
    print ((gb['BL']) + '|' + (gb["BM"]) + '|' + (gb["BR"]))
    player1()
    
    
def player1(): 
    print("player 1 is X. Player 2 is O")
    player1=input('Player 1, choose your spot to place X (TL, ML, BL, TM, MM, BM, TR, MR, BR ) ')
    gb[player1]=="X"
    ttt(gb)    
    

    

    
        
        

ttt(gb)



