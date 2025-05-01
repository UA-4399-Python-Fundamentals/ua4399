import math


def triangle_area(base, height):
    """
        Returns the area of triangle based on given base and height
        Args:
            base (number): The base of a triangle
            height (number): The height of a triangle
    """
    return "Not a number" if not base.isdigit() or not height.isdigit() else round(float(base) * float(height) / 2,2)


def rectangle_area(length, width):
    """
        Returns the area of triangle based on given base and height
        Args:
            length (number): The length of a rectangle
            width (number): The width of a rectangle
    """
    return "Not a number" if not length.isdigit() or not width.isdigit() else round(float(length) * float(width),2)


def circle_area(radius):
    """
        Returns the area of circle based on given radius
        Args:
            radius (number): The radius of a circle
    """
    return "Not a number" if not radius.isdigit() else round(math.pi * math.pow(float(radius),2),2)

def calculator(figure, first_num, second_num=""):
    """
        Calls certain function to calculate area depending on the given values
        Args:
            figure (str): rectangle, circle or triangle
            first_num(str): base, length or radius, depending on the figure
            second_num(str): height, width or nothing, depending on the figure
    """
    match figure:
        case "rectangle":
            return rectangle_area(first_num, second_num)
        case "triangle":
            return triangle_area(first_num, second_num)
        case "circle":
            return circle_area(first_num)
        case _:
            return "Entered figure is not supported"


def init():
    """
    Asks the user for the figure to calculate area, then first and second(if needed) value
    Pass them to calculator() function
    """
    vals = {
        "rectangle": ["length", "width"],
        "triangle": ["base", "height"],
        "circle": ["radius"]
    }

    figure = input("Enter figure to calculate area: rectangle, triangle or circle: ")
    if figure not in vals:
        return f"The figure {figure} is not supported"

    first_num = input(f"Please enter the {vals[figure][0]} ")
    second_num = input(f"Please enter the {vals[figure][1]} ") if not figure == "circle" else "0"
    result = calculator(figure, first_num, second_num)
    if result == "Not a number":
        return "Only digits supported"
    else:
        return f"The area of a {figure} based on its {" and ".join(vals[figure])} is {result}"

print(init())


