import math

def rectangular_area(side_a: float, side_b: float) -> float:
    """
    Calculates the area of a rectangle

    Args: Length of one side of the rectangle.
          Length of the adjacent side.

    Returns: The area of the rectangle.
    """
    return side_a * side_b


def triangle_area(base_a: float, height_h: float) -> float:
    """
    Calculates the area of a triangle.

    Args: Length of the base of the triangle.
          Height of the triangle.

    Returns: The area of the triangle.
    """
    return 1/2 * base_a * height_h


def circle_area(r: float, π = math.pi) -> float:
    """
    Calculates the area of a circle.

    Args: Radius of the circle.

    Returns: The area of the circle, rounded to 2 decimal places.
    """
    return round(π * math.pow(r, 2), 2)