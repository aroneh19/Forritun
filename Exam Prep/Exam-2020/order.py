class Order:
    def __init__(self, item: str, price: float):
        self.item = item
        self.price = price

    def __str__(self):
        return f"Item: {self.item}, price: {self.price}"