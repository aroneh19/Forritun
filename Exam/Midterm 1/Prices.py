
counter = 0
total_price = 0
lowest_price = 0

while True:
    price = float(input())
    if price == 0:
        break
    else:
        counter += 1
        total_price += price
        if (price < lowest_price) or (lowest_price == 0):
            lowest_price = price
print(f"Number of items: {counter}")
if total_price == 0:
    print(f"Total price: 0.0")
else:
    print(f"Total price: {round(total_price, 1)}")
if lowest_price != 0:
    print(f"Lowest price: {lowest_price}")