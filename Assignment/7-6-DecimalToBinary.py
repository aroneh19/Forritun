def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        binary += "0"
    while decimal > 0:
        if decimal % 2 == 0:
            binary += "0"
        else:
            binary += "1"
        decimal = decimal // 2
    return binary[::-1]

print(decimal_to_binary(255))