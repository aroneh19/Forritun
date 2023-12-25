
price = int(input())
cash = int(input())
change = cash - price

while change > 0:
    if change >= 20:
        print(20)
        change -= 20
    elif change >= 10:
        print(10)
        change -= 10
    elif change >= 5:
        print(5)
        change -= 5
    elif change >= 2:
        print(2)
        change -= 2
    elif change >= 1:
        print(1)
        change -= 1