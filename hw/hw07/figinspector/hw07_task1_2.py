def area_rectangle(a, b):
    return a * b


def area_triangle(a, h):
    return 0.5 * a * h


def area_circle(r):
    return 3.1416 * r**2


def print_condition():
    return input(
        "Defines the shape for calculation, 'Rectangle', 'Triangle' or 'Circle': "
    )


def calc_area(data):
    """
    Calculates the area of a rectangle, triangle, or circle.
    """

    result = lambda shape, area: f"Area of {shape.title()} = {area} parrots!"

    if data.lower() == "rectangle":
        a, b = int(input("enter length: ")), int(input("enter width: "))
        answer = result(data, area_rectangle(a, b))

    elif data.lower() == "triangle":
        a, h = int(input("enter base: ")), int(input("enter height: "))
        answer = result(data, area_triangle(a, h))

    elif data.lower() == "circle":
        r = int(input("enter radius: "))
        answer = result(data, area_circle(r))

    else:
        answer = result(data, "Wrong parameter")

    print(answer)


calc_area(print_condition())
