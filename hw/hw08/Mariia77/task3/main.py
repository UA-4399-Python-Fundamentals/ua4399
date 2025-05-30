from hw.hw07.Mariia77.task2 import area_rectangle, area_triangle, area_circle


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
