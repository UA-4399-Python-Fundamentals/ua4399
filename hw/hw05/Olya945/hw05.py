# first task

print("\nfirst task")

#Вводимо числа
input_string = input("Введіть цілі числа через пробіл: ")

# Перетворюємо рядок у список цілих чисел
numbers = list(map(int, input_string.split()))

# Перетворюємо список цілих чисел у дробові числа та виводимо результат
float_numbers = list(map(float, numbers))
print("Список дробових чисел:", float_numbers)
