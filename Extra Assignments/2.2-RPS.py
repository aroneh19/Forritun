val1 = input()
val2 = input()

if val1 == "rock" and val2 == "paper":
    print("Player 2")
elif val1 == "rock" and val2 == "scissors":
    print("Player 1")
elif val1 == "paper" and val2 == "rock":
    print("Player 1")
elif val1 == "paper" and val2 == "scissors":
    print("Player 2")
elif val1 == "scissors" and val2 == "paper":
    print("Player 1")
elif val1 == "scissors" and val2 == "rock":
    print("Player 2")
else:
    print("Draw")