#1
class Ball(object):
    def __init__(self, type = "regular"):
        self.ball_type = type
        
#2
import random
class Ghost:
    def __init__(self):
        self.color =  random.random.choice("white" or "red" or "yellow" or "purple")
        
#3
class Human(object):
    def __init__(self):
        pass

class Man(Human):
    def __init__(self, name):
        self.name = name

class Woman(Human):
    def __init__(self, name):
        self.name = name

def God():
    adam = Man('Adam')
    eva = Woman('Eva')
    return [adam, eva]

#4
class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s, age is {self.age}"
        
#5
class Sphere:
    def __init__(self, radius, mass):
        self.radius = int(radius)
        self.mass = int(mass)

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * 3.14159 * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * 3.14159 * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)
    
#6
import re
def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-]+$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception

