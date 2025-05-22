# Homework Lesson 10

# ///////////////////////////////////////////////////////////////////
# 1 - Inherits of class
print("Subtask 1")

class Polygon:
    def __init__(self, height, width):
        self.height = height
        self.width  = width
    
    def square(self):
        pass


class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__(height, width)
    
    def square(self):
        return self.height * self.width


r = Rectangle(height=10, width=20)
print(f"The square of a rectangle is {r.square()}")
