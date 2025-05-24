import area_formulas

def choose_a_shape(area_formulas):
    print("Choose a shape: ")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = area_formulas.area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")

    elif choice == 2:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = area_formulas.area_triangle(base, height)
        print(f"The area of the triangle is: {area}")

    elif choice == 3:
        radius = float(input("Enter the radius: "))
        area = area_formulas.area_circle(radius)
        print(f"The area of the circle is: {area}")

    else:
        print("Invalid choice. Please choose a valid shape.")

if __name__ == "__main__":
    choose_a_shape(area_formulas)
