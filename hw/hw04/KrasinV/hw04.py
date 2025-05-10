#Temp Converter
temp_input = input("Enter temperature in Celsius: ")
tempc = int(temp_input)
if tempc < -273.15:
    print("Temperature is below absolute zero (-273.15C)")
else:
    tempfff = (tempc*9/5)+32
    print(f"{tempc}C is equavalent to {tempfff}F")