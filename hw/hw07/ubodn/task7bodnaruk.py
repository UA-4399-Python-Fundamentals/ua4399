# Task 1

def max_of_two(a, b):
    """
    Returns the largest of two numbers.
    """
    return a if a > b else b


# Task 2

import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

def choose_area():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print("Area of rectangle:", area_rectangle(length, width))

    elif choice == "2":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        print("Area of triangle:", area_triangle(base, height))

    elif choice == "3":
        radius = float(input("Enter the radius: "))
        print("Area of circle:", area_circle(radius))

    else:
        print("Invalid choice.")


choose_area()


# Task 3

def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

print(count_characters("softserve"))
