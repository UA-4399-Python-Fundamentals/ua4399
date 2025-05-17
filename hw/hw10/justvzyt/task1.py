class Polygon:
    def find_area(self):
        print("Area of the figure is", self.side**2)
    
    def __init__(self, side):
        self.side = side

class Rectangle(Polygon):
    pass

g = Rectangle(20)
g.find_area()