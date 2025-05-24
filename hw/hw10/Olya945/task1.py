class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, lenght, width):
        super().__init__([lenght, width])
        self.length = lenght
        self.width = width

    def area(self):
        return self.length * self.width
    
    def output(self):
        return f"Прямокутник довжиною {self.length} і шириною {self.width} має площу {self.area()}"

rect = Rectangle(10, 7)
print(rect.output())
