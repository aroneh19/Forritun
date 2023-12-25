number = int(input()) # Do not change this line

while number > 0:
    if number % 10 == 7:
        print("The number contains 7.")
        break
    else:
        number //= 10
else:
    print("The number does not contain 7.")