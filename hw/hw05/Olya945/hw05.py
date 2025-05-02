# first task

print("\nfirst task")

#Вводимо числа
input_string = input("Введіть цілі числа через пробіл: ")

# Перетворюємо рядок у список цілих чисел
numbers = list(map(int, input_string.split()))

# Перетворюємо список цілих чисел у дробові числа та виводимо результат
float_numbers = list(map(float, numbers))
print("Список дробових чисел:", float_numbers)


#second task

print("\nsecond task\n")

# Вводимо число n
n = int(input("Введіть ціле число n: "))

# Початкові числа послідовності
a, b = 0, 1
    
# Виводимо перше число
print(a, end=' ')
    
# Поки наступне число не перевищує n
while b <= n:
    print(b, end=' ')
    # Обчислюємо наступне число Фібоначчі
    a, b = b, a + b

print(f"Числа Фібоначчі до {n}:")


#third task
print("\nthird task\n")

def factorial(n):
     
    if n == 0 or n == 1:
        return 1
    
    if n < 0:
        return "Факторіал не визначений для від'ємних чисел"
    
    else:
        return n * factorial(n - 1)

# Вводимо число n
n = int(input("Введіть ціле число n: "))

# Обчислюємо факторіал
result = factorial(n)

# Виводимо результат
print(f"Факторіал числа {n} дорівнює {result}")

