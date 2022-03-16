player=1
coins=70
def display_state():
     global coins 
     print ("enter coins =", coins)

def get_input(players):
     global coins 
     print (player , "player please enter coins (1,4,9,16): \n")
     move= int (input())
     if move ==1 or move == 4 or move == 9 or move == 16 or move == 25 or move == 36 or move ==49:
          coins ==coins - move 
          return move 

     else :
          print ("you have to enter 0 - squere number ")

def is_loser ():
          global coins 
          if coins < 1 :
               return True 
def play_game ():
     display_state ()
     while True :
          get_input("FIRST")
          display_state()
          if is_loser():
              print ("first player win ")    
              break

          get_input("secound") 
          display_state()
          if (is_loser()):
               print ("secound player win")
               break
if player ==1 :
     player =2
else :
     player=1
     