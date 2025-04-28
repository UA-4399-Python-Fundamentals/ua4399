for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} парне і ділиться на 2")
    elif number % 2 != 0 and  number % 3 == 0:
        print(f"{number} - непарне і ділиться на 3")
    elif number % 2 != 0 and number % 3 != 0:
        print(f"{number} - не ділиться ні на 2 ні на 3")