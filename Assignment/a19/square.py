from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, length):
        self.length = length
    
    def get_area(self):
        return self.length ** 2

    def get_perimeter(self):
        return 4 * self.length