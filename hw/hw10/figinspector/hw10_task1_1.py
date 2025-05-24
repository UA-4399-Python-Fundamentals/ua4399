from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width =  width
        self.height = height

    def area(self):
        return self.width * self.height
    
rect_1 = Rectangle(34, 55)
print(rect_1.area())