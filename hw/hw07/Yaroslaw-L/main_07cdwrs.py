#1 Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    
#2 Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)

#3 No yelling!
def filter_words(st):
    st = " ".join(st.split())
    return st.capitalize()

#4 Convert a Number to a String
def number_to_string(num):
    return str(num)

#5 Reversing Words in a String
def reverse(st):
    return ' '.join(reversed(st.split()))

#6 Reverse List Order
def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]

#7 Multiples of 3 or 5
def solution(number):
    result=0
    for each in range(1, number):
        if each % 3 ==0 or each % 5 ==0:
            result += each
    return result 

#8 Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump/mpg <= fuel_left:
        return True
    else:
        return False
    
#9 Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == 'r' else f"{name} does not play banjo"

#10 Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#11 Counting sheep...
def count_sheeps(sheep):
    return sum(1 for i in sheep if i)

#12 def correct_tail(body, tail):
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail[0]:
        return True
    else:
        return False
