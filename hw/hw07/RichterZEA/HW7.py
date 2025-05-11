# TASK1
# def hw1(a, b):
#     """Returns the greater number"""
#     if a > b:
#         return a
#     elif b > a:
#         return b
# print(hw1(5, 10))
# help(hw1)

#TASK2
# import math
# def rec(len, wid):
#     area = len * wid
#     return area
# def tri(bass, heig):
#     area = 0.5 * bass * heig
#     return area
# def cir(rad):
#     area = math.pi * rad **2
#     return area
# a = input("Choose a figure to calculate: ").lower()
# if a == "rectangle":
#     len = float(input("Length: "))
#     wid = float(input("Width: "))
#     print(rec(len, wid))
# elif a == "triangle":
#     bass = float(input("Base: "))
#     heig = float(input("Height: "))
#     print(tri(bass, heig))
# elif a == "circle":
#     rad = float(input("Radius: "))
#     print(cir(rad))
# else:
#     print("I don't know this geometric figure..")

#TASK3
def num(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char, count in counts.items():
        print(f"{char}: {count}")

num("Home Work 07")