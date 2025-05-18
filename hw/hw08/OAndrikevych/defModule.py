# This module contains three functions for finding areas

import math

def rectangle_area():
    """
    This function calculates the area of a rectangle.
    """
    a = float(input("Enter the length of the rectangle: "))
    b = float(input("Enter the width of the rectangle: "))
    area = round((a * b), 2)
    return area

def triangle_area():
    """
    This function calculates the area of a triangle.
    """
    a = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    area = round((0.5*h*a), 2)
    return area

def circle_area():
    """
    This function calculates the area of a circle.
    """
    r = float(input("Enter the radius of the circle: "))
    area = round((math.pi * r**2), 2)
    return area
