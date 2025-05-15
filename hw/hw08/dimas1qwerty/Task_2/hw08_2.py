import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[$#@]", password)

    return all([has_lower, has_upper, has_digit, has_special])

user_password = input("Enter your password: ")

if is_valid_password(user_password):
    print("Password is valid!")
else:
    print("Password is invalid!")
