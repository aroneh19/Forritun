num = int(input())
divider = 0
result = 0

for i in range(1, num + 1):
    divider += 1
    result = result + (1 / (2 ** divider))
    print(result)