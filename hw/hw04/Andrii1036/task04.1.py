'''Homework 04 task1 '''

# "Temperature Converter"
# Write a Python program that prompts the user to enter a temperature in Celsius and then
# converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. Your program should then
# print out the converted temperature in Fahrenheit.
# However, if the user enters a temperature below -273.15°C (the lowest possible
# temperature in the universe, also known as absolute zero), your program should print an
# error message instead of attempting to convert the temperature.
# Note: You can assume that the user will enter a valid input (a number for the temperature in Celsius).
# Example output:
# Enter the temperature in Celsius: 25
# 25°C is equivalent to 77°F
# Example output (if the user enters a temperature below absolute zero):
# Enter the temperature in Celsius: -300
# Error: Temperature below absolute zero (-273.15°C)

# Declaring variables and constant
temperature_celsium = None
ABSOLUTE_ZERO = -273.15

# Check for unwanted characters
def has_unwanted_characters(number):
    for item in number:
        if item not in '0123456789.,-,-':
            return False                
    return True                        

# Convertation value
def convertation_to_fahrenheit(celsium):
    fahrenheit = (celsium * 9/5) + 32
    print(f"{temperature_celsium}°C is equivalent to {fahrenheit}°F")

# Input validation
while temperature_celsium is None:
    celsium = input('Enter the temperature in Celsius: ')
    if has_unwanted_characters(celsium):
        if ',' in celsium:
            celsium = celsium.replace(',','.')
        temperature_celsium = float(celsium)
    else:
        print('Please enter a valid temperature using only numeric characters.')

# Display results
if temperature_celsium < ABSOLUTE_ZERO:
    print("Temperature is below absolute zero!")
else:
    convertation_to_fahrenheit(temperature_celsium)
