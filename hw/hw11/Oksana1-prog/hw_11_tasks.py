#Task 1.
#Write a program that prompts the user to enter their age
class NegativeAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    if age % 2 == 0:
        print("The age is even.")
    else:
        print("The age is odd.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except NegativeAgeError as e:
    print(f"Exception: {e}")
except ValueError:
    print("Invalid input! Please enter an integer.")
#Task 2
# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week
def day_of_week(number):
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
        print(days[number])
    else:
        print("Invalid number! Please enter a number between 1 and 7.")

try:
    num = int(input("Enter a number (1-7): "))
    day_of_week(num)
except ValueError:
    print("Invalid input! Please enter a numeric value.")