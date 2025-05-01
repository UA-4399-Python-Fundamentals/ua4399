#Prompt the user to enter the temperature in Celsius and then convert it to Fahrenheit.
#The formula for conversion is F = C * 9/5 + 32
#Print the converted temperature in Fahrenheit.
print("Enter the temperature in Celsius:")
celsius = float(input())
fahrenheit = celsius * 9 / 5 + 32
if celsius > -273.15:
    print("The temperature in Fahrenheit is:", fahrenheit)
else:
    print("Error: Temperature below absolute zero!")