#Task 1 Create a polygon class and a rectangle class
#that inherits from the polygon class and finds the square
#of rectangle.
class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0] * num_sides
    def set_sides(self, sides_list):
        if len(sides_list) != self.num_sides:
            raise ValueError(f"A polygon with {self.num_sides} sides requires exactly {self.num_sides} side lengths.")
        self.sides = sides_list
    def get_sides(self):
        return self.sides
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width
        self.set_sides([length, width, length, width])
    def area(self):
        return self.length * self.width
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width}, area={self.area()})"
rect = Rectangle(5, 3)
print(rect)
print("Sides:", rect.get_sides())