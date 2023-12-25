def main():
    num1_str = input()
    num2_str = input()

    result = divide_safe(num1_str, num2_str)
    print(result)

def divide_safe(num1_str, num2_str):
    try:
        num1_float = float(num1_str)
        num2_float = float(num2_str)
        result = num1_float / num2_float
        return round(result, 5)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
main()
