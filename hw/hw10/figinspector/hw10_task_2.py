# I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
    
    
# II. Color-ghost
import random

class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

        
# III. Basic-subclasses-Adam-and-Eve
def God():
    return [Man(), Woman()]

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass


# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property            
    def info(self):
        return f"{self.name}s age is {self.age}"
    

# V. Building Spheres
# block
class Block:
    def __init__(self, dimensions):
        self.width, self.length, self.height = dimensions
        
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        w, l, h = self.width, self.length, self.height
        return 2 * (w * l + w * h + l * h)
    
# sphere
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
        volume = (4 / 3) * math.pi * self.radius ** 3
        return round(volume, 5)

    def get_surface_area(self):
        area = 4 * math.pi * self.radius ** 2
        return round(area, 5)

    def get_density(self):
        density = self.mass / ((4 / 3) * math.pi * self.radius ** 3)
        return round(density, 5)


# VI. Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise Exception("Invalid class name")
    cls.__name__ = new_name
    return cls