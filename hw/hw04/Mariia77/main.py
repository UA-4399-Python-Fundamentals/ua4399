temp = float(input("Enter a temperature in Celsius: "))
if float(temp) < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    F = (temp * 9 / 5) + 32
    print(f"{temp}°C is equivalent to {F}°F")
