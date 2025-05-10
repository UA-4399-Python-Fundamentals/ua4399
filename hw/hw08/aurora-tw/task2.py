import re

def check_pass(password):
    password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$@#]).{6,16}$')
    return "Welcome!" if password_pattern.match(password) else "Invalid password"

print(check_pass(input("Enter password")))