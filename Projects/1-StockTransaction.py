symbol = input("\nThe stock symbol: ")
nshares = int(input("Number of shares: "))
bprice = float(input("The stock buying price: "))
sprice = float(input("The stock selling price: "))
paid = nshares * bprice
received = nshares * sprice
profit_loss = (received * 0.97 - paid * 1.03)

print(f"\nTransactions for stock: {symbol}")
print(f"Bought {nshares} shares @ {round(bprice, 2)}")
print(f"Paid {round(paid, 2)}")
print(f"Commission when buying: {round(paid*0.03, 2)}")
print(f"Sold {nshares} shares @ {round(sprice, 2)}")
print(f"Received {round(received, 2)}")
print(f"Commission when selling: {round(received*0.03, 2)}")
print(f"Profit or loss: {round(profit_loss, 2)}\n")