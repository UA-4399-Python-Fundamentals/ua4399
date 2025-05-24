# Task 1
def my_func(number_one=0, number_two=0):
    """
    Returns the largest of two numbers.

    Parameters:
    number_one (int or float): The first number.
    number_two (int or float): The second number.

    Returns:
    int or float: The larger of the two numbers.
    """
    return max(number_one, number_two)

print(my_func(4,8))


# Task 2
import math
def rectangle_area(w, l):
    A = w*l
    return A
def triangle_area(h, b):
    A = h*b/2
    return A
def circle_area(r):
    A = math.pi * r ** 2
    return A
choice = input("Enter your choice (rectangle/triangle/circle): ")

if choice == "rectangle":
    # Get input from user
    w = float(input("Enter the rectangle width (integer or float): "))
    l = float(input("Enter the rectangle length (integer or float): "))
    print(rectangle_area(w, l))
elif choice == "triangle":
    h = float(input("Enter the triangle height (integer or float): "))
    b = float(input("Enter the triangle base (integer or float): "))
    print(triangle_area(h, b))
elif choice == "circle":
    r = float(input("Enter the circle radius (integer or float): "))
    print(circle_area(r))
else:
    print("Invalid choice.")


# Task 3
def count_characters(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result