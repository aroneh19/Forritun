
def collect_digits(a_str):
    result = ""  # result that will be returned
    for i in a_str:  # Loop that checks if it is a digit and adds it to result
        if i.isnumeric():
            result += i
    return result

def inverse_case(a_str):
    result = ""  # result that will be returned
    for i in a_str:  # Loop that checks if the character is upper or lower
        if i.isupper():  # If the character is upper then convert it to lower
            result += i.lower()
        else:  # If the character is lower then convert it to upper
            result += i.upper()
    return result

def to_hex(an_int):
    hex_characters = "0123456789ABCDEF"  # Set up 16 characters or all the possibilities in hex
    result = ""  # result that will be returned
    while an_int > 0:  # Loop that runs until all the numbers have been used
        remaining = an_int % 16  # Checks the remainders
        result += hex_characters[remaining]  # Adds to result the index of hex_characters
        an_int = an_int // 16
    return result[::-1]  # Returns the reverse of the result

while True:  # Loop that runs the code until q has been typed 
    start = input()
    if start == "q":
        break
    a_str = input()
    if start == "c":
        collected_digits = collect_digits(a_str)
        print(collected_digits)
    elif start == "i":
        inversed_case = inverse_case(a_str)
        print(inversed_case)
    elif start == "h":
        an_int = int(a_str)
        hex_value = to_hex(an_int)
        print(hex_value)