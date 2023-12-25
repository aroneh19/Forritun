class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares
    
    def __str__(self) -> str:
        return f"{self.symbol}: {self.shares}"
    