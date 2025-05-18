import math

def area_rectangle():
    a = float(input("a side: "))

    return a**2

def area_triangle():
    a = float(input("A side: "))
    b = float(input("B side: "))
    c = float(input("C side: "))

    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def area_circle():
    r = float(input("r: "))

    return math.pi*(r**2)

choice = input("Choose: rectangle / triangle / circle : ")

match choice:
    case "rectangle":
        print(area_rectangle())
    case "triangle":
        print(area_triangle())
    case "circle":
        print(area_circle())
    case _:
        print("Unknown figure! Check for a typo.")
