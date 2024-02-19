import random
import pygame
import sys
import os
amount_dropped = 10

item_dict = []
roll_values = []

all_item_types = ["weapon","armor","spells","unique"]
rareities = ["common","uncommon","rare","legendary"]
poassble_min = ["200","400","600","800"]
poassble_max = ["200","400","800","1000"]

def item_list():
    counter = 0
    while amount_dropped >= counter:
        min_max_stats = random.randrange(0,4)
        item_dict.append(all_item_types[random.randrange(0,4)])
        item_dict.append(roll_values[random.randrange(poassble_min[min_max_stats],poassble_max[min_max_stats],10)])
        counter +=1
    return item_dict

print (item_list())



#make a fucntion randomizes numbers from 300-1001 and make a ductonary with the output of the item_list functiuon 