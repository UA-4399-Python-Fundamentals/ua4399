try:
    x =float(input("Введіть температуру в Цельсіях: "))
    if x < -273.15:
        print("Помилка: температура нижче абсолютного нуля (-273.15°C)")
    else:
        far = (x * 9/5) + 32
        print(f"{x}°C є рівне до {far}°F")
except ValueError:
    print("Ви ввели не число!")
