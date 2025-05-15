password = input("Enter password: ")

special_chars = "$#@"

if (6 <= len(password) <= 16 and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in special_chars for c in password)):
    print("Password is valid")
else:
    print("Password must be 6–16 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character from [$#@]")