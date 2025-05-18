import random
import math
import re

#Regular Ball Super Ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
# print(ball1.ball_type)  #=> "regular"
# print(ball2.ball_type)  #=> "super"

#Color Ghost
class Ghost():
    colors = ["red","yellow","purple","white"]

    def __init__(self):
        self.color = Ghost.colors[random.randint(0, len(Ghost.colors)-1)]

g1 = Ghost()
# print(g1.color)


#Basic subclasses - Adam and Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(),Woman()]



#Classy Classes
class Person:
    def __init__(self,name,age):
        self.info=f"{name}s age is {age}"
    def get_info(self):
        return self.info

#Building Spheres
class Sphere(object):
    def __init__(self,radius,mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        #volume = (4 / 3) × π × r³
        result = (4/3) * math.pi * math.pow(self.radius,3)
        return round(result,5)

    def get_surface_area(self):
        #SA = 4 * π * r²
        result = 4 * math.pi * math.pow(self.radius,2)
        return round(result, 5)

    def get_density(self):
        #density = mass / volume
        result = self.mass / Sphere.get_volume(self)
        return round(result, 5)

ball = Sphere(2, 50)
# print(ball.get_volume())
# print(ball.get_surface_area())
# print(ball.get_density())


#Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    check_name = re.compile(r'^[A-Z][A-Za-z0-9]*$')
    if not check_name.match(new_name):
        raise ValueError
    else:
        cls.__name__ = new_name
    return None

