import re

password = input("Enter password: ")
if len(re.findall("[a-z]", password)) > 0 and len(re.findall("[A-Z]", password)) > 0 and len(re.findall("[0-9]", password)) > 0 and len(re.findall("$|#|@", password)) > 0 and len(password) >= 6 and len(password) <= 16:
    print("Valid")
else:
    print("Not valid")