#this is the main file for this game... there will be others included

#first we have to import the necessary libraries
import math
import random
import time

#libs imported, now we can make the function for taking input, hope this works
def input(input_array,input_q):
    input_t=False
    while input_t not in input_array:
        input_t=input(input_q)
    return input_t
    #that was just a simple function for getting input with an array, the main UI one will come next
