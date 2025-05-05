from calculator import *


def init():
    """
    Asks the user for the figure to calculate area, then first and second(if needed) value
    Pass them to calculator() function
    """

    figure = input("Enter figure to calculate area: rectangle, triangle or circle: ")
    if figure not in VALS:
        return f"The figure {figure} is not supported"
    first_num = input(f"Please enter the {VALS[figure][0]} ")
    second_num = input(f"Please enter the {VALS[figure][1]} ") if not figure == "circle" else "0"
    result = calculator(figure, first_num, second_num)

    if result == "Not a number":
        return "Only digits supported"
    else:
        return f"The area of a {figure} based on its {" and ".join(VALS[figure])} is {result}"

print(init())


