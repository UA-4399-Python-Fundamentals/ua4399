# 1
celsius = float(input("Please, enter a temperature in Celsius: "))
farenheit = (celsius * 9 / 5) + 32

if celsius > -273.15:
    print(f"{celsius}°C is equivalent to {farenheit}°F")
else:
    print("Temperature below absolute zero")
