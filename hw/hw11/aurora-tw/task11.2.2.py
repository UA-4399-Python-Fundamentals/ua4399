run = True

def init():
    global run
    number = input("Enter the number between 1 and 7: ")
    try:
        result =  f"Day of the week is {get_day_of_the_week_by_number(int(number))}"
    except ValueError:
        return "Please enter a number between 1 and 7"
    else:
        run = False
        return result

def get_day_of_the_week_by_number(number):
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if not isinstance(number,int) or number not in range(1,8):
        raise ValueError
    else:
        return days[number-1]

while run:
    print(init())