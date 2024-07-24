import time

witch_temp = input("write f to find your temp in fahrenheit or c for celsius \n")

if witch_temp == "c":
    user_temp_input_C = int(input("what celsius is it? "))
    user_temp_input_F = (user_temp_input_C * 1.8) + 32
    print (user_temp_input_F)
    time.sleep(2)
    quit 
if witch_temp == "f":
    user_temp_input_F = int(input("what fahrenheit is it? "))
    user_temp_input_C = (user_temp_input_F / 1.8) - 32
    print (user_temp_input_C)
    time.sleep(2)
    quit
else:
    print ("try again")


