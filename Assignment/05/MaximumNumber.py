
num = int(input())

while True:
    num2 = int(input())
    if num2 < 0:
        break
    elif num2 > num:
        num = num2
print(num)