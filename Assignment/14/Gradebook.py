def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)

def main():
    grades_dict = {}

    while True:
        email = input()
        grade = int(input())
        response = input()

        if email in grades_dict:
            grades_dict[email].append(grade)
        else:
            grades_dict[email] = [grade]

        if response == 'n':
            break

    emails = sorted(grades_dict.keys())

    for email in emails:
        grades = grades_dict[email]
        average_grade = calculate_average(grades)
        print(f"{email}: {average_grade}")

if __name__ == "__main__":
    main()
