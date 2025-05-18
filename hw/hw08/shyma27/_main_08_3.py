import _module_08_3 as m
from math import pow, pi

formula = input("What do you want to calculate: ").lower()
if formula == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print(m.rectangle_area(l, w))
elif formula == "triangle":
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    print(m.triangle_area(b, h))
elif formula == "circle":
    r = float(input("Enter radius: "))
    #print(m.circle_area(r))
    print(m.circle_area(pow(r, 2), pi))
else:
    print("Incorrect name")