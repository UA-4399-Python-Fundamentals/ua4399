#Task1. Write a function that returns the largest number of two numbers
def get_larger_number(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a(int): The first number.
    b(int): The second number.

    Returns:
    int or float: The larger of the two numbers.
    """
    return a if a > b else b
print(get_larger_number(10, 25))

#Task2. Write a program that calculates the area of a rectangle, triangle and circle (write three functions to calculate the area, and call them in the main program depending on the user's choice).
import math

def rect_area(l, w): return l * w
def tri_area(b, h): return 0.5 * b * h
def circ_area(r): return math.pi * r ** 2

def rectangle():
    c = input("1-Rectangle 2-Triangle 3-Circle: ")
    if c == '1':
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("Area:", rect_area(l, w))
    elif c == '2':
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("Area:", tri_area(b, h))
    elif c == '3':
        r = float(input("Radius: "))
        print("Area:", circ_area(r))
    else:
        print("Invalid choice.")

rectangle()

#Task 3. Write a function that calculates the number of characters included in a given string
def count_characters(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts
print(count_characters("hello"))