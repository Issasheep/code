int_one = input("type a number and find out witch one is larger! ")
int_two = input("type a number and find out witch one is larger! ")

if int_one == int_two:
    print("they are the same! ")
    quit
elif int_one > int_two:
    print ("is bigger " +int_one)
else:
    print ("is bigger " +int_two)