class Prices:
    def __init__(self, name):
        self.name = name
        self.price_dict = {}

    def set_price(self, symbol: str, price: float):
        self.price_dict[symbol] = price
    
    def get_price(self, stock: str):
        if stock in self.price_dict.keys():
            return self.price_dict[stock]
        else: return None

    def __str__(self) -> str:
        result = f"{self.name}:"
        for symbol, price in self.price_dict.items():
            result += f"\n{symbol}: {price:.2f}"
        return result
