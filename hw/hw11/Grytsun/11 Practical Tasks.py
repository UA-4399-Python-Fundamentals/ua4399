# 1 

def process_age(age):
    """Processes the entered age and determines if it is even or odd."""
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."


def main():
    """Main function to prompt the user and handle exceptions."""
    try:
        age = int(input("Enter your age: "))
        message = process_age(age)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

    # 2

def get_day_of_week(number):
    """Returns the day of the week corresponding to the given number."""
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if number in days:
        return days[number]
    else:
        raise ValueError("Invalid number. Please enter a number between 1 and 7.")


def main():
    """Main function to prompt the user and handle exceptions."""
    try:
        number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))
        day = get_day_of_week(number)
        print(f"The day of the week is: {day}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()  