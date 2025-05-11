import math


def area_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"
    s = (a + b + c) / 2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)


def area_rectangle(length, width):
    return length * width


def area_circle(radius):
    return round(math.pi * radius ** 2, 2)


def main():
    print("Choose a shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter 1, 2 or 3: ")

    if choice == '1':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of rectangle:", area_rectangle(length, width))

    elif choice == '2':
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))
        print("Area of triangle:", area_triangle(a, b, c))

    elif choice == '3':
        radius = float(input("Enter radius: "))
        print("Area of circle:", area_circle(radius), 2)

    else:
        print("Invalid choice!")


main()
