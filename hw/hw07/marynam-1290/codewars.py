# 1 Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# 2 Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# 3 No yelling!
def filter_words(st):
    st = " ".join(st.split())
    return st.capitalize()


# 4 Convert a Number to a String
def number_to_string(num):
    pass  # Return a string of the number here!
    return str(num)


# 5 Reversing Words in a String
def reverse(st):
    st = st.split()
    st = reversed(st)
    return " ".join(st)


# 6 Reverse List Order
def reverse_list(l):
    "return a list with the reverse order of l"
    return l[::-1]


# 7 Multiples of 3 or 5
def solution(number):
    pass
    natural_numbers = list(range(1, number))
    sum = 0
    for num in natural_numbers:
        if num % 3 == 0:
            sum += num
            continue
        elif num % 5 == 0:
            sum += num
    return sum


# 8 Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_left = mpg * fuel_left
    if distance_left >= distance_to_pump:
        return True
    else:
        return False


# 9 Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# 10 Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"


# 11 Counting sheep...
def count_sheeps(sheep):
    number_of_sheeps = 0
    for i in sheep:
        if i == True:
            number_of_sheeps += 1
        else:
            number_of_sheeps += 0
    return number_of_sheeps


# 12 Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == str(tail):
        return True
    else:
        return False
