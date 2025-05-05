def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return 3.14 * radius ** 2

shape = input("Choose shape (rectangle/triangle/circle): ").strip().lower()

if shape == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", area_rectangle(l, w))
elif shape == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", area_triangle(b, h))
elif shape == "circle":
    r = float(input("Enter radius: "))
    print("Area:", area_circle(r))
else:
    print("Unknown shape.")