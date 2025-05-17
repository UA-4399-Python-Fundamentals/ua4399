#1 
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
    
#2  
import math
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)

#3 
def filter_words(input_str):
    words = input_str.split()
    formatted_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    return " ".join(formatted_words)

#4 
def number_to_string(num):

    return str(num)

#5 
def reverse(st):
    words = st.split()
    
    reversed_words = words[::-1]
    
    return " ".join(reversed_words)

#6 
def reverse_list(l):
    return l[::-1]

#7 
def solution(number):
    if number < 0:
        return 0

    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

#8 
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#9 
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
#10 
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#11 
def count_sheeps(sheep):
   
    return sum(1 for s in sheep if s is True)

#12 
def correct_tail(body, tail):
    return body[-len(tail):] == tail