def check_password(password):
    import re
    if len(password) < 6 or len(password) > 16:
        print("Password length is valid")
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*]', password):
        return False
    print("Password is true")
    return True 

