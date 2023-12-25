answer = input("You need something doubled? (Y)es? ")

while True:
    if answer == "Y":
        number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
        print(number*2)
        answer = input("You need something else doubled? (Y)es? ")
    else:
        break