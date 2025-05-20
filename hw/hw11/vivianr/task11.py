#task1
def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

def main():
    try:
        age_input = input("Enter your age: ")
        age = int(age_input)
        result = process_age(age)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Unexpected error occurred.")

main()

#task2
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
    if number in days:
        return days[number]
    else:
        raise ValueError("Number must be between 1 and 7.")

def main():
    try:
        num_input = input("Enter a number (1–7): ")
        number = int(num_input)
        day = get_day_of_week(number)
        print(f"Day of the week: {day}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Invalid input.")

main()
