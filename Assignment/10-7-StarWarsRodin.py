def main():
    num = int(input())
    number = input().split()

    # Define the dictionary
    my_dict = {
        "1": 4,
        "2": 5,
        "3": 6,
        "4": 1,
        "5": 2,
        "6": 3,
        "7": 7,
        "8": 8,
        "9": 9
    }
    converted_numbers = []
    for num in number:
        converted_numbers.append(dict[num])

    sorted_numbers = sorted(converted_numbers)

    original_numbers = [key for key, value in my_dict.items() if value in sorted_numbers]

    # Print the sorted original numbers
    for i in range(num):
        if original_numbers[i] in dict:
            if i == num - 1:
                print(dict[original_numbers[i]])
            else:
                print(dict[original_numbers[i]], end=" ")
        else:
            if i == num - 1:
                print(original_numbers[i])
            else:
                print(original_numbers[i], end=" ")

if __name__ == "__main__":
    main()
