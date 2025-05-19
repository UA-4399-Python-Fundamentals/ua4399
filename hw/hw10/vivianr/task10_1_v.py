class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, length):
        super().__init__(4)
        self.width = width
        self.length = length
    def square(self):
        return self.width * self.length