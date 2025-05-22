# Task 1

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")


user_input = int(input("Enter your age: "))
check_age(user_input)


# Task 2

def day_of_week(num):
    if num == 1:
        return "Monday"
    if num == 2:
        return "Tuesday"
    if num == 3:
        return "Wednesday"
    if num == 4:
        return "Thursday"
    if num == 5:
        return "Friday"
    if num == 6:
        return "Saturday"
    if num == 7:
        return "Sunday"

    return "Invalid day number. Please enter a number between 1 and 7."

try:
    user_input = input("Enter a number (1-7) to get the day of the week: ")
    number = int(user_input)
    print(day_of_week(number))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
