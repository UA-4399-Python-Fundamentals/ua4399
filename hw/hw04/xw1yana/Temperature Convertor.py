a = float(input("Введіть значення температури в Цельсіях: "))

if a < -273.15:
    print("Помилка: Ви ввели температуру нижче абсолютного нуля.")
else:
    f = (a * 9/5) + 32
    print(f"{a}°С дорівнює {f}°F")