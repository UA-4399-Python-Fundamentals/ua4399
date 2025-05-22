############################################################################## 1 ##############################################################################

# class Ball:
#     def __init__(self, ball_type: str = 'regular'):
#         self.ball_type = ball_type

# b1 = Ball('super')
# b2 = Ball()
# print(b1.ball_type)
# print(b2.ball_type)


############################################################################## 2 ##############################################################################

# import random

# class Ghost:
#     _color_list = ['yellow', 'purple', 'red']
#     def __init__(self):
#         self.color = random.choice(Ghost._color_list)

# g1 = Ghost()
# print(g1.color)


############################################################################## 3 ##############################################################################

# class Human:
#     def __init__(self, name):
#         self.name = name

# class Man(Human):
#     def __init__(self, name='Adam'):
#         super().__init__(name)

# class Woman(Human):
#     def __init__(self, name='Eva'):
#         super().__init__(name)

# def create():
#     return [Man(), Woman()]

# pair = create()
# print(type(pair[0]).__name__)
# print(type(pair[1]).__name__)
# print(pair[0].name)
# print(pair[1].name)


############################################################################## 4 ##############################################################################

# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     @property
#     def Info(self):
#         return f"{self.name}'s age is {self.age}"
    
#     def get_info(self):
#         return self.Info
    
# man = Person('John', 36)
# print(man.get_info())


############################################################################## 5 ##############################################################################

# import math

# class Sphere:
#     def __init__(self, radius: float, mass: float):
#         self.radius = radius
#         self.mass = mass

#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         volume = (4/3) * math.pi * self.radius**3
#         return round(volume, 5)
    
#     def get_surface_area(self):
#         surface_area = 4 * math.pi * self.radius**2
#         return round(surface_area, 5)
    
#     def get_density(self):
#         density = self.get_mass() / self.get_volume()
#         return round(density, 5)
    
# sp = Sphere(10, 15)

# print(sp.get_radius())
# print(sp.get_mass())
# print(sp.get_volume())
# print(sp.get_surface_area())
# print(sp.get_density())


############################################################################## 6 ##############################################################################

# import re

# def change_class_name(cls, new_name: str):
#     if not isinstance(new_name, str) or not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
#         raise ValueError(
#             "Invalid class name. The name must start with an uppercase letter and contain only alphanumeric characters.")
#     cls.__name__ = new_name
#     return cls

# class MyClass:
#     pass

# print(f"Old class name: {MyClass.__name__}")
# MyClass = change_class_name(MyClass, "SecondUsefulClass")
# print(f"New class name: {MyClass.__name__}")