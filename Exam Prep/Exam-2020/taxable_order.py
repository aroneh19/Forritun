class TaxableOrder:
    def __init__(self, item: str, price: float, tax: float):
        self.item = item
        self.price = price + (price * tax)
    
    def __str__(self):
        return f"Item: {self.item}, price: {self.price}"