from area import rectangle_area, circle_area, triangle_area

print("Choose a shape to calculate the area:")
print("1. Rectangle")
print("2. Circle")
print("3. Triangle")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == 2:
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area}")
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is: {area}")
