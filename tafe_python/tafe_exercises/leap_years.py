year_input = int(input("what year would you like to know? "))
if year_input < 1582:
    print("Not within the Gregorian calendar period")
    quit
elif year_input % 4:
    print("it's a common year")
    quit
elif year_input % 100:
    print("it's a leap year")
    quit
elif year_input % 400:
    print("it's a common year")
    quit
else:
    print("it's a leap year")