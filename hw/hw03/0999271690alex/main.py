zen = "Beautiful is better than ugly"

# Підрахунок кількості слів
print("better:", zen.count("better"))
print("never:", zen.count("never"))
print("is:", zen.count("is"))

# Вивід у верхньому регістрі
zen_upper = zen.upper()
print("\nUppercase:\n", zen_upper)

# Заміна символу "i" на "&"
zen_replaced = zen.replace("i", "&")
print("\nWith replaced 'i':\n", zen_replaced)

number = 1234

# Добуток цифр
digits = [int(d) for d in str(number)]
product = 1
for d in digits:
    product *= d
print("Product of digits:", product)

# У зворотному порядку
reversed_number = int(str(number)[::-1])
print("Reversed number:", reversed_number)

# Сортування по зростанню
sorted_digits = sorted(digits)
print("Digits in ascending order:", sorted_digits)

a = 5
b = 10

print("Before swap: a =", a, ", b =", b)

# Обмін
a, b = b, a

print("After swap: a =", a, ", b =", b)
