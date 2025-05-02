import math

VALS = {
    "rectangle": ["length", "width"],
    "triangle": ["base", "height"],
    "circle": ["radius"]
}

def calculator(figure, first_num, second_num="0"):
    """
        Returns area of a given figure
        Args:
            figure (str): rectangle, circle or triangle
            first_num(str): base, length or radius, depending on the figure
            second_num(str): height, width or nothing, depending on the figure
    """
    if not first_num.isdigit() or not second_num.isdigit():
        return "Not a number"
    match figure:
        case "rectangle":
            return round(float(first_num) * float(second_num),2)
        case "triangle":
            return round(float(first_num) * float(second_num) / 2,2)
        case "circle":
            return round(math.pi * math.pow(float(first_num),2),2)
        case _:
            return f"The figure {figure} is not supported"