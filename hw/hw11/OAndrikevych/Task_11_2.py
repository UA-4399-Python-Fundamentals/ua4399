def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(number, "Invalid number. Please enter a number between 1 and 7.")

def read_int():
    while True:
        try:
            number = int(input("Enter a number (1-7): "))
            return number
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid integer.")

number = read_int()
day_of_week = get_day_of_week(number)
print(f"Number {number} corresponds to the next day of the week: {day_of_week}")
print("End of program")
