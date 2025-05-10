################################################ 1 ################################################

# def larger_number(num_1: int, num_2: int) -> str:
#     """
#     Takes two values and returns a message with the greater one.

#     Args: First number
#           Second number

#     Returns: Greater value, or reports that they are equal.
#     """
#     if num_1 > num_2:
#         return f"The greater number is: {num_1}"
#     elif num_2 > num_1:
#         return f"The greater number is: {num_2}"
#     else:
#         return "The numbers are equal."

# a = int(input("Enter first number: "))
# b = int(input("Enter secon number: "))

# print(larger_number(a, b))


################################################ 2 ################################################

# import math
# choose_figure = input("Choose figure: (r)ectangle, (t)riangle, (c)ircle: ")


# def rectangular_area(side_a: float, side_b: float) -> float:
#     """
#     Calculates the area of a rectangle

#     Args: Length of one side of the rectangle.
#           Length of the adjacent side.

#     Returns: The area of the rectangle.
#     """
#     return side_a * side_b

# def triangle_area(base_a: float, height_h: float) -> float:
#     """
#     Calculates the area of a triangle.

#     Args: Length of the base of the triangle.
#           Height of the triangle.

#     Returns: The area of the triangle.
#     """
#     return 1/2 * base_a * height_h

# def circle_area(radius_circle_r: float, π = math.pi) -> float:
#     """
#     Calculates the area of a circle.

#     Args: Radius of the circle.

#     Returns: The area of the circle, rounded to 2 decimal places.
#     """
#     return round((π * radius_circle_r**2), 2)


# def area_calculation(figure: str):
#     """
#     Prompts for shape dimensions based on the chosen figure, then calculates and returns its area.

#     Args: The type of figure ('r', 't', or 'c').

#     Returns: The calculated area or an error message if the input is invalid.
#     """
#     if figure == 'r':
#         length_rectangular = float(input('Length: '))
#         float_rectangular = float(input('Float: '))
#         return rectangular_area(length_rectangular, float_rectangular)
    
#     elif figure == 't':
#         base = float(input('Base: '))
#         height = float(input('Height: '))
#         return triangle_area(base, height)
    
#     elif figure == 'c':
#         radius = float(input('Radius: '))
#         return circle_area(radius)
    
#     else:
#         return "Wrong figure!"


# print(area_calculation(choose_figure))


################################################ 3 ################################################

# word_str = input("Enter any word (but the task recommends ‘hello’): ")

# def count_chars(argument: str) -> dict:
#     """
#     Counts the number of occurrences of each character in the input string.

#     Args: The string to analyze.

#     Returns: A dictionary where keys are characters and values are their frequencies.
#     """
#     char_freq = {}
#     for sign in argument:
#         if sign in char_freq:
#             char_freq[sign] += 1
#         else:
#             char_freq[sign] = 1
#     return char_freq

# print(count_chars(word_str))
