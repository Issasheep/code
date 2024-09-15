
lock = 0
while lock < 1:
    player_1 = input("player 1 rock, paper, scissors: ")
    player_2 = input("player 2 rock, paper, scissors: ")

    input_dict = {"paper":0,"rock":1,"scissors":2}

    if player_1 == player_2:
        print("it's a tie!")
    number_tran = input_dict

    x = int(input_dict.get(player_1))
    y = int(input_dict.get(player_2))

    z = y - x
    print (z)
    if x < y:
        if z < range(-1,1):
            print ("player 1 wins")
        else:
            print ("player 2 wins")
    else:
        print ("player 2 wins")
    if player_1 == "hello!":
        lock += 1


