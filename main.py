#this is the main file for this game... there will be others included

#first we have to import the necessary libraries
import math
import random
import time
import sys
import os
import json

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
    worlds_file=json.load(open("worlds.json","r"))
    worlds=[]
    worldlist=[]
    world_data=[]
    for world in worlds_file["worlds"]:
        try:
            cworld=open(world,"r")
            cworld_file=json.load(cworld)
            worlds.append(cworld_file)
            worldlist.append(world)
            world_data.append(cworld_file["world_data"])
        except:
            print("A world could not be loaded!")
    game_main(worldlist,10,10,[],worlds,world_data,0)
    #[worldarr],gold,health,items,worlds
    #new_game calls game_main with basic init settings
def save_data(data_arr,save_n):
    pass
def load_data(save_n):
    pass
#game main loop here
def partial_move_run(partial_move,worldlist,gold_l,health_l,items_l,worlds,world_data,cw):
    if partial_move["type"]=="normal":
        print(partial_move["text"])
    elif partial_move["type"]=="add_items":
        items=items_l
        world_data_n=world_data
        try:
            items_l.append(world_data["item_gain_random_wr"])#not done need to fix
def interpret_json_game(worldlist,gold_l,health_l,items_l,worlds,world_data,cw):
    current_world_data=worlds[cw]
    game_choices=current_world_data["game_loop"]
    move=random.randint(0,len(game_choices)-1)
    move_data=game_choices[move]
    for partial_move in move_data:
        partial_move_run(partial_move,worldlist,gold_l,health_l,items_l,worlds,world_data,cw)
    print(current_world_data)
    time.sleep(10)
def game_main(worldlist,gold_l,health_l,items_l,worlds,world_data,cw):
    print(worlds)
    #main game loop
    gold=gold_l
    health=health_l
    items=items_l
    game_p=True
    while game_p:
        interpret_json_game(worldlist,gold_l,health_l,items_l,worlds,world_data,cw)
title_screen()
