input_num = input('Give me the number, please ')

# Обрізаємо перші 4 символи
current_num = list(input_num)[:4]

# Перемножуємо цифри
product_num = int(current_num[0]) * int(current_num[1]) * int(current_num[2]) * int(current_num[3])
print("Product of digits:", product_num)

# Реверсуємо цифри і виводимо число
reverse_num = int(''.join(current_num[::-1]))
print("Reversed number:", reverse_num)

# Відсортовуємо цифри по зменшенню і виводимо результат
sorted_num = sorted(current_num, reverse=True)
print("Sorted digits (descending):", int(''.join(sorted_num)))
