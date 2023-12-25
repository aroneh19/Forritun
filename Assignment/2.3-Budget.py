budget = int(input())
project1 = int(input())
project2 = int(input())
project3 = int(input())

sufficient = budget - project1 - project2 - project3

if sufficient >= 0:
    print("Budget is sufficient.")
else:
    print("Budget is insufficient.")
