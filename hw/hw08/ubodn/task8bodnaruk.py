# Task 2

import re

password = input("Enter your password: ")

pattern = r"""^(?=.*[a-z])      # at least one lowercase
              (?=.*[A-Z])      # at least one uppercase
              (?=.*\d)         # at least one digit
              (?=.*[$#@])      # at least one special char
              [A-Za-z\d$#@]{6,16}$  # only allowed chars, and length
           """

if re.match(pattern, password, re.VERBOSE):
    print("✅ Password is valid!")
else:
    print("❌ Password is invalid.")
