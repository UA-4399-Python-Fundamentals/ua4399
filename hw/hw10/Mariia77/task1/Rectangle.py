from Polygon import Polygon


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def findArea(self):
        a, b = self.sides
        area = a * b
        print(f"The area of rectangle is {area}")
