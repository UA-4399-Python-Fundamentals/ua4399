celsius_in = float(input("Enter temperature in Celsius: "))
ABSOLUTE_ZERO = -273.15

if celsius_in < ABSOLUTE_ZERO:
    print("Error: Temperature below absolute zero (-273.15C)")
else:
    fahrenheit = celsius_in * 1.8 + 32
    print(f"{celsius_in}C is equivalent to {fahrenheit}F")