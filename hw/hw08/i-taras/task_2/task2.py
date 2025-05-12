
def check_len_password(signs: str) -> bool:
    if 16 >= len(signs) >= 6:
        return True
    else:
        return False
    

def check_lower_upper_signs(signs: str) -> bool:
    has_lower = False
    has_upper = False
    for sign in signs:
        if sign.islower():
            has_lower = True
        elif sign.isupper():
            has_upper = True
        if has_upper and has_lower:
            break

    return has_lower and has_upper


def check_number(signs: str) -> bool:
    has_number = False
    for sign in signs:
        if sign.isdigit():
            has_number = True
            break

    return has_number


def check_special_signs(signs: str) -> bool:
    special_signs = '$#@'
    has_special_signs = False
    for sign in signs:
        if sign in special_signs:
            has_special_signs = True
            break

    return has_special_signs


def is_valid_password(password: str) -> str:
    len_passwor = check_len_password(password)
    l_w_signs = check_lower_upper_signs(password)
    number = check_number(password)
    special = check_special_signs(password)
    if len_passwor and l_w_signs and number and special:
        return 'Your password is strong'
    else:
        return "Your password is not secure"


password = input("Enter your password: ")
print(is_valid_password(password))
