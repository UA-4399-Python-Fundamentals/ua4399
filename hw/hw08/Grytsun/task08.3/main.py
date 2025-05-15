from geometry import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {rectangle_area(a, b)}")
    elif choice == "2":
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {triangle_area(a, h)}")
    elif choice == "3":
        r = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {circle_area(r)}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()