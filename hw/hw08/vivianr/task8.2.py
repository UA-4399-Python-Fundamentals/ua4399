def password_is_valid(password):
    return (6 <= len(password) <= 16 and
            any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in ['$', '#', '@'] for char in password))

password = input("Enter a password: ")
if password_is_valid(password):
    print("Valid password")
else:
    print("Invalid password")