count = int(input())
list = []

for i in range(count):
    num = int(input())
    list.append(num)
list.reverse()

for i in list:
    print(i)
