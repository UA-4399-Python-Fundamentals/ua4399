def is_int(val):
    try:
        int(val)
        return True
    except:
        return False

def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

def is_number(val):
    if is_float(val) or is_int(val):
        return True
    else:
        return False


def calc_fahrenheit(value):
    if not is_number(value):
        print("Not a number")
    elif float(value) < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
    else:
        result = (float(value) * 9/5) + 32
        print(f"{value}°C is equivalent to {result}°F")


temp_c = input("Enter the temperature in Celsius")
calc_fahrenheit(temp_c)
