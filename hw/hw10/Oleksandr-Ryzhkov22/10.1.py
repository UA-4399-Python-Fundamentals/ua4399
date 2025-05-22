class Poligon:
    def __init__(self, n):
        self.n = n
        self.sides = [0] * n

    def set_side(self, i, length):
        if 0 <= i < self.n:
            self.sides[i] = length
        else:
            raise IndexError("Side index out of range")

    def get_side(self, i):
        if 0 <= i < self.n:
            return self.sides[i]
        else:
            raise IndexError("Side index out of range")
        
class Rectangle(Poligon):   
    def __init__(self, width, height):
        super().__init__(4)
        self.set_side(0, width)
        self.set_side(1, height)
        self.set_side(2, width)
        self.set_side(3, height)

    def area(self):
        return self.get_side(0) * self.get_side(1)

area = Rectangle(5,10)
print(area.area())   