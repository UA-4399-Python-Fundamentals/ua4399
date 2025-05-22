# HW 7.1
# Task1. Write a function that returns the largest number of two numbers (use DocStrings documentation strings in the function).
def large(a,b):
    if a > b:
        return a
    else:
        return (b)
print (large(76,4))    

# Task2. Write a program that calculates the area of a rectangle, triangle and circle (write three functions to calculate the area.
#  And call them in the main program depending on the user's choice).
def area_rectangular(a,b):
    print(f"Area of rectangular: {a * b}")
def area_triangle(a,b):
    print(f"Area of triagnle: {1/2* a * b}")
def area_circle(r):
    print(f"Area of circle: {3.14 * r *r }")

mode = input(" What area you are calculating ? \n  r - for rectangular \n  t - for triangle \n  c - for circle \n  Enter r, t or c:")
if mode == "r":
    a = int(input(f"Enter the length:"))
    b = int(input(f"Enter the width:"))
    area_rectangular(a,b)
elif mode == "t":
    a = int(input(f"Enter the base:"))
    b = int(input(f"Enter the height:"))
    area_triangle(a,b)
elif mode == "c":
    r = int(input(f"Enter the radius:"))
    area_circle(r)



# Task3. Write a function that calculates the number of characters included in given string
# • input: "hello"
# • output: {"h":1, "e":1, "|":2,"O":1}

def char_counter(string="hello"):
    counter={}
    for i in string:
        counter[i]=counter.get(i,0)+1
    return counter

print(char_counter("hello"))
