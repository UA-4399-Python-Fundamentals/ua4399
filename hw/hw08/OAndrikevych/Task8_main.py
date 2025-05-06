print("Task 08.3")
# Task3. Write a program that calculates the area of a rectangle and a triangle

"""
This main program asks for the object and calculates its area.
"""

import sys
print(sys.path)

import math

from defModule import rectangle_area, triangle_area, circle_area

def main():
    print("Which object's area would you like to calculate?")
    print("1: Rectangle")
    print("2: Triangle")
    print("3: Circle")

    try:
        choice = int(input("Enter your choice (1, 2, or 3): ").strip())
    except ValueError:
        print("Invalid input! Please enter a whole number (1, 2, or 3).")
        return

    match choice:
        case 1:
            area = rectangle_area()
            print(f"The area of the rectangle is: {area}")
        case 2:
            area = triangle_area()
            print(f"The area of the triangle is: {area}")
        case 3:
            area = circle_area()
            print(f"The area of the circle is: {area}")
        case _:
            print("Invalid choice.")

if __name__ == "__main__":
    main()