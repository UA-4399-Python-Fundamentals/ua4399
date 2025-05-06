import math
#Task1
def max(a,b):
    """
    Returns the maximum of two numbers.
    
    Parameters:
    a (int): First number
    b (int): Second number
    
    Returns:
    int: The maximum of a and b
    """
    return a if a > b else b
#Task2
def areaOfTheRectangle(length, width):
    """
    Calculates the area of a rectangle.
    
    Returns:
    int: The area of the rectangle
    """
    return length * width


def areaOfTheCircle(radius):
    """
    Calculates the area of a circle.
    
    Returns:
    float: The area of the circle
    """
    return round(math.pi * radius * radius, 2)
                 
def areaOfTheTriangle(base, height):
    """
    Calculates the area of a triangle.
    
    Returns:
    float: The area of the triangle
    """
    return 0.5 * base * height

choice = input("Choose the shape whose area you want to calculate: Rectangle (R), Circle (C) or Triangle (T): ").strip().upper()
if choice == 'R':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = areaOfTheRectangle(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == 'C':
    radius = float(input("Enter the radius of the circle: "))
    area = areaOfTheCircle(radius)
    print(f"The area of the circle is: {area}")
elif choice == 'T':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = areaOfTheTriangle(base, height)
    print(f"The area of the triangle is: {area}")
else:
    print("Invalid choice. Please choose R, C, or T.")

#Task3
count_characters = lambda s: {char: s.count(char) for char in set(s)}
user_input = input("Enter a string: ")
result = count_characters(user_input)
print(result)
