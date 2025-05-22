# Task2.
# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

password = input("Enter password:")

def validation1(password):
    if re.search(r"[a-z]", password):
        print("Lower case: True")
    else:
        print("Lower case: False")

def validation2(password):
    if re.search(r"[A-Z]", password):
        print("Upper case: True")
    else:
        print("Upper case: False")

def validation3(password):
    if re.search(r"[0-9]", password):
        print("Numbers: True")
    else:
        print("Numbers: False")

def validation4(password):
    if re.search(r"[$#@]", password):
        print("Special case: True")
    else:
        print("Special case: False")

def validation5(password):
    if len(password) >= 6:
        print("Min len: True")
    else:
        print("Min len: False")

def validation6(password):
    if len(password) <= 16:
        print("Max len: True")
    else:
        print("Max len: False")

validation1(password)
validation2(password)
validation3(password)
validation4(password)
validation5(password)
validation6(password)


