def celcius_to_fahrenheit(celsius):
    if celsius >= -273.15:
        print(f"Temperature in Fahrenheit: {round(celsius * 9/5 + 32, 2)}°F")
    else:
        print("Temperature cannot be below absolute zero -273.15°C")

input_celsius = float(input("Enter temperature in Celsius: "))
celcius_to_fahrenheit(input_celsius)