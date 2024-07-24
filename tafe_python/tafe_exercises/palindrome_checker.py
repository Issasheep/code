user_input = input("this is a palindrone checker, so enter a word that maybe a palindrone ")
user_input_reversed =  user_input [::-1]

if user_input == user_input_reversed:
    print ("True")
else:
    print ("False")