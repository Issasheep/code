user_input = input("type a letter and see if it's a vowel ")
vowel_list = ["a","e","i","o", "u"]
place_holder_value = 0
for i in vowel_list:
    if i == user_input:
        print ("True")
        place_holder_value += 1
        quit

if place_holder_value == 0:
    print ("False")