from area import area_rectangle, area_triangle, area_circle

def choose_area():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print("Area of rectangle:", area_rectangle(length, width))

    elif choice == "2":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        print("Area of triangle:", area_triangle(base, height))

    elif choice == "3":
        radius = float(input("Enter the radius: "))
        print("Area of circle:", area_circle(radius))

    else:
        print("Invalid choice.")


choose_area()
