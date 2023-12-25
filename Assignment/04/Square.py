size = int(input())

for i in range(size):
    for x in range(size):
        if i == 0 or i == size - 1 or x == 0 or x == size - 1:
            if x == size - 1:
                print("*", end="")
            else:
                print("*", end=" ")
        else:
            print(" ", end=" ")
    print()