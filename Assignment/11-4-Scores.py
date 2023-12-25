
score = input()
result= 0
score_list = []
list = score.split(" ")
for i in list:
    score_list.append(float(i))

score_list.sort()
newlist = score_list[3:]


if len(score_list) >= 3:
    for i in newlist:
        result += float(i)
    print(f"Sum of scores (3 lowest removed): {result}")
else:
    print("At least 3 scores needed!")