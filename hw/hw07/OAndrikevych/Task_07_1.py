print("Task 07.1.1")
# Task1. Write a function that returns the largest number of two numbers
def max_of_two(num1: float, num2: float) -> float:
    """
    This function returns the larger of two numbers.

    Parameters:
    num1 (float): 1st number
    num2 (float): 2nd number

    Returns:
    max_of_two (float): The larger of two numbers
    """
    return max(num1, num2)

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

print(f"The greater of {num1} and {num2} is: {max_of_two(num1, num2)}")

print("\nTask 07.1.2")
# Task2. Write a program that calculates the area of a rectangle, triangle and circle

import math

def rectangle_area():
    """
    This function calculates the area of a rectangle.
    """
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = round((length * width), 2)
    return area

def triangle_area():
    """
    This function calculates the area of a triangle using Heron's formula.
    """
    a = float(input("Enter the 1st side length of the triangle: "))
    b = float(input("Enter the 2nd side length of the triangle: "))
    c = float(input("Enter the 3rd side length of the triangle: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)

def circle_area():
    """
    This function calculates the area of a circle.
    """
    radius = float(input("Enter the radius of the circle: "))
    area = round((math.pi * radius**2), 2)
    return area

def main():
    """
    The main function asks for the object and calculates its area.
    """
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

print("\nTask 07.1.3")
# Task3. Write a function that calculates the number of characters

def count_char(s: str) -> dict:
    """
    This function returns a dictionary with character counts in the given string
    """
    out = {}
    for char in s:
        out[char] = out.get(char, 0) + 1
    return out

st = input("Enter a string: ")
res = count_char(st)
print(res)