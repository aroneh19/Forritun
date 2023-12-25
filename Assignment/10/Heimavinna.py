homework = input()

homework = homework.split(";")

result = 0

for i in homework:
    if "-" in i:
        i = i.split("-")
        result += int(i[1]) - int(i[0]) + 1
    else:
        result += 1
print(result)