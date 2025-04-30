# Temperature Converter
temp_cels = float(input("Enter the temperature in Celsius: "))

25# Check if the temperature is below absolute zero
if float(temp_cels) < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
else:
        fahrenheit = (temp_cels * 9/5) + 32
        print (f"{temp_cels}°C is equivalent to {fahrenheit}°F")