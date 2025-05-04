import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

choice = input("Введіть фігуру (rectangle/triangle/circle): ").lower()

if choice == "rectangle":
    l = float(input("Довжина: "))
    w = float(input("Ширина: "))
    print("Площа:", rectangle_area(l, w))

elif choice == "triangle":
    b = float(input("Основа: "))
    h = float(input("Висота: "))
    print("Площа:", triangle_area(b, h))

elif choice == "circle":
    r = float(input("Радіус: "))
    print("Площа:", circle_area(r))

else:
    print("Невідома фігура.")
