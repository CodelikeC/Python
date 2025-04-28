#slicing : create a substring by extracting elements from another string indexing[] or slice 
#[start : stop : step]
# hieu index la duoc, giong het C++

#tic tac toe // 
import numpy as np 
import cmath   
print ("The tic tac toe game")
print ("------The official game-------")

def players (players_1, players_2): 
    print ("we have two players in the game!")
    print ("You have to choose player 1 or player 2 ? ")
numbers_player_1 = int(input(1))
numbers_player_2 = int(input(2))
if numbers_player_1 < 0 : 
    print ("error, please try again.")
elif numbers_player_1 > 0 | numbers_player_2 > 0  : 
    print ("Continue to the game ")
else : 
    print ("Error. Try again")
return players_in_the_game
players_in_the_game = players(players_1, players_2)


def game (a, b, c ) : 
    print ("----This is a menu----")
    print ("------Player1/Player2------")
a = int (input())
b = int (input())
c = int (input())
if a > 0 :
    print ("The computer choose the scissor")
    print ("The player choose the paper")
elif a < 0 : 
    print ("The computer and players choose the same. The game is draw") 
elif a == 0 : 
    print ("The player was lose the game")
else : 
    print ("The computer lose")    
if b > 0 : 
    print ("The computer choose rock")
    print ("The player choose the paper")
elif b < 0 : 
    print ("The computer lose")
elif b == 0 : 
    print ("The computer choose rock too")
    print ("The game draw")
else : 
    print ("The player lose the gmae ")

if c > 0 : 
    print("The player choose the scissor")
    print ("The computer choose rock")
else : 
    print ("The computer won")

game_maker = game(a,b,c)
return game_maker