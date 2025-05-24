from random import randint

print("Давай зіграємо в гру!")
print("Я загадала число від 1 до 100.")
print("Зможеш його вгадати?")
print("Я буду давати підказки, якщо ти не вгадаєш.")
print("В тебе є 10 спроб.")

play = input("Натисни 'Enter', щоб почати гру.")
number = randint(1, 100)

tentative = 0
while tentative < 10:
    tentative += 1
    print(f"\nСпроба номер {tentative}")
    try:
        user_number = int(input("Введи число від 1 до 100: "))
    except ValueError:
        print("Будь ласка, введіть ціле число!")
        tentative -= 1
        continue
    
    if user_number == number:
        print("Вітаю! Ти вгадав число!")
        break
    elif user_number < 1 or user_number > 100:
        print("Ти ввів число не в діапазоні від 1 до 100.")
        tentative -= 1
    elif user_number < number:
        print("Моє число більше.")
    else:  # user_number > number
        print("Моє число менше.")
if tentative == 10 and user_number != number:
    print(f"Спроби закінчилися. Ти не вгадав число.")
    print(f"Я загадала {number}.")
    
