# 03-1
text = """
Sparse is better than dense.
Readability counts.
If the implementation is easy to explain, it may be a good idea.
"""
# Вивід тексту
print(f"Count 'better' == {text.count("better")}")
print(f"Count 'never == {text.count("never")}")
print(f"Count 'is' == {text.count("is")}")

# Вивід uppercase
text_upper = text.upper()
print("\nUppercase:\n", text_upper)

# Заміна "i" на "&"
text_replaced = text.replace("i", "&")
print("\nWith replaced 'i':\n", text_replaced)


# 03-2
number = int(input("Your number: "))

# Добуток цифр
digits = [int(d) for d in str(number)]
product = 1
for d in digits:
    product *= d
print("Product of digits: ", product)

# У зворотному порядку
reversed_number = int(str(number)[::-1])
print("Reversed number: ", reversed_number)

# У порядку зростання
sorted_number = sorted(digits)
print("Sorted number: ", sorted_number)

#03-3
# Заміна двох значень
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Поміняємо значення місцями без використання третьої змінної
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

