
file_name = input()

file = open(file_name, "r")

list = []
list1 = []
list2 = []
list3 = []


for line in file:
    num = line.strip()
    try:
        num = float(num)
        list.append(num)
        num = str(num)
        list1.append(num)
    except ValueError:
        continue

if list:
    print(" ".join(list1))  # Question 1

    # ----------------------------------------------------------------

    result = 0
    for i in list:
        result += i
        list2.append(str(round(result, 1)))
    print(" ".join(list2)) # Question 2

    # ----------------------------------------------------------------

    list.sort()
    for i in list:
        i = str(i)
        list3.append(i)
    print(" ".join(list3)) # Question 3

    # ----------------------------------------------------------------

    # Calculate the median
    length = len(list)
    middle = length // 2

    if length % 2 == 0:
        median = (list[middle - 1] + list[middle]) / 2
    else:
        median = list[middle]

    print(round(median, 2))
