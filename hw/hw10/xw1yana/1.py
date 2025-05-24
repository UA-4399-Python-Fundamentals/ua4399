class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, lenght, width):
        super().__init__(4)
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width