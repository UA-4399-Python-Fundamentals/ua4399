user_pass = input("Enter your password: ")


def pass_valid(user_pass):
    if not (16 >= len(user_pass) >= 6):
        print("Password is not valid")
        return
    lower = False
    upper = False
    digit = False
    special = False
    for character in user_pass:
        if character.islower():
            lower = True
        elif character.isupper():
            upper = True
        elif character.isdigit():
            digit = True
        elif character in ["$", "#", "@"]:
            special = True
    if not (lower and upper and digit and special):
        print("Password is invalid")
        return
    print("Password is valid")


pass_valid(user_pass)
