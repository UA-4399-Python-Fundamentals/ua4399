# Task 1
def find_greater_number(n1, n2):

    """This is a function that returns greater number from the 2 passed as an argument."""
    return n1 if n1>n2 else n2


# Task 2
import math

def triangle_area():

    """This is a functions to calculate area of a triangle. No parameters, the values and input-added."""

    base = int(input("Enter your base in cm: "))
    height_to_base = int(input("Enter the height to base in cm: "))
    area = height_to_base * base / 2
    return area

def rectangle_area():

    """This is a functions to calculate area of a rectangle. No parameters, the values and input-added."""

    a = int(input("Enter one side length: "))
    b = int(input("Enter another side length: "))
    area = a * b
    return area

def circle_area():

    """This is a functions to calculate area of a circle. No parameters, the values and input-added."""

    radius = int(input("Enter your radius: "))
    area = math.pi * radius ** 2
    return round(area,1)

def calculate_area():
    """This is a wrap-up function that allows to calculate the area of a user-chosen figure"""
    figure = input("Please enter a figure you want to calculate the area of: ")
    match figure:
        case "triangle":
            return triangle_area()
        case "rectangle":
            return rectangle_area()
        case "circle":
            return circle_area()
        case _:
            print("Please verify your input! Enter either triangle, circle, or rectangle.")

calculate_area()


# Task 3
def calculate_number_of_elements(str):
    result = {}
    for letter in str:
        count = str.count(letter)
        result.update({letter: count})
    print(result)


calculate_number_of_elements("hello")