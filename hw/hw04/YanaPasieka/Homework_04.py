# Інпут температури
celsius = float(input("Enter the temperature in Celsius: "))

# Чекаємо, чи є температура нижчою за абсолютний нуль
if celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    # Виконуємо формулу
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")
