#this is the main file for this game... there will be others included

#first we have to import the necessary libraries
import math
import random
import time
import sys

#set the --- var
line="----------"

#libs imported

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)
def input_gnui(input_array,input_q):
    input_t=False
    while input_t not in input_array:
        input_t=input(input_q).upper()
    return input_t
    #that was just a simple function for getting input with an array, the main UI one will come next
def input_gnui_wm(input_array,input_q,input_m):
    print(input_m)
    return input_gnui(input_array,input_q)
    #this function adds a message which will usually be used but not always
def input_main(input_array,input_m):
    #this automatically generates an input_q
    input_array_r=[]
    input_q_r=""
    for item in input_array:
        input_array_r.append(str(item).upper())
        input_q_r+=str(item).upper()+", "
    input_q_r=input_q_r[:-2]+": "
    return input_gnui_wm(input_array_r,input_q_r,input_m)
def title_screen():
    #title screen of game
    print_slow("The Adventure Game")
    print("\n"+line)
    input_g=input_main(["N","R","T","E"],"(N)ew game, (R)esume game, (T)utorial, (E)xit")
    if input_g=="N":
        new_game()
    elif input_g=="R":
        print("Coming soon!")
    elif input_g=="T":
        print("Coming soon!")
    elif input_g=="E":
        print_slow("Exiting...")
        exit()
def new_game():
    game_main([],10,10,[])
    #[worldarr],gold,health,items
    #new_game calls game_main with basic init settings
