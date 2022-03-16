import random
#set player to 1
player=1
#set the inital state 
coins=random.randint(0,100)
print("the number of object is now",coins)
flag=1
while True :
    #get valid move 
    print ("player",player)
    move=int(input("what is your move? "))
    while flag==1:
        while move==coins:
            print("Please enter number less than ",coins)
            move=int(input())
        break
    if flag==1:
        flag=0
        old_move=move
    while old_move*2<=move:
        print("Please enter move less than or equal ",old_move*2)
        move=int(input())
    if move <= coins  :
        coins=coins-move
    else:
        print("incorrect move")
    #update  the state 
    print ("the number of coins is now",coins)
    old_move=move
     #check win state - win , lose , stalemate
    if coins==0:
       print ("player",player,"wins")
       break
    #switch players 2->1 , 1->2 go back to the valid move line 
    if  player ==1:
      player =2
    else:
     player=1

print ("game is over")