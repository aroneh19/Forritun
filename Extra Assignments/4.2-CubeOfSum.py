max_int = int(input())

for i in range(max_int + 1):
    digit_sum = sum(int(digit) for digit in str(i))
    if i == digit_sum ** 3:
        print(i)