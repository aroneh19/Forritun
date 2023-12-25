
def get_name():
    while True:
        name = input("What's your name? ")
        if all(char.isalpha() or char.isspace() for char in name) and any(char.isalpha() for char in name):
            return name
        else:
            print("Please enter a valid name.")

def get_age():
    while True:
        age_str = input("How old are you? ")
        if age_str.isdigit():
            age = int(age_str)
            if 0 <= age <= 125:
                return age
            else:
                print(f"You seriously expect me to believe you are {age} years old?")
        else:
            print("Please enter an integer.")

if __name__ == "__main__":
    name = get_name()
    age = get_age()
    print(f"Nice to meet you {name}. Congratulations on your {age} years.")

