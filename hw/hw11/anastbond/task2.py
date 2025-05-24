def process_number(number):
  if number < 1 or number > 7:
    raise ValueError('Enter a correct week number')
  days = {
      1: "Monday",
      2: "Tuesday",
      3: "Wednesday",
      4: "Thursday",
      5: "Friday",
      6: "Saturday",
      7: "Sunday"
  }
  return days[number]

def main():
    try:
      number = int(input('Enter the number'))
      result = process_number(number)
      print(f"Day of the week is {result}")
    except ValueError as e:
        if "correct week number" in str(e):
           print(e)
        else:
           print("Error: Please enter a numeric value")
