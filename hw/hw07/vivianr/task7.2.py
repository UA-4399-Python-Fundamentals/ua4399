'''
Calculate the area of rectangle, triangle, and circle.
'''
import math
def rectangle_area(length, width):
    return length * width 

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

user_choice = input("Choose a shape (rectangle, triangle, circle): ")
if user_choice == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif user_choice == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is: {area}")       
elif user_choice == "circle":
    radius = float(input("Enter the radius: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area}") 
else:
    print("Invalid shape. Please choose rectangle, triangle, or circle.")
    