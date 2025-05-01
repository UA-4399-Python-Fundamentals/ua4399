temperature_c = float(input("Enter the temperature in Celsius: "))

if temperature_c > -273.15:
    result = (temperature_c * 9/5) + 32
    print(f"{temperature_c}°C is equivalent to {result}°F")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")