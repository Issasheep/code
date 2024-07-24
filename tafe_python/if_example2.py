# Another example of an IF statement, this time with an ELIF and ELSE sections
age = int(input("Please enter your age in years: "))

# Use different conditions to determine what age bracket they are in.
# Pretend to be a computer, and step through each decision to see how
# the right age bracket is determined based on the age entered.
if (age < 0):
    print("Hmm, you haven't been born yet!")
elif (age < 13):
    print("You are a child")
elif (age < 20):
    print("You are a teenager")
elif (age < 50):
    print("You are an adult")
elif (age < 100):
    print("You are a senior citizen")
elif (age < 120):
    print("Wow, you are a centenarian!")
else:
    print("Either you are the oldest person alive, or you entered the wrong value")