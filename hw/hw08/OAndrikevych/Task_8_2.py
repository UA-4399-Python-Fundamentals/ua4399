print("Task 08.2")
# Task2. Write a Python program to check the validity of a password

import re

def pass_check(passwd: str) -> bool:
    """
    This function checks the validity of a password based on the following rules:
    - At least 1 lowercase letter [a-z]
    - At least 1 uppercase letter [A-Z]
    - At least 1 number [0-9]
    - At least 1 special character [$#@]
    - Minimum length: 6 characters
    - Maximum length: 16 characters
    """
    return (6 <= len(passwd) <= 16 and
            all(re.search(pattern, passwd) for pattern in [r"[a-z]", r"[A-Z]", r"\d", r"[$#@]"]))

passwd = input("Enter your password: ")

print("!!! Password is valid !!!" if pass_check(passwd) else "XXX Password is invalid XXX")