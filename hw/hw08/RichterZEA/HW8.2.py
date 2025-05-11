import re

def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'
    return bool(re.match(pattern, password))
user_password = input("Enter your password: ")
if is_valid_password(user_password):
    print("Password is valid")
else:
    print("Password is invalid")