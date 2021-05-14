from tkinter import *
import random
def play():
    user=input("What is your choice:'r' for rock, 'p' for paper, 's' for scissors\n")
    computer=random.choice(['r','p','s'])
    print("Computer's choice "+ computer)
    if(user==computer):
        print("It's a tie");

    if is_win(user,computer):
        return "You won"
    else:
        return "you lost"

def is_win(player,opponent):
    if player=='r':
        if opponent=='s':
            return True
        else :
            return False
    elif player=='p':
        if opponent=='r':
            return True
        else:
            return False
    elif player=='s':
        if opponent=='p':
            return True
        else:
            return False
x=1
while(x):
    print(play())
    x=input("Play again?")

