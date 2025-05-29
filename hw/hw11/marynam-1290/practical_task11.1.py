# 1

user_age = input("Please, enter your age: ")


def even_odd(user_age):
    user_age = int(user_age)
    if user_age < 0:
        raise ValueError("Number must be non-negative")
    elif user_age % 2 == 0:
        print("The age number is even")
    else:
        print("The age number is odd")


even_odd(user_age)
