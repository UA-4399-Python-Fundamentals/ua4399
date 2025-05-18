# Task 1
def the_largest_number(num1, num2):
    """
    This function takes two numbers and returns the larger one.
    """
    return num1 if num1 > num2 else num2


# Task 2

def rectangle_area(length: float, width: float) -> float:
    """
    This function takes the length and width of a rectangle and returns its area.
    """
    return length * width


def triangle_area(length: float, width: float) -> float:
    """
    This function takes the base and height of a triangle and returns its area.
    """
    return (length * width) / 2


def circle_area(radius: float) -> float:
    """
    This function takes the radius of a circle and returns its area.
    """
    return 3.14 * (radius ** 2)


# Task 3

def number_of_characters(string: str) -> dict:
    """
    This function takes a string and returns a dictionary with the count of each character in the string.
    :param string: str: The input string.
    :return: dict: A dictionary with characters as keys and their counts as values.
    """
    return {i: string.count(i) for i in set(string.lower())}


def main():
    # Task 1
    print("Task 1")
    print(f"The largest number is: {the_largest_number(3, 4)}")

    # Task 2
    print("\nTask 2")
    figure = input("Enter the figure (rectangle, triangle, circle): ").strip().lower()

    if figure == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print(f"The area of the rectangle is: {rectangle_area(length, width)}")
    elif figure == "triangle":
        length = float(input("Enter the base: "))
        width = float(input("Enter the height: "))
        print(f"The area of the triangle is: {triangle_area(length, width)}")
    elif figure == "circle":
        radius = float(input("Enter the radius: "))
        print(f"The area of the circle is: {circle_area(radius)}")

    # Task 3
    print("\nTask 3")
    string = input("Enter a string: ")
    print(f"Number of characters: {number_of_characters(string)}")


if __name__ == "__main__":
    main()
