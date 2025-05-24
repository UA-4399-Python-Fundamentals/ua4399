# Homework Lesson 07

# ///////////////////////////////////////////////////////////////////
# 1 - Return the largest number
print("Subtask 1")

def largest_number(number1: int, number2: int) -> int:
    """
    Calculates the largest number of two numbers.
    
        Parameters:
            number1 (int): First number
            number2 (int): Second number
    
        Returns:
            (int): The largest number of two numbers
    """
    
    return number1 if number1 > number2 else number2
    

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(f"Number {largest_number(number1, number2)} is larger from the numbers of {number1} and {number2}")

# ///////////////////////////////////////////////////////////////////
# 2 - Area of rectangle, triangle and circle
print("Subtask 2")

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
    
    from math import pi
    
    return round(pi * radius ** 2, 2)


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


figure = input("Select a figure to calculate: Rectangle (1), Circle (2) or Triangle (3): ")
if not figure in ('1', '2', '3'):
    print("Unexpected figure. Try again.")
    exit
    
if figure == '1':
    print("RECTANGLE")
    length = float(input("Enter the length of a rectangle: "))
    width  = float(input("Enter the width of a rectangle: "))
    
    print(f"The area of a rectangle is: {area_of_rectangle(length, width)}")
elif figure == '2':
    print("CIRCLE")
    radius = float(input("Enter the radius of the circle: "))
    
    print(f"The area of the circle is: {area_of_circle(radius)}")
elif figure == '3':
    print("TRIANGLE")
    height = float(input("Enter the height of a triangle: "))
    width  = float(input("Enter the width of a triangle: "))
    
    print(f"The area of a triangle is: {area_of_triangle(height, width)}")


# ///////////////////////////////////////////////////////////////////
# 3 - Number of characters
print("Subtask 3")

def number_of_chars(string: str) -> dict:
    """
    Calculates the number of characters in the string.
        
        Parameters:
            string (str): String to analyze
        
        Returns:
            (dict): Dictionary with the results of count of characters
    """
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    
    return result

string = input("Enter a string to calculate characters: ")
print(number_of_chars(string))
