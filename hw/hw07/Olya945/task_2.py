import math

def rectangle_area(length, width):
    """
    Ця функція обчислює площу прямокутника.
    length - довжина прямокутника
    width - ширина прямокутника
    """
    return length * width

def triangle_area(base, height):
    """
    Ця функція обчислює площу трикутника.
    base - основа трикутника
    height - висота трикутника
    """
    return 0.5 * base * height

def circle_area(radius):

    """
    Ця функція обчислює площу кола.
    radius - радіус кола
    """
    return math.pi * radius ** 2

def calculate():
    """
    Ця функція запитує у користувача площу якої фігури він хоче обчислити.
    Потім запитує необхідні параметри та обчислює площу шляхом виклику відповідної функції.
    """
    print("Виберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Введіть номер фігури (1/2/3): ")
    if choice == '1':
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        area = rectangle_area(length, width)
        print("Площа прямокутника:", area)
    elif choice == '2':
        base = float(input("Введіть довжину основи трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        area = triangle_area(base, height)
        print("Площа трикутника:", area)
    elif choice == '3':
        radius = float(input("Введіть радіус кола: "))
        area = circle_area(radius)
        print("Площа кола:", area)
    else:
        print("Помилка вибору")

calculate()