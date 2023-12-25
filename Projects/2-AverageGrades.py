
average_grade = 0
highest_grade = 0
total_weight = 0
counter = 0

while True:
    grade = float(input())
    if grade >= 0:
        counter = 1
        weight = int(input())
        total_weight += weight
        if grade > highest_grade:
            highest_grade = grade
        average_grade += grade * weight
    else:
        break

if counter == 1:
    if total_weight > 0:
        weighted_average_grade = average_grade / total_weight
        print(f"Weighted average grade: {round(weighted_average_grade, 2)}")
    print(f"Highest grade: {highest_grade}")