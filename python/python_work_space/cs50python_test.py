import numpy as np
width = int(input("how large? "))
length = int(input("how long? "))
counter = 1
for i in range(width):
    print ("\n")
    counter += 1
    #length -= counter
    for i in range(length -i):
        print (" * ",end="")
