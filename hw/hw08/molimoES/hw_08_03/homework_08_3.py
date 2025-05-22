# Homework Lesson 08

# ///////////////////////////////////////////////////////////////////
# 3 - Calculates the area og rectangle, triangle  and circle
print("Subtask 3")

import math_functions

figure = input("Select a figure to calculate: Rectangle (1), Circle (2) or Triangle (3): ")
if not figure in ('1', '2', '3'):
    print("Unexpected figure. Try again.")
    exit
    
if figure == '1':
    print("RECTANGLE")
    length = float(input("Enter the length of a rectangle: "))
    width  = float(input("Enter the width of a rectangle: "))
    
    print(f"The area of a rectangle is: {math_functions.area_of_rectangle(length, width)}")
elif figure == '2':
    print("CIRCLE")
    radius = float(input("Enter the radius of the circle: "))
    
    print(f"The area of the circle is: {math_functions.area_of_circle(radius)}")
elif figure == '3':
    print("TRIANGLE")
    height = float(input("Enter the height of a triangle: "))
    width  = float(input("Enter the width of a triangle: "))
    
    print(f"The area of a triangle is: {math_functions.area_of_triangle(height, width)}")
