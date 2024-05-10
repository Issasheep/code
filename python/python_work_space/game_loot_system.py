import random

#a item drops 
#that item has a chance to have some rarity on it

item_rareity_list = ["common","uncommon","rare","epic","legendary","hero's"]
possable_number_of_effects = [0,random.randint(1,2),random.randint(2,3),random.randint(3,5),random.randint(5,8),random.randint(8,10)]
possable_item_effects = ["fire damage","frost damage","crit chance","crit damage"]

#all this will be assuming a item dropping event happened


item_dropped_score = random.randint(1,1000)

#if item_dropped_score >= 200: #common

def item_rareity(item_rareity_list,item_dropped_score):
    

for i in item_dropped:
    print (i)