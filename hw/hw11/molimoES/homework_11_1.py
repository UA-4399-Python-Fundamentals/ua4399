# Homework Lesson 11

# ///////////////////////////////////////////////////////////////////
# 1 - Check age
print("Subtask 1")

def process_age_input(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        return f"The age is even: {age}"
    else:
        return f"The age is odd: {age}"

try:
    user_input = input("Please enter your age: ")
    age = int(user_input)
    message = process_age_input(age)
    print(message)
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# ///////////////////////////////////////////////////////////////////
# 2 - Analyze the number
print("Subtask 2")

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
        return f"The day of the week is: {days[number]}"
    else:
        raise ValueError("Invalid number. Please enter a number between 1 and 7.")


try:
    user_input = input("Enter a number (1-7) to get the day of the week: ")
    number = int(user_input)
    result = get_day_of_week(number)
    print(result)
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")