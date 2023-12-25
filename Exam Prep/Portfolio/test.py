from stock import Stock
from prices import Prices
from portfolio import Portfolio

# Create a few stocks
stock_apple = Stock("AAPL", 1000)
stock_google = Stock("GOOGL", 500)
stock_amazon = Stock("AMZN", 300)
stock_dell = Stock("DELL", 700) # This stock will not have a price
print(stock_apple)
print()

# Create a portfolio and add stocks to it
portfolio = Portfolio("My stocks")
print(portfolio)
portfolio.add(stock_apple)
portfolio.add(stock_google)
portfolio.add(stock_amazon)
portfolio.add(stock_dell)
print(portfolio)
print()

# Create market prices 
prices = Prices("Closing prices")
print(prices)
prices.set_price("AAPL", 145.85)
prices.set_price("GOOGL", 96.27)
prices.set_price("AMZN", 92.96)
print(prices)
print()

# The value of a portfolio is the sum of the market value of the individual stocks.
# The market value of a stock is the market price * number of shares.
# If no price exists for at stock, the market value of the stock is 0.
value = portfolio.value(prices)
print(f"Value of portfolio is: {value:.2f}")

# Change the market price and recompute the value of the portfolio
prices.set_price("GOOGL", 99.75)
print(prices.get_price("GOOGL"))
value = portfolio.value(prices)
print(f"Value of portfolio is: {value:.2f}")
