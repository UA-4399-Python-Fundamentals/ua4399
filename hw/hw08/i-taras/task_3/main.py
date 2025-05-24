from areas import rectangular_area, triangle_area, circle_area



def area_calculation(figure: str):
    """
    Prompts for shape dimensions based on the chosen figure, then calculates and returns its area.

    Args: The type of figure ('r', 't', or 'c').

    Returns: The calculated area or an error message if the input is invalid.
    """
    if figure == 'r':
        length_rectangular = float(input('Length: '))
        float_rectangular = float(input('Float: '))
        return rectangular_area(length_rectangular, float_rectangular)
    
    elif figure == 't':
        base = float(input('Base: '))
        height = float(input('Height: '))
        return triangle_area(base, height)
    
    elif figure == 'c':
        radius = float(input('Radius: '))
        return circle_area(radius)
    
    else:
        return "Wrong figure!"
    
choose_figure = input("Choose figure: (r)ectangle, (t)riangle, (c)ircle: ").lower()
print(area_calculation(choose_figure))