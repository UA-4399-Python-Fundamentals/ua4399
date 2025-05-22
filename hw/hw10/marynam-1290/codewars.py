# I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# II. Color-ghost
import random


class Ghost(object):

    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# III. Basic-subclasses-Adam-and-Eve
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    adam = Man()
    eve = Woman()

    return [adam, eve]


# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        self.info = f"{name}s age is {age}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"


# V. Building Spheres
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
        volume = (4 / 3) * math.pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        volume_unrounded = (4 / 3) * math.pi * self.radius**3
        density = self.mass / volume_unrounded
        return round(density, 5)
