from fun import rectangle, triangle, circle

figure = input("Choose a figure to calculate its area: ").lower()
if figure == "rectangle":
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    print("Area of the rectangle:", rectangle(a, b))
elif figure == "triangle":
    a = float(input("Base a: "))
    h = float(input("Height h: "))
    print("Area of the triangle:", triangle(a, h))

elif figure == "circle":
    r = float(input("Radius r: "))
    print("Area of the circle:", circle(r))
else:
    print("Unknown figure.")