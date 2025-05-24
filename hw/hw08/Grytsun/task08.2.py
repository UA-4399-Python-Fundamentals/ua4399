import re

def validate_password(password):
 
    if len(password) < 6 or len(password) > 16:
        return "Invalid password: Length must be between 6 and 16 characters."

    if not re.search("[a-z]", password):
        return "Invalid password: Must contain at least one lowercase letter."


    if not re.search("[A-Z]", password):
        return "Invalid password: Must contain at least one uppercase letter."

  
    if not re.search("[0-9]", password):
        return "Invalid password: Must contain at least one digit."


    if not re.search("[$#@]", password):
        return "Invalid password: Must contain at least one special character ($, #, or @)."

    return "Password is valid."


password = input("Enter your password: ")
print(validate_password(password))