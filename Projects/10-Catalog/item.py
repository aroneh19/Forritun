class Item:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
    
    def set_name(self, name: str):
        self.name = name
    
    def set_category(self, category: str):
        self.category = category

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category}"