import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
   
    length = 5.0
    width = 3.0
    base = 4.0
    height = 2.0
    radius = 1.0

    print(f"Area of rectangle: {area_rectangle(length, width)}")
    print(f"Area of triangle: {area_triangle(base, height)}")
    print(f"Area of circle: {area_circle(radius)}")