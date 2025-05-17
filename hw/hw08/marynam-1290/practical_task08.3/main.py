from area import shapes


def calculate():

    user_shape = input("Please enter your shape to calculate its area: ").lower()

    if user_shape == "rectangle":
        width = input("Enter width: ")
        length = input("Enter length: ")
        area = shapes.area_rectangle(width, length)
        print(f"Area of rectangle: {area}")
    elif user_shape == "triangle":
        height = input("Enter height: ")
        base = input("Enter base: ")
        area = shapes.area_triangle(height, base)
        print(f"Area of triangle: {area}")
    elif user_shape == "circle":
        radius = input("Enter radius: ")
        area = shapes.area_circle(radius)
        print(f"Area of circle: {area}")


calculate()
