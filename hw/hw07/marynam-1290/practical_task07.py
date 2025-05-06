# 1
def compare(num1, num2):
    """Returns largest number of two numbers"""
    if num1 > num2:
        return num1
    else:
        return num2


print(compare(4, 5))

# 2


def area_rectangle(length, width):
    length = float(length)
    width = float(width)
    return length * width


def area_triangle(base, height):
    base = float(base)
    height = float(height)
    return 0.5 * base * height


def area_circle(radius):
    radius = float(radius)
    Pi = 3.14
    return float(Pi * radius**2)


def main():
    users_choice = input("Choose a shape to calculate its area: ").lower()

    if users_choice == "rectangle":
        length = input("Enter the length of rectangle: ")
        width = input("Enter the width of rectangle: ")
        area = area_rectangle(length, width)
        print(f"Area of rectangle: {area:.2f}")
    elif users_choice == "triangle":
        base = input("Enter the base of triangle: ")
        height = input("Enter the height of triangle: ")
        area = area_triangle(base, height)
        print(f"Area of triangle: {area:.2f}")
    elif users_choice == "circle":
        radius = float(input("Enter the radius of circle: "))
        area = area_circle(radius)
        print(f"Area of circle: {area:.2f}")


main()


# 3
# Write a function that calculates the number of characters included in given string
# Input: “hello”
# Output: {“h”:1, “e”:1, “l”:2, “o”:1}


def count_char(word):
    char_pull = {}

    for character in word:
        if character in char_pull:
            char_pull[character] += 1
        else:
            char_pull[character] = 1

    print(repr(char_pull))


word = input("Enter your word: ")
count_char(word)
