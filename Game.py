# -*- coding: utf-8 -*-
"""
Spyder Editor
Ansar Mazhar
Electrical Engineer
This is a temporary script file.
"""
#Main function
row1 = [7,8,9]
row2 = [4,5,6]
row3 = [1,2,3]
u = 0

def printt(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    return 0
def interface(row1,row2,row3): 
    print("Welcome to Tic Tac Toe")
    print("It is a game between two players at the same computer")
    print("There are two symbols for move: O and X")
    print("For player1 symbol is O")
    print("For player2 symbol is X")
    print("You have to select a digit as showing on the interface")
    printt(row1,row2,row3)
    return 0

def input1(row1,row2,row3):
   inp1 = input("First Choice: Enter your choice:\n")
   return int(inp1)
def input2(row1,row2,row3):
   inp2 = input("Second Player: Enter your choice: \n")
   return int(inp2)

def decision_making1(row1,row2,row3):
    global u
    b = input1(row1,row2,row3)
    if b == 7:
        row1[0] = "O"
    elif b == 8:
        row1[1] = "O"
    elif b == 9:
         row1[2] = "O"
    elif b == 4:
         row2[0] = "O"
    elif b == 5:
         row2[1] = "O"
    elif b == 6:
         row2[2] = "O"
    elif b == 1:
         row3[0] = "O"
    elif b == 2:
         row3[1] = "O"
    elif b == 3:
         row3[2] = "O"
    else:
        pass
def decision_making2(row1,row2,row3):
    global u
    c = input2(row1, row2, row3)
    if c == 7:
        row1[0] = "X"
    elif c == 8:
        row1[1] = "X"
    elif c == 9:
         row1[2] = "X"
    elif c == 4:
         row2[0] = "X"
    elif c == 5:
         row2[1] = "X"
    elif c == 6:
         row2[2] = "X"
    elif c == 1:
         row3[0] = "X"
    elif c == 2:
         row3[1] = "X"
    elif c == 3:
         row3[2] = "X"
    else:
        pass    
def matching1(row1,row2,row3):
    global u
    if row1[0]=="O" and row1[1]=="O" and row1[2]=="O":
        print("Player1 Won!")
        u = 1
    elif row1[0]=="O" and row2[0]=="O" and row3[0]=="O":
        print("Player1 Won!")
        u = 1
    elif row1[2]=="O" and row2[2]=="O" and row3[2]=="O":
        print("Player1 Won!")
        u = 1
    elif row3[0]=="O" and row3[1]=="O" and row3[2]=="O":
        print("Player1 Won!")
        u = 1
    elif row1[1]=="O" and row2[1]=="O" and row3[1]=="O":
        print("Player1 Won!")
        u = 1
    elif row1[0]=="O" and row2[1]=="O" and row3[2]=="O":
        print("Player1 Won!")
        u = 1
    elif row1[2]=="O" and row2[1]=="O" and row3[0]=="O":
        print("Player1 Won!")
        u = 1
    else:
        pass
def matching2(row1,row2,row3):
    global u
    if row1[0]=="X" and row1[1]=="X" and row1[2]=="X":
        print("Player 2 Won!")
        u = 1
    elif row1[0]=="X" and row2[0]=="X" and row3[0]=="X":
        print("Player 2 Won!")
        u = 1
    elif row1[2]=="X" and row2[2]=="X" and row3[2]=="X":
        print("Player 2 Won!")
        u = 1
    elif row3[0]=="X" and row3[1]=="X" and row3[2]=="X":
        print("Player 2 Won!")
        u = 1
    elif row1[1]=="X" and row2[1]=="X" and row3[1]=="X":
        print("Player 2 Won!")
        u = 1
    elif row1[0]=="X" and row2[1]=="X" and row3[2]=="X":
        print("Player 2 Won!")
        u = 1
    elif row1[2]=="X" and row2[1]=="X" and row3[0]=="X":
        print("Player 2 Won!")
        u = 1
    else:
        pass
#Function in case match is drawn
def draw():
    print("Match has been drawn!!")
def greetings():
    print("Thanks for playing the game TIC TACK TOE")
    print("Hope you have enjoyed it")
interface(row1,row2,row3)
#Loop completes total 8 moves and remains one move
for i in range(5):
    decision_making1(row1, row2, row3)
    matching1(row1, row2, row3)
    if u == 1:
        break #If player1 wins loop breaks
    printt(row1,row2,row3)
    decision_making2(row1, row2, row3)
    matching2(row1, row2, row3)
    if u == 1:
        break #If player2 wins loop breaks
    printt(row1,row2,row3)


# u=0 in case match is drawn
if u == 0:
    draw()
    printt(row1,row2,row3)
greetings()

    
    
