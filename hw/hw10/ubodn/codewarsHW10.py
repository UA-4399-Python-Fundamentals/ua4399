# Regular Ball Super Ball

class Ball():
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Color Ghost

import random

class Ghost():
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Basic subclasses - Adam and Eve

class Human():
    pass

class Man(Human):
    pass
        
class Woman(Human):
    pass

def God():
    return [Man(), Woman()]


# Classy Classes

class Person():
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# Building Spheres
   
import math

class Sphere():
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3
    
    def get_surface_area(self):
        return 4 * math.pi * self.radius ** 2
    
    def get_density(self):
        volume = self.get_volume()
        return self.mass / volume
    

# Python's Dynamic Classes #1

def class_name_changer(cls, new_name):
    cls.__name__ = new_name
    return cls.__name__





