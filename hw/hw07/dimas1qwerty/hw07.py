#======task 1======
def max_of_two(a: float, b: float) -> float:
    """
    Повертає більше з двох чисел.
    a (float) - перше число, b (float) - друге число
    Returns:
    найбільше число
    """
    return a if a > b else b

print("Максимальне число:", max_of_two(10, 20))

#======task 2======
def rectangle_area(l, w):
    area = l * w
    return area
def triangle_area(b, h):
    area = 1/2 * b * h
    return area
def circle_area(r):
    area = 3.14 * r**2
    return area

formula = input("What do you want to calculate: ").lower()
if formula == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print(rectangle_area(l, w))
elif formula == "triangle":
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    print(triangle_area(b, h))
elif formula == "circle":
    r = float(input("Enter radius: "))
    print(circle_area(r))
else:
    print("Incorrect name")
#======task 3======
def count_characters(s: str) -> dict:
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result


text = "hello"
print(count_characters(text))
