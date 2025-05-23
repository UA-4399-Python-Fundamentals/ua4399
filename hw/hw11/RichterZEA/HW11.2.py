def day_by_number(day_input):
    try:
        day_number = int(day_input)
        days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        if day_number in days:
            print(f"The day of the week is: {days[day_number]}")
        else:
            print("Please enter a number from 1 to 7.")
    except ValueError:
        print("Error: Input is not a number.")
day_input = input("Enter a number from 1 to 7: ")
day_by_number(day_input)