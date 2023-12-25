program = input()
file = open(program, "r")

for line in file:
    words = line.split(" ")
    for i in words:
        print(i[::-1])