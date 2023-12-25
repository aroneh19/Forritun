a_str = input()

last_name, first_name = a_str.split(", ")
last_name = last_name.capitalize()
first_character = first_name[0].upper()

print(f"{first_character}. {last_name}")