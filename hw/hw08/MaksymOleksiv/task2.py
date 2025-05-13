import re

def is_valid_pass(password: str) -> bool:
    is_lovercase = bool(re.search(r'[a-z]', password))
    is_uppercase = bool(re.search(r'[A-Z]', password))
    is_digit = bool(re.search(r'[0-9]', password))
    is_special = bool(re.search(r'[@#$%^&+=]', password))
    is_min_length = len(password) >= 6
    is_max_length = len(password) <= 16

    return is_lovercase and is_uppercase and is_digit and is_special and is_min_length and is_max_length

password = input("Enter a password: ")

if is_valid_pass(password):
    print("Valid password")
else:
    print("Invalid password")