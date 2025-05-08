import re

def is_valid_password(password):
    if len(password) < 6 and len(password) > 16:
        return False
    elif not re.search(r"[a-z]", password):
        return False
    elif not re.search(r"[A-Z]", password):
        return False
    elif not re.search(r"[0-9]", password):
        return False
    elif not re.search(r"[$#@]", password):
        return False

password = input("Enter your password: ")

if is_valid_password(password):
    print("Valid password.")
else:
    print("Invalid password.")
