import random

choice = ["n", "e", "s","w"]
random_choice = random.choice(choice)

def moves():
    global coins
    while True:
        y = 1
        x = 1
        player_location = (x, y)
        print("You can travel: (N)orth.")
        
        while player_location != (3, 1):
            the_move = input("Direction: ")
            if (the_move == "n" or the_move == "N") and y < 3 and player_location != (2,2):
                y += 1 
            elif (the_move == "s" or the_move == "S") and y > 1 and player_location != (2,3):
                y -= 1     
            elif (the_move == "e" or the_move == "E") and x < 3 and player_location != (1,1) and player_location != (2,1) and player_location != (2,2):
                x += 1
            elif (the_move == "w" or the_move == "W") and x > 1 and player_location != (2,1) and player_location != (3,1) and player_location != (3,2):
                x -= 1
            else:
                print("Not a valid direction!") 
                invalid_location(player_location)
                continue
            player_location = (x, y)
            lever_check(player_location)
            location_options(player_location)
        play_again = input("Play again (y/n):")
        print()
        coins = 0
        if play_again.lower() == "n":
            break
    return player_location

def location_options(location):
    x, y = location
    if x == 3 and y == 1:
        print(f"Victory! Total coins {coins}.")
    elif x == 1 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")    
    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")     
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")        
    elif x == 3 and y == 3 :
        print("You can travel: (S)outh or (W)est.")
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    else:
        print("Not a valid direction!")
    return location

def invalid_location(location):
        x, y = location
        if  x == 1 and y == 1:
            print("You can travel: (N)orth.")
        elif x == 1 and y == 2:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif x == 1 and y == 3:
            print("You can travel: (E)ast or (S)outh.")
        elif x == 2 and y == 1:
            print("You can travel: (N)orth.")    
        elif x == 2 and y == 2:
            print("You can travel: (S)outh or (W)est.")     
        elif x == 2 and y == 3:
            print("You can travel: (E)ast or (W)est.")        
        elif x == 3 and y == 3 :
            print("You can travel: (S)outh or (W)est.")
        elif x == 3 and y == 2:
            print("You can travel: (N)orth or (S)outh.")
        return location
coins = 0

def lever_check(location):
        x, y = location
        global coins 
        if x == 1 and y == 2:
            print("Pull a lever (y/n):")
            lever_inp = input().lower()
            if lever_inp == "y":
                coins += 1
                print(f"You received 1 coin, your total is now {coins}.")
        elif x == 2 and y == 2:
            print("Pull a lever (y/n):")  
            lever_inp = input().lower()
            if lever_inp == "y":
                coins += 1
                print(f"You received 1 coin, your total is now {coins}.")
        elif x == 2 and y == 3:
            print("Pull a lever (y/n):")
            lever_inp = input().lower()
            if lever_inp == "y":
                coins += 1
                print(f"You received 1 coin, your total is now {coins}.")
       
        elif x == 3 and y == 2:
            print("Pull a lever (y/n):")
            lever_inp = input().lower()
            if lever_inp == "y":
                coins += 1
                print(f"You received 1 coin, your total is now {coins}.")

        return location

moves()
