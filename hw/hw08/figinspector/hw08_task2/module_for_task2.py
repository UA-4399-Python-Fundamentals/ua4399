import re


def check_password(password):
    """
    Password checker function
    """

    return (
        6 <= len(password) <= 16
        and re.search(r"[a-z]", password)
        and re.search(r"[A-Z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[$#@]", password)
    )
