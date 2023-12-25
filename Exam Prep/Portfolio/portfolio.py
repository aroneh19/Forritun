from stock import Stock
from prices import Prices

class Portfolio():
    def __init__(self, name):
        self.name = name
        self.collection = []
                 
    def add(self, stock: Stock):
        self.collection.append(stock)
    
    def value(self, prices: Prices):
        value = 0
        for stock in self.collection:
            if prices.get_price(stock.symbol) is not None:
                value += prices.get_price(stock.symbol) * stock.shares
        return value
    
    def __str__(self):
        result = f"{self.name}:"
        for stock in self.collection:
            result += f"\n{stock.symbol}: {stock.shares}"
        return result
