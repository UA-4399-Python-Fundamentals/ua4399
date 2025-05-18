string = input(str("Введіть рядок: "))

def count_characters(string):
    """
    Ця функція підраховує кількість букв рядка.
    """

    result_dict = {}
    count = 0
    for character in string:
        if character in result_dict:
            result_dict[character] += 1
        else:
            result_dict[character] = 1
    return result_dict
result = count_characters(string)
print("Кількість букв рядка:", result)



