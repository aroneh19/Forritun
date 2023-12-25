a_str = input()
counter = 0
for i in a_str:
    if counter % 2 == 0:
        print(i, end="")
    counter += 1