import math
def area_rectangle(length, width):
    return length * width
def area_triangle(base, height):
    return 0.5 * base * height
def area_circle(radius):
    return math.pi * radius ** 2
def main():
    print("Choose a shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of rectangle:", area_rectangle(l, w))
    elif choice == '2':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of triangle:", area_triangle(b, h))
    elif choice == '3':
        r = float(input("Enter radius: "))
        print("Area of circle:", area_circle(r))
    else:
        print("Invalid choice!")
main()