days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def process_number(user_input):
    if 1 <= user_input <= 7:
        print(days[user_input])
    else:
        raise ValueError("Number must be between 1 and 7")

try:
    user_input = int(input('Enter number (1–7): '))
    process_number(user_input)
except ValueError as e:
    print("Error:", e)
