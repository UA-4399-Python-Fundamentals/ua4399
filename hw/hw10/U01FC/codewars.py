####
class Ball:
    def __init__(self, ballType = "regular"):
        self.ball_type = ballType

####
import random
class Ghost(object):
    __colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(self.__colors)

####
class Human:
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        pass

    def __str__(self):
        return "Man"

class Woman(Human):
    def __init__(self):
        pass

    def __str__(self):
        return "Woman"

def God():
    return [Man(), Woman()]

####
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.info = f"{name}s age is {age}"

####
import math
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4 / 3 * (math.pi * self.radius ** 3), 5)
    
    def get_surface_area(self):
        return round(4 * (math.pi * self.radius ** 2), 5)
    
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
    
####
import string

def class_name_changer(cls, new_name):
    if not (new_name.isalnum() and new_name.startswith(tuple(string.ascii_uppercase))):
        raise Exception("Should be alphanumeric and start with uppercase letter")
    cls.__name__ = new_name
