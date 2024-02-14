#lets crunshy some numbers 
all_item_types = ["weapon","armor","spells","unique"]
import random 
amount_dropped = 10
counter = 0
item_dict = {}
def item_type():
    item = random.randrange(0,3)
    return item
while amount_dropped >= counter:
    print(item_type())
    counter +=1