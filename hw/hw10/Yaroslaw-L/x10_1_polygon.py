from abc import ABC, abstractmethod
class Polygon(ABC):
        @abstractmethod
        def area_p(self):
                pass
        
class Rectangle(Polygon):
        def __init__(self, width, height):
                self.width = width
                self.height = height
        def area_p(self):
                return self.width*self.height
#Create for rectangle
width, height = map(float, input("Type a width and height of rectangle separated by space: ").split())
rct = Rectangle(width, height)
print("Area of rectangle: ", rct.area_p())