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

    if number < 1 or number > 7:
        raise ValueError("Number must be between 1 and 7.")
    
    return days[number]

def main():
    try:
        number = int(input("Enter a number between 1 and 7: "))
        day = get_day_of_week(number)
        print(f"The day of the week is: {day}")
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter a valid integer.")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
    


