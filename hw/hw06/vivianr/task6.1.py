for i in range(1, 10):
    if i % 2 == 0:
        print(f"Even and divisible by 2: {i}")
    elif i % 2 !=0 and i % 3 == 0:
        print(f"Odd and divisible by 3: {i}")
    elif i % 2 != 0 and i % 3 != 0:
        print(f"Odd and not divisible by 3: {i}")