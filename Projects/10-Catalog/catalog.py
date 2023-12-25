class Catalog:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def set_name(self, name: str):
        self.name = name

    def add(self, item: str):
        self.items.append(item)

    def remove(self, item: str):
        self.items.remove(item)
    
    def clear(self):
        self.items = []

    def __str__(self):
        # Athugar hvort catalog-ið er tómt
        if self.items == []:
            catalog_string = f"Catalog {self.name}:" # Prentar catalog-ið
        else:     
            catalog_string = f"Catalog {self.name}:\n"
        for item in self.items:
            if item == self.items[-1]: # Athugar hvort myndin er seinasta myndin í catalog-inu
                catalog_string += f"\t{item}"
            else:
                catalog_string += f"\t{item}\n"
        return catalog_string # Returnar öllum myndunum