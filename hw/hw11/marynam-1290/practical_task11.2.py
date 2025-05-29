# 2
user_number = input("Enter your number: ")

week_days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def specified_day(user_number):
    if not user_number.isdigit():
        raise ValueError("Input is not numeric")
    else:
        user_number = int(user_number)
        if 1 <= user_number <= 7:
            print(week_days.get(user_number))
        else:
            print("Please, enter the number between 1 and 7")


specified_day(user_number)
