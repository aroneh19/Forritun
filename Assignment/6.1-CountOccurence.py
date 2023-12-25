a_str = input()
char_to_count = input()
counter = 0

for i in a_str:
    if i == char_to_count:
        print(counter)
    counter += 1
