high = 1000
low = 1
counter = 0
guess = 500

while counter < 10:
    counter += 1

    print(guess)
    cmd = input()

    if cmd == "c":
        print("I AM VICTORIOUS")
        break
    elif cmd == "h":
        high = guess - 1
        guess = int((low + high) / 2)
    elif cmd == "l":
        low = guess + 1
        guess = int((low + high) / 2)
    elif cmd == "q":
        print("Quitter")
        break
else:
    print("Tsk, tsk, don't try to cheat me")