class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0] * no_of_sides

    def input_sides(self):
        self.sides = [float(input(f"Enter side {i+1}: ")) for i in range(self.n)]

    def display_sides(self):
        print("The sides are:", ", ".join(map(str, self.sides)))


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
        self.width = 0
        self.height = 0

    def input_sides(self):
        self.width = float(input("Enter width: "))
        self.height = float(input("Enter length: "))
        self.sides = [self.width, self.height]

    def find_area(self):
        return self.width * self.height


rect = Rectangle()
rect.input_sides()
rect.display_sides()
print(f"The area of the rectangle is: {rect.find_area()}")
