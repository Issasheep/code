# One way to sort two numbers into order
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

# We will use nested IF statements here
if (num1 == num2):
    print("The two numbers are equal")
else:
    # OK, so they are different. Use a second decision
    # to determine which one comes first
    if (num1 < num2):
        print(num1, "comes before", num2)
    else:
        print(num2, "comes before", num1)
        
# A second way to sort two numbers. This time we don't
# use nested IF statements
if (num1 == num2):
    print("The two numbers are equal")
elif (num1 < num2):
    print(num1, "comes before", num2)
else:
    print(num2, "comes before", num1)