def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")

# Master code
try:
    age_input = int(input("Enter your age: "))
    process_age(age_input)
except ValueError as e:
    print("Error:", e)

# Task 2

def day_of_week(num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if num not in days:
        raise ValueError("Invalid number! Enter a number from 1 to 7.")
    return days[num]

# Master code
try:
    num_input = int(input("Enter a number (1–7) to get the day of the week: "))
    print("Day of the week:", day_of_week(num_input))
except ValueError as e:
    print("Error:", e)
