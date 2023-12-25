def sum_of_divisors(number):
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result += i
    return result

def decide(number):
    result = sum_of_divisors(number)
    if result == number:
        return f"{number} is a perfect number."
    elif result < number:
        return f"{number} is deficient."
    elif result > number:
        return f"{number} is abundant."

# print(decide(10))