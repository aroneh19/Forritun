list1 = []
list2 = []
list3 = []

while True:
    num = input().lower()
    if num == "x":
        break
    else:
        list1.append(num)

for i in list1:
    if i == list1[0]:
        list2.append(i)
        previous = i[-1] 
    elif i[0] == previous:
        list2.append(i)
        previous = i[-1]
    else:
        list3.append(i)

for i in list2:
    if i != list2[-1]:
        print(i, end=" ")
    else:
        print(i)

for i in list3:
    if i != list3[-1]:
        print(i, end=" ")
    else:
        print(i)