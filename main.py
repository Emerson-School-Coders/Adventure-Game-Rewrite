#this is the main file for this game... there will be others included

#first we have to import the necessary libraries
import math
import random
import time
import sys
import os

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
    input_g=input_main(["N","R","T","E", "S"],"(N)ew game, (R)esume game, (T)utorial, (E)xit, (S)ettings")
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
    game_main([{0:tutorial_world,1:earth_main_world},0],10,10,[])
    #[worldarr],gold,health,items
    #new_game calls game_main with basic init settings
def save_data(data_arr,save_n):
    pass
def load_data(save_n):
    pass
#world defs here

#game main loop here
def game_main(world_array_l,gold_l,health_l,items_l):
    #main game loop
    world_array=world_array_l
    gold=gold_l
    health=health_l
    items=items_l
    game_p=True
    while game_p:
        turn_ret=world_array[0][world_array[1]](world_array,gold,health,items)
        if turn_ret[0]==True:#this means we're rewriting main vars, otherwise we're just updating some
            world_array=turn_ret[1]
            gold=turn_ret[2]
            health=turn_ret[3]
            items=turn_ret[4]
        else:
            gold+=turn_ret[2]
            health+=turn_ret[3]
            for item in turn_ret[4]:
                items.append(item)
            for item in turn_ret[5]:
                items.remove(item)