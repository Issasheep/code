import random

amount_dropped = 10

item_dict = []
roll_values = []

all_item_types = ["weapon","armor","spells","unique"]

def drop_test():
    item_list()

def item_list():
    counter = 0
    while amount_dropped >= counter:
        item_dict.append(all_item_types[random.randrange(0,4)])
        item_dict.append(random.randrange(300,1001))
        counter +=1
    return item_dict

#make a fucntion randomizes numbers from 300-1001 and make a ductonary with the output of the item_list functiuon 