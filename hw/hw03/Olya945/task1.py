# first task

print("\nfirst task")

# Записуємо текст як багаторядковий рядок:
text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# Рахуємо та виводимо кількість слів "better", "never" та "is":
count_better = text.count("better")
count_never = text.count("never")
count_is = text.count("is")

print("\nКількість 'better':", count_better)
print("Кількість 'never':", count_never)
print("Кількість 'is':", count_is)

# Виводимо текст у верхньому регістрі та з заміненими 'i' на '&':
text_upper = text.upper()
print("\nТекст у верхньому регістрі:\n", text_upper)

text_replaced = text.replace("i", "&")
print("Текст із заміненими 'i' на '&':\n", text_replaced)


#second task

print("\nsecond task\n")

# Просимо ввести число:
number = input("Введіть чотиризначне натуральне число: ")

# Перевіряємо чи є введені дані чотиризначним натуральним числом;
# Якщо так, то виводимо добуток цифр, число у зворотному порядку та відсортовані цифри;
# Якщо ні, то виводимо повідомлення про помилку:
if number.isdigit() and len(number) == 4:
    a, b, c, d = map(int, number)
    result = a * b * c * d
    print("\nДобуток цифр: ", result)

    reversed_number = number[::-1]
    print("Число у зворотному порядку: ", reversed_number)

    sorted_digits = ''.join(sorted(number))
    print("Відсортовані цифри: ", sorted_digits)

else:
    print("Помилка: потрібно ввести чотиризначне натуральне число!\n")


#third task

print("\nthird task\n")

# Задаємо змінні a та b:
a = 15
b = 22

print(f"Початкові значення: a = {a}, b = {b}")

# Виконуємо обмін значеннями:
a, b = b, a

print(f"Значення після обміну: a = {a}, b = {b}")









