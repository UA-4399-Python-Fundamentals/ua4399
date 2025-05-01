temperature = float (input("Enter temperature in Celsius: "))
# Перевіряємо, чи температура нижча за абсолютний нуль
if temperature < -273.15:
    print("Error: Temperature below absolute zero! (-273.15°C)")
else:
    # Конвертуємо температуру в Фаренгейти
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equivalent to {fahrenheit}°F")
    