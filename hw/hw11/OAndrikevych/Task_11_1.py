class CustomAgeError(Exception):
    pass


def process_age(age):
    if age < 0:
        raise CustomAgeError("Age cannot be negative. Please enter a valid age.")

    return "even" if age % 2 == 0 else "odd"


def get_user_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid integer.")


try:
    user_age = get_user_age()
    result = process_age(user_age)
    print(f"Your age {user_age} is {result}.")
except CustomAgeError as e:
    print(f"Error: {e}")

print("End of program.")
