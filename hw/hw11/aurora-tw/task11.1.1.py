run = True

def init():
    global run
    age = input("Enter your age: ")
    try:
        result = f"Your age is an {check_if_odd_or_even_age(int(age))} number"
    except ValueError:
        return "Please enter a positive integer"
    else:
        run = False
        return result


def check_if_odd_or_even_age(age):
    if not isinstance(age,int) or age < 0:
        raise ValueError
    else:
        return "even" if age%2==0 else "odd"

while run:
    print(init())