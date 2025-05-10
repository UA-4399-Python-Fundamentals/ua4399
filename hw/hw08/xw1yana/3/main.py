import area

def main():
    choice = input("Choose the shape to calculate the area: rectangle/triangle/circle ").lower()

    if choice == 'rectangle':
        a = float(input("Enter length (a): "))
        b = float(input("Enter width (b): "))
        print("Area of rectangle:", area.area_rectangle(a, b))

    elif choice == 'triangle':
        h = float(input("Enter height (h): "))
        a = float(input("Enter base (a): "))
        print("Area of triangle:", area.area_triangle(h, a))

    elif choice == 'circle':
        r = float(input("Enter radius (r): "))
        print("Area of circle:", area.area_circle(r))

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
