def area_of_rectangle(length, width) -> float:
    """
    Calculates the area of a rectangle.
    
        Parameters:
            length (float): Length of a rectangle
            width (float):  Width of a rectangle
        
        Returns:
            (int): The area of a rectangle
    """
    
    return length * width


def area_of_circle(radius) -> float:
    """
    Calculates the area of a circle.
    
        Parameters:
            radius (float): Radius of a circle
        
        Returns:
            (float): The area of a circle
    """
    
    from math import pi, pow
    
    return round(pi * pow(radius, 2), 2)


def area_of_triangle(height, width) -> float:
    """
    Calculates the area of a triangle.
        
        Parameters:
            height (float): Height of a triangle
            width (float):  Width of a triangle
        
        Returns:
            (float): The area of a triangle
    """
    
    return height * width / 2
