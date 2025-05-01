celsius = float(input ('Enter the temperature in celsius: '))
if celsius > -273.15:
    fahrenheit = (celsius*9/5)+32
    print ((f"{celsius}°C is equal to {fahrenheit}°F."))
if celsius < -273.15:
    print ('Temperature below absolute zero (-273.15°C)')
