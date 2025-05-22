import area_functions

choice = input("Enter your choice (rectangle/triangle/circle): ")

if choice == "rectangle":
    # Get input from user
    w = float(input("Enter the rectangle width (integer or float): "))
    l = float(input("Enter the rectangle length (integer or float): "))
    print(area_functions.rectangle_area(w, l))
elif choice == "triangle":
    h = float(input("Enter the triangle height (integer or float): "))
    b = float(input("Enter the triangle base (integer or float): "))
    print(area_functions.triangle_area(h, b))
elif choice == "circle":
    r = float(input("Enter the circle radius (integer or float): "))
    print(area_functions.circle_area(r))
else:
    print("Invalid choice.")