#1 Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Example usage
ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)  # Output: "regular"
print(ball2.ball_type)# your code goes here

# Color Ghost
import random

# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Example usage
ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)  # Output: "regular"
print(ball2.ball_type)  # Output: "super"

#2 Color Ghost
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Example usage
ghost = Ghost()
print(ghost.color) # Output: "white", "yellow", "purple", or "red"

#3 Basic subclasses - Adam and Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    """Creates Adam and Eve."""
    return [Man(), Woman()]


# Example usage
creation = God()
print(isinstance(creation[0], Man))  # Output: True
print(isinstance(creation[1], Woman))  # Output: True
print(isinstance(creation[0], Human))  # Output: True
print(isinstance(creation[1], Human))  # Output: True

#4 Classy Classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# Example usage
person = Person("John", 34)
print(person.info)  # Output: "Johns age is 34"

#5 Building Spheres
import math

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        """Returns the radius of the sphere."""
        return self.radius

    def get_mass(self):
        """Returns the mass of the sphere."""
        return self.mass

    def get_volume(self):
        """Returns the volume of the sphere, rounded to 5 decimal places."""
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        """Returns the surface area of the sphere, rounded to 5 decimal places."""
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        """Returns the density of the sphere, rounded to 5 decimal places."""
        density = self.mass / self.get_volume()
        return round(density, 5)


# Example usage
sphere = Sphere(2, 50)
print(sphere.get_radius())        # Output: 2
print(sphere.get_mass())          # Output: 50
print(sphere.get_volume())        # Output: 33.51032
print(sphere.get_surface_area())  # Output: 50.26548
print(sphere.get_density())       # Output: 1.49208

#6 Dynamic Classes
def class_name_changer(cls, new_name):
    """Changes the name of a given class to a new valid name."""
    if not new_name.isalnum() or not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name


# Example usage
class MyClass:
    pass

# Change class name to UsefulClass
class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__)  # Output: UsefulClass

# Change class name to SecondUsefulClass
class_name_changer(MyClass, "SecondUsefulClass")
print(MyClass.__name__)  # Output: SecondUsefulClass

# Invalid class name example
try:
    class_name_changer(MyClass, "invalidName")
except ValueError as e:
    print(e)  # Output: Class name must start with an uppercase letter and contain only alphanumeric characters.

try:
    class_name_changer(MyClass, "Invalid Name!")
except ValueError as e:
    print(e)  # Output: Class name must start with an uppercase letter and contain only alphanumeric characters.