from areas import rectangle_area, triangle_area, circle_area

def main():
    print("Choose figure to calculate area:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        print("Area of rectangle:", rectangle_area(a, b))

    elif choice == "2":
        a = float(input("Enter base a: "))
        h = float(input("Enter height h: "))
        print("Area of triangle:", triangle_area(a, h))

    elif choice == "3":
        r = float(input("Enter radius r: "))
        print("Area of circle:", circle_area(r))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
