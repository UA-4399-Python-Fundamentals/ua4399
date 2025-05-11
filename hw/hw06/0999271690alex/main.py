for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} – парне та ділиться на 2")
    elif num % 2 != 0 and num % 3 == 0:
        print(f"{num} – непарне та ділиться на 3")
    elif num % 2 != 0 and num % 3 != 0:
        print(f"{num} – не ділиться ні на 2, ні на 3")



while True:
    login = input("Введіть логін: ")
    if login == "First":
        print("Вітаємо, користувачу!")
        break
    else:
        print("Невірний логін. Спробуйте ще раз.")

