import math

def area_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"
    s = (a + b + c) / 2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)


def area_rectangle(length, width):
    return length * width


def area_circle(radius):
    return round(math.pi * radius ** 2, 2)