is_running = True

while is_running == True:
    try:
        temp = float(input("Enter the temperature in Celsius: "))
        if temp >= -273.15:
            far = (temp * 9/5) + 32
            print(f"The temperature in F is: {far}F")
            is_running = False
        elif temp < -273.15:
            print("ERROR! Enter the number higher than -273.15")
        else:
            print("ERROR! Unknown error")
    except ValueError:
        print("ERROR! Enter the number please!")