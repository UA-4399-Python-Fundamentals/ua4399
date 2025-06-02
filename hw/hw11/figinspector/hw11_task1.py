def check_age(age):
    if age < 0:
        raise ValueError('Age cannot ba negative')
    if age % 2 == 0:
        print('Your age is even')
    else:
        print('Your age is add')

try:
    user_input = input('Enter your age: ')
    age = int(user_input)
    check_age(age)
except ValueError as e:
    print(f"Invalid input:", e)