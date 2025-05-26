def day_of_weel(day_number:int):
    if not 1 < day_number < 7:
        raise OutOfRangeDayOfWeekError("Week has only seven days, you can use numbers between 1 and 7")
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return  days[day_number]

print(day_of_weel(int(input())))