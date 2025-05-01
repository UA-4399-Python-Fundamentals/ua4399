def c_to_f ():
  celsius = float(input("Enter the temperature in Celsius."))
  if celsius < -273.15:
    return "Error!"
  fahrenheit = (celsius * 9/5) + 32
  message = f"The temperature in Celsius is {celsius}. The temperature in Fahrenheit is {fahrenheit}"
  return message
