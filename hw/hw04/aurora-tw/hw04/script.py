temp_c = input("Enter the temperature in Celsius")

if float(temp_c) < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    result = (float(temp_c) * 9/5) + 32
    print(f"{temp_c}°C is equivalent to {result}°F")



