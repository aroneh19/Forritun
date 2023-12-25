
def main():
    password = ""
    valid_list = []
    invalid_list = []

    while password != "quit":
        password = input("Enter password: ")
        if password.lower() == "quit":
            break

        if check_password(password):
            print("Password is valid")
            valid_list.append(password)
        else:
            print("Password is invalid")
            invalid_list.append(password)
        
    if valid_list:
        print("\nValid passwords:")
        print_passwords(valid_list)

    if invalid_list:
        print("\nInvalid passwords:")
        print_passwords(invalid_list)
        
def check_password(password: str):
    num_counter = 0

    for i in password:
        if i.isnumeric():
            num_counter += 1

    if len(password) >= 8:
        if num_counter >= 3:
            return True
    return False

def print_passwords(passwords: list[str]):
    password_length = 0
    digit_counter = 0
    for password in passwords:
        print(password, end=" ")
        password_length += len(password)

        for word in password:
            if word.isnumeric():
                digit_counter += 1
    print()

    average_length = password_length / len(passwords)
    average_digits = digit_counter / len(passwords)

    print(f"Average length: {average_length:.1f}")
    print(f"Average # of digits: {average_digits:.1f}")

if __name__ == '__main__':
    main()