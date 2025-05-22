import math

def rectangle_area(a, b):
    """Calculate the area of a rectangle."""
    return a * b

def triangle_area(a, h):
    """Calculate the area of a triangle."""
    return 0.5 * a * h

def circle_area(r):
    """Calculate the area of a circle."""
    return math.pi * math.pow(r, 2)

__all__ = ['rectangle_area', 'triangle_area', 'circle_area']