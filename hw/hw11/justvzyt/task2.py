days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

number = input("Day number: ")

try:
    number = int(number)

    if number < 1 or number > 7:
        raise ValueError("You should have chosen a number from 1 to 7!")
    print(days[number-1])
except ValueError as e:
    print(e)