age = float(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("You can't have age below zero!")
    print("Even" if age % 2 == 0 else "Odd")
except ValueError as e:
    print(e)