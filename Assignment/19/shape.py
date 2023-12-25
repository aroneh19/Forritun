class Shape:
    def __str__(self):
        return f"{type(self).__name__} with area of {self.get_area():.2f} and perimeter of {self.get_perimeter():.2f}"
