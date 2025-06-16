from math import pi, pow


def triangle_area():
    """Calculates triangle area"""
    while True:
        print("Enter numeric values:")
        height = input("Height value: ")
        base = input("Base value: ")
        if height.isnumeric() and base.isnumeric():
            area = float(height) * float(base) / 2
            return print(f"Triangle area: {round(area, 2)}")
        else:
            print("Error! Please, enter numerical values")


def rectangle_area():
    """Calculates rectangle area"""
    while True:
        print("Enter numeric values:")
        length = input("Length value: ")
        width = input("Width value: ")
        if length.isnumeric() and width.isnumeric():
            area = float(length) * float(width)
            return print(f"Rectangle area: {round(area, 2)}")
        else:
            print("Error! Please, enter numerical values")


def circle_area():
    """Calculates circle area"""
    while True:
        print("Enter numeric values:")
        radius = input("Radius value: ")
        if radius.isnumeric():
            area = (pow(float(radius), 2)) * pi
            return print(f"Circle area: {round(area, 2)}")
        else:
            print("Error! Please, enter numerical values")
