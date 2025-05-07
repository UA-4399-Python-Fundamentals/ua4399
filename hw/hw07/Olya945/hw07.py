    #task 1

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

def largest_number(a, b):
    """
    Ця функція повертає найбільше з двох чисел.
    a - перше число
    b - друге число
    """

    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Числа однакові"

result = largest_number(a, b)
print("Результат:", result)
    