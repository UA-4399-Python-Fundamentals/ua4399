def check_age(age):
    if age < 0:
        raise ValueError('Enter a positive number')
    if age % 2 == 0:
        return 'Age is even'
    else:
        return 'Age is odd'
try:
    age = int(input('Enter your age: '))
    result = check_age(age)
    print(result)
except ValueError as e:
    print(e)