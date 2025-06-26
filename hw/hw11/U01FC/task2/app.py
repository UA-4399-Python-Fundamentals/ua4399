def check_weekday(number):
    try:
        if not isinstance(number, (int, float)):
            raise ValueError
        if number < 1 or number > 7:
            raise ValueError
        else:
            weekdays = {
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
            }
            return weekdays[number]
    except ValueError:
        return "Value should be a number 1-7"
    
print(check_weekday(1))
print(check_weekday(0))
print(check_weekday(7))
print(check_weekday(8))
print(check_weekday(-8))
print(check_weekday("8"))
print(check_weekday("S"))