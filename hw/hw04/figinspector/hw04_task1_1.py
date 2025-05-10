c = float((input("Enter a temperature in Celsius for convert to Fahrenheit: ")))

if c < -273.15:
    print("Error: temperature below absolute zero, -273.15!")
else:
    f = (c * 9 / 5) + 32
    print(f"{c}°C = {f}°F")
