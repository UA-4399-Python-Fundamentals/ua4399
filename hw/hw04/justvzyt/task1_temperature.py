celsius = float(input("Enter the temperature in Celsius: "))

if celsius < -273.15:
    print("Temperature below absolute zero (-273.15)")
else:
    far = celsius*1.8+32
    print(f"{celsius}*C is equivalent to {far}*F")