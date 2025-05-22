import math
import figures

area = input("Choose what to calculate area for: rectangle / triangle / circle : ")

match area:
    case "rectangle":
        a = int(input("Side a: "))
        b = int(input("Side b: "))
        figures.area_rectangle(a, b)
    case "triangle":
        a = int(input("Side a: "))
        b = int(input("Height h: "))
        figures.area_triangle(a, b)
    case "circle":
        r = int(input("Radius r: "))
        figures.area_circle(r)
    case _:
        print("Figure not found!")