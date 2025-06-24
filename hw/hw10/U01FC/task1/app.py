class Polygon:
    def __init__(self, num_sides):
        self.__num_sides = num_sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width