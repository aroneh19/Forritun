counter = 0  # Counter for passsword attempts
valid = 0  # Counter for valid passwords
invalid = 0  # counter for invalid passwords

while True:
    uppercase = False
    lowercase = False
    number = False
    length = False
    password = input()  # Input for password
    
    if password == "q":
        break
    else:
        counter += 1  # Increases for each attempt
    
    if 20 >= len(password) >= 6:  # Checks if password length is between 6 and 20 characters
        length = True

    for i in password:  # Checks for each character in password whether it has a lower or upper case and a number
        if i.isupper():
            uppercase = True
        if i.islower():
            lowercase = True
        if i.isnumeric():
            number = True

    if length:
        if not lowercase:
            print(f"{password}: Missing lower case letter.")
        if not uppercase:
            print(f"{password}: Missing upper case letter.")
        if not number:
            print(f"{password}: Missing numeric letter.")
        if length and lowercase and uppercase and number:
            print(f"{password}: Valid password of length {len(password)}.")
            valid += 1
        else:
            invalid += 1
    else:
        print(f"{password}: Invalid length.")
        invalid += 1

# Prints how many times it took and how many valid and invalid passwords were entered
print(f"You tried {counter} passwords, {valid} valid, {invalid} invalid.")
