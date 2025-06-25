class Polygon:
    def __init__(self, side):
        self.n = side
        self.sides = [0 for i in range(side)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)} : ")) for i in range(self.n)]
