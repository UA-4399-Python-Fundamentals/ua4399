# Task3.
# Write a program that calculates the area of a rectangle S=a*b, the area of a triangle S=0.5*h*a, 
# the area of a circle S=pi*,**2. This module must be used in another module in which we ask the user 
# the area of which figure he wants to calculate.
# (To perform the task, you need to import the math module, and from it the pow() function and the value 
#  of the variable pi, and module, which contains three functions for finding areas, into the main program.
#    The basic logic of the program is executed in the main module).

import math
import Task3module

mode = input(" What area you are calculating ? \n  r - for rectangular \n  t - for triangle \n  c - for circle \n  Enter r, t or c:")
if mode == "r":
    a = int(input(f"Enter the length:"))
    b = int(input(f"Enter the width:"))
    print(Task3module.area_rectangular(a,b))
elif mode == "t":
    a = int(input(f"Enter the base:"))
    b = int(input(f"Enter the height:"))
    print(Task3module.area_triangle(a,b))
elif mode == "c":
    r = int(input(f"Enter the radius:"))
    print(Task3module.area_circle(r))