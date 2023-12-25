x, y = 1, 1
lever = False

while True:
    if x == 1 and y == 1:
        if lever:
            print("Direction: You can travel: (N)orth.")
        else:
            print("You can travel: (N)orth.")
        direction = input()
        if direction == "n" or direction == "N":
            y += 1
            lever = True
        else:
            print("Direction: Not a valid direction!")
            lever = False

    elif x == 1 and y == 2:
        if lever:
            print("Direction: You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input()
        if direction == "n" or direction == "N":
            lever = True
            y += 1
        elif direction == "e" or direction == "E":
            lever = True
            x += 1
        elif direction == "s" or direction == "S":
            lever = True
            y -= 1
        else:
            print("Direction: Not a valid direction!")
            lever = False
    
    elif x == 1 and y == 3:
        if lever:
            print("Direction: You can travel: (E)ast or (S)outh.")
        else:
            print("You can travel: (E)ast or (S)outh.")
        direction = input()
        if direction == "e" or direction == "E":
            lever = True
            x += 1
        elif direction == "s" or direction == "S":
            lever = True
            y -= 1
        else:
            print("Direction: Not a valid direction!")
            lever = False
    
    elif x == 2 and y == 1:
        if lever:
            print("Direction: You can travel: (N)orth.")
        else:
            print("You can travel: (N)orth.")
        direction = input()
        if direction == "n" or direction == "N":
            lever = True
            y += 1
        else:
            print("Direction: Not a valid direction!")
            lever = False
    
    elif x == 2 and y == 2:
        if lever:
            print("Direction: You can travel: (S)outh or (W)est.")
        else:
            print("You can travel: (S)outh or (W)est.")
        direction = input()
        if direction == "w" or direction == "W":
            x -= 1
            lever = True
        elif direction == "s" or direction == "S":
            y -= 1
            lever = True
        else:
            print("Direction: Not a valid direction!")
            lever = False

    elif x == 2 and y == 3:
        if lever:
            print("Direction: You can travel: (E)ast or (W)est.")
        else:
            print("You can travel: (E)ast or (W)est.")
        direction = input()
        if direction == "e" or direction == "E":
            x += 1
            lever = True
        elif direction == "w" or direction == "W":
            x -= 1
            lever = True
        else:
            print("Direction: Not a valid direction!")
            lever = False
    
    elif x == 3 and y == 1:
        print("Direction: Victory!")
        break
    
    elif x == 3 and y == 2:
        if lever:
            print("Direction: You can travel: (N)orth or (S)outh.")
        else:
            print("You can travel: (N)orth or (S)outh.")
        direction = input()
        if direction == "n" or direction == "N":
            y += 1
            lever = True
        elif direction == "s" or direction == "S":
            y -= 1
            lever = True
        else:
            print("Direction: Not a valid direction!")
            lever = False
    
    elif x == 3 and y == 3:
        if lever:
            print("Direction: You can travel: (S)outh or (W)est.")
        else:
            print("You can travel: (S)outh or (W)est.")
        direction = input()
        if direction == "s" or direction == "S":
            y -= 1
            lever = True
        elif direction == "w" or direction == "W":
            x -= 1
            lever = True
        else:
            print("Direction: Not a valid direction!")
            lever = False