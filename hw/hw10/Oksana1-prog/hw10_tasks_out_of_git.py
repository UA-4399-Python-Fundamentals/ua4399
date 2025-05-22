#Task 1 Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
class Ball:
    def __init__(self, ball_type="regular"):
        self.ballType = ball_type
ball1 = Ball()
ball2 = Ball("super")
print(ball1.ballType)
print(ball2.ballType)
#Task Color-ghost
import random
class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
ghost1 = Ghost()
ghost2 = Ghost()
ghost3 = Ghost()
print(ghost1.color)
print(ghost2.color)
print(ghost3.color)
# Task 3 Basic-subclasses-Adam-and-Eve
class Human:
    def __init__(self, name=None):
        self.name = name
class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)
class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)
def create():
    return [Man(), Woman()]
first_humans = create()
print(type(first_humans[0]).__name__)
print(type(first_humans[1]).__name__)
print(first_humans[0].name)
print(first_humans[1].name)
#Task 4 Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def Info(self):
        return f"{self.name}'s age is {self.age}"
    def get_info(self):
        return self.Info
person1 = Person("John", 34)
print(person1.get_info())
# Task 5 Building Spheres
import math
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        return round(volume, 5)
    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)
    def get_density(self):
        volume = self.get_volume()
        if volume == 0:
            return 0
        density = self.mass / volume
        return round(density, 5)
sphere = Sphere(5, 100)
print(f"Radius: {sphere.get_radius()}")
print(f"Mass: {sphere.get_mass()}")
print(f"Volume: {sphere.get_volume()}")
print(f"Surface Area: {sphere.get_surface_area()}")
print(f"Density: {sphere.get_density()}")
#Test 6 Dynamic Classes
import re
def change_class_name(cls, new_name):
    if not isinstance(new_name, str) or not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise ValueError(
            "Invalid class name. The name must start with an uppercase letter and contain only alphanumeric characters.")
    cls.__name__ = new_name
    return cls
class MyClass:
    pass
print(f"Old class name: {MyClass.__name__}")
MyClass = change_class_name(MyClass, "SecondUsefulClass")
print(f"New class name: {MyClass.__name__}")
