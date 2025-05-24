import random

number = random.randint(1, 100)
tries = 10

for i in range(1, tries + 1):
    try:
        a = int(input("Введіть число: "))
        if a < number:
            print("Дуже мало!")
        elif a > number:
            print("Дуже багато!")
        else:
            print("Вітаю! Ви вгадали число!")
            break
    except ValueError:
        print("Введіть ціле число!")
else:
    print(f"Ви викорситали всі {tries} спроб. Число було {number}")



