from modules import compute_rectangle, compute_triangle, compute_circle


def ask_data(text):
    return int(input(f"{text}: "))


def compute_area():
    """
    Calculates the area of a rectangle, triangle, or circle.
    """
    message = "Defines the shape for calculation, 'Rectangle', 'Triangle' or 'Circle': "
    shape = input(message)
    result = lambda shape, area: f"Area of {shape.title()} = {area} parrots!"
    answer = None

    match shape.lower():
        case "rectangle":
            a, b = ask_data('Enter side A'), ask_data('Enter side B')
            answer = result(shape, compute_rectangle(a, b))
        case "triangle":
            b, h = ask_data("Enter base"), ask_data("Enter height")
            answer = result(shape, compute_triangle(b, h))
        case "circle":
            r = ask_data("Enter radius")
            answer = result(shape, compute_circle(r))
        case _:
            answer = f"\"{shape}\" — undefined figure"

    print(answer)


compute_area()

