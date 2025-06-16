import math

def largest(x, y):
    '''This function returns the largest number of two numbers'''
    return max(x, y)

def number_of_characters(input_string):
    '''Calculates number in input string'''
    char_counts = {}
    for character in input_string:
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    print(char_counts)

def triangle_area():
    '''Calculates triangle area'''
    while True:
        print("Enter numeric values:")
        height = input("Height value: ")
        base = input("Base value: ")
        if height.isnumeric() and base.isnumeric():
            area = float(height) * float(base) / 2
            return print(f"Triangle area: {round(area, 2)}")
        else:
            print("Error! Please, enter numerical values")

def rectangle_area():
    '''Calculates rectangle area'''
    while True:
        print("Enter numeric values:")
        length = input("Length value: ")
        width = input("Width value: ")
        if length.isnumeric() and width.isnumeric():
            area = float(length) * float(width)
            return print(f"Rectangle area: {round(area, 2)}")
        else:
            print("Error! Please, enter numerical values")

def circle_area():
    '''Calculates circle area'''
    while True:
        print("Enter numeric values:")
        radius = input("Radius value: ")
        if radius.isnumeric():
            area = (float(radius) ** 2) * math.pi
            return print(f"Circle area: {round(area, 2)}")
        else:
            print("Error! Please, enter numerical values")

def main():
    print(
        "Which area you want to calculate?\n" \
        "1. Triangle\n" \
        "2. Rectangle\n" \
        "3. Circle\n"
        "4. Exit\n"
    )
    while True:
        user_choice = input("Enter number 1-4: ")
        match user_choice:
            case "1":
                triangle_area()
            case "2":
                rectangle_area()
            case "3":
                circle_area()
            case "4":
                print("Bye")
                break
            case _:
                print("Wrong value")

main()