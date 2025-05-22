# I. Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

# II. Find The Distance Between Two Points

import math
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)


# III. No yelling!

def filter_words(st):
    # Split the string by whitespace, remove extras
    words = st.split()
    
    # Lowercase all words, capitalize first one
    words = [word.lower() for word in words]
    words[0] = words[0].capitalize()
    
    # Join them back into a string
    return ' '.join(words)

# IV. Convert a Number to a String

def number_to_string(num):
    string = str(num)
    return string

# V. Reversing Words in a String

def reverse(st):
    words = st.split()          
    reversed_words = words[::-1]
    st = ' '.join(reversed_words)
    return st

# VI. Reverse List Order

def reverse_list(l):
    reversed_list = l[::-1]
    return reversed_list


# VII. Multiples of 3 or 5

def solution(number):
    if number < 0:
        return 0
    
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False

# IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    if boolean is True:
        return "Yes"
    else:
        return "No"

# XI. Counting sheep

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count

# XII. Is this my tail?

def correct_tail(body, tail):
    return body[-len(tail):] == tail