##task1
def largest_number(n1, n2):
    '''This function compares two numbers and returns the largest one'''
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return "One number should be bigger than another"

print(largest_number(500, 3))

##task2
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

##task3
def char_num(word):
    result = {}
    for char in word:
        if char not in result:
            result[char] = 1
        else:
            result[char] = result[char] + 1
    return result

print(char_num("hello"))