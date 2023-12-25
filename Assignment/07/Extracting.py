def extract_first_number_from_string(string_to_search):
    lever = False
    number = ""

    for i in string_to_search:
        if i.isnumeric():
            lever = True
            number += i
        elif i.isnumeric() == False and lever == True:
            break
    if lever:
        return int(number)
    return -1

# print(extract_first_number_from_string("Hallo ég heiti aorn 195 og 19"))