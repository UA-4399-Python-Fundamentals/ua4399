import math


def area_rectangle(width, length):
    width = float(width)
    length = float(length)
    area = width * length
    return area


def area_triangle(height, base):
    height = float(height)
    base = float(base)
    area = 0.5 * height * base
    return area


def area_circle(radius):
    radius = float(radius)
    area = math.pi * pow(radius, 2)
    return area


__all__ = ["area_rectangle", "area_triangle", "area_circle"]
