# Homework Lesson 08

# ///////////////////////////////////////////////////////////////////
# 2 - Validity of a password
print("Subtask 2")

import re

def validate_password(passwd):
    return 6 <= len(passwd) <= 16 and re.search(r"[a-z]", passwd) and re.search(r"[A-Z]", passwd) and re.search(r"\d", passwd) and re.search(r"[$#@]", passwd)


passwd = input("Enter your password: ")

if validate_password(passwd):
    print("Validation is correct.")
else:
    print("Error! Try again.")
