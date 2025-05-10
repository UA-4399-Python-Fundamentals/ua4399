# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# Simple: Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dist, 2)


# No yelling!
def filter_words(st):
    long_st = st.lower().capitalize()
    return ' '.join(long_st.split())


# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# Reversing Words in a String
def reverse(st):
    my_list = st.split()
    my_list.reverse()
    return ' '.join(my_list)


# Reverse List Order
def reverse_list(l):
    l.reverse()
    return l


# Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0

    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    

# Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)


# Is this my tail?
def correct_tail(body, tail):
    if body[- 1] == tail:
        return True
    else:
        return False
