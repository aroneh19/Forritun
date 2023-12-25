class Height:
    def __init__(self, feet, inches): # Initialize height
        self.feet = feet

        while inches >= 12: # Checks if inches is higher than 12
            self.feet += 1 # Adds to feet
            inches -= 12 # Deducts from inches
        self.inches = inches
    
    def cm(self):
        ft_to_cm = self.feet * 30.48 # Calculates feet to cm
        in_to_cm = self.inches * 2.54 # Calculates inches to cm
        centimeter = round(ft_to_cm + in_to_cm) # Adds them together
        return centimeter

    def __gt__(self, other):
        # Checks if self height is greater than other height
        return (self.feet > other.feet) or ((self.feet == other.feet) and (self.inches > other.inches))

    def __add__(self, other):
        # Adds self height to other height
        return Height(self.feet + other.feet, self.inches + other.inches) # Creating a new combined height

    def __str__(self) -> str:
        return f"{self.feet} ft, {self. inches} in" # Returns the specified format