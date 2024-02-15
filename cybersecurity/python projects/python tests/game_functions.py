import random

amount_dropped = 10

item_dict = []
roll_values = []

all_item_types = ["weapon","armor","spells","unique"]

def item_list():
    counter = 0
    while amount_dropped >= counter:
        item_dict.append(all_item_types[random.randrange(0,4)])
        counter +=1
    return item_dict

def item_value_rolls():
    counter = 0
    for x in item_dict:
        item_roll_value = random.randrange(300,1001)
        roll_values.append(item_roll_value)
        counter +=1
    return item_roll_value

#make a fucntion randomizes numbers from 300-1001 and make a ductonary with the output of the item_list functiuon 