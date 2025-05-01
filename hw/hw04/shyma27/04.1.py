c = input("Enter the temperature in Celsius: ")

if float(c) < -273.15:
    print("Error: Temperature is below absolute zero (-273.15\u00B0C)")
#check if user entered float
elif "." in c:
    f = ((float(c) * 9/5)) + 32
    print(round(f, 2))
else:
    f = int(((float(c) * 9/5)) + 32)
    print(f)