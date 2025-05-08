from point import Point

class Point2D(Point):
    def __init__(self, x, y, color=(0, 0, 0)):
        super().__init__(x, y)

        print(f"creating a 2D point {x}, {y} {color}")
        self.color = color  # default color black
        

    def __str__(self):
        print(super().__str__())
        return f"Point2D({self.x}, {self.y}, {self.color})"
        # return f"Point2D({self.x}, {self.y}, {self.color   })"
    # def __repr__(self):
    #     return f"<{self.x}, {self.y}>"


p1 = Point2D(10, 20)
print(p1)
# print([p1])
# print(Point2D.__mro__)
# print(list.__mro__)
# print(type(p1.__repr__))