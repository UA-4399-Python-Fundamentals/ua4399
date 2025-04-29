def get_valid_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number (e.g., 36.6)")

def temperature_converter(temperature_in_celsius):
    temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
    if temperature_in_celsius < -273.15:
        print("Error: Temperature below absolute zero (-273.15)")
    else:
        print(f"{temperature_in_celsius}°C is equivalent to {temperature_in_fahrenheit}°F")

user_input = get_valid_float("Enter the temperature in Celsius: ")
temperature_converter(user_input)