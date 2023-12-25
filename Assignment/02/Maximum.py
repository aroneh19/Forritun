
num1 = int(input()) # Do not change this line
num2 = int(input()) # Do not change this line
num3 = int(input()) # Do not change this line

if num1 >= num2 and num1 >= num3:
    max_int = num1
elif num2 >= num1 and num2 >= num3:
    max_int = num2
elif num3 >= num2 and num3 >= num1:
    max_int = num3

print(max_int) # Do not change this line
