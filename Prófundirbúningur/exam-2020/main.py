from order import Order
from taxable_order import TaxableOrder

def check_orders(order_list):
    for i in range(len(order_list)-1):
        order1 = order_list[i]
        order2 = order_list[i+1]
        if order1.price > order2.price:
            print(f"{order1.item} is more expensive ({order1.price}) than {order2.item} ({order2.price})")
        else:
            print(f"{order1.item} is more (or equally) expensive ({order1.price}) than {order2.item} ({order2.price})")

# Main starts here
order1 = Order("iPhone", 1000.0) # An order with the item iPhone and the price
1000.0
order2 = Order("Kindle", 200.5)
order3 = Order("Samsung", 850.9)
# An order with the item Lenovo, the price 800.0 and 10% tax.
# The price with tax should be rounded to one decimal digit.
order4 = TaxableOrder("Lenovo", 800.0, 0.1)

order_list = [order1, order2, order3, order4]
for order in order_list:
    print(order)
check_orders(order_list)
order5_item = f"{order1.item}+{order2.item}"
order5_price = order1.price + order2.price
print(f"Item: {order5_item}, price: {order5_price}")
order6_item = f"{order5_item}+{order4.item}"
order6_price = order5_price + order4.price
print(f"Item: {order6_item}, price: {order6_price}")

