##task1
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError
except ValueError:
    print("Age should be a positive number")
else:
    if is_even(age):
        print ("Even")
    else:
        print("Odd")

##task2
days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

try:
    n = input("Enter number: ")
    if not n.isdigit() or (int(n) > 7 or int(n) <= 0):
        raise ValueError
except ValueError:
    print("Enter a number from 1 to 7")
else:
    print(f"Day: {days[int(n)]}")