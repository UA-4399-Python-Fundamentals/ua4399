# task_processor.py

def process_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    except ValueError as e:
        print(f"Invalid input: {e}")
# Task 2: Get the day of the week based on a number
def get_day_of_week():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
#     # Prompt user for input
    try:
        number = int(input("Enter a number (1-7) to get the day of the week: "))
        print(f"The day is: {days[number]}")
    except ValueError:
        print("Invalid input: Please enter a number.")
    except KeyError:
        print("Invalid number: Must be between 1 and 7.")
#     # Handle invalid input
if __name__ == "__main__":
    print("Task 1:")
    process_age()
    print("\nTask 2:")
    get_day_of_week()
#     # Get the day of the week based on the number