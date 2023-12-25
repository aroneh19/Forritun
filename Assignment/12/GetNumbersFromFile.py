def main():
    filename = get_valid_filename()
    numbers = get_numbers_from_file(filename)
    display_numbers(numbers)

def get_valid_filename():
    while True:
        filename = input()
        if file_exists(filename):
            return filename
        else:
            print(f"{filename} not found! Please try again.")

def file_exists(filename: str):
    try:
        with open(filename, 'r'):
            return True
    except FileNotFoundError:
        return False

def get_numbers_from_file(filename: str) -> list:
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                tokens = line.strip().split()
                for token in tokens:
                    if token.isdigit():
                        number = int(token)
                        numbers.append(number)
            return numbers
    except FileNotFoundError:
        return []

def display_numbers(numbers):
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)

if __name__ == "__main__":
    main()