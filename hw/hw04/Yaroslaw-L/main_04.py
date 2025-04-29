#Temperature converter
c = float(input("Celsuis-Fahrenheit temperature converter. \nSupported symbols are 0-9,. \nType temperature in Celsius: ").replace(",", "."))
f = (c * 9/5) + 32
ok = -273.15

if c >= ok:
    print(f"{c}°C is equivalent to {f}°F")
elif c < ok:
    print("That temperature is below the absolute zero and don't exist in the Universe.\n Reload program and type correct temperature in Celsius.")
else:
    print(f"{type(c)}")