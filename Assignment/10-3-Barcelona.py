taska = input()
taska = taska.split()

rod = input()
rod = rod.split()

counter = 1

for i in rod:
    if rod[0] == taska[1]:
        print("fyrst")
        break
    elif rod[1] == taska[1]:
        print("naestfyrst")
        break
    elif i == taska[1]:
        print(counter, "fyrst")
    counter += 1