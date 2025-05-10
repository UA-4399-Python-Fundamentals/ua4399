#Jenny's secret message
def greet(name):
    return "Hello, my love!" if name == "Johny" else f"Hello, {name}!"

#Find The Distance Between Two Points
import math
def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2)),2)

#No yelling!
def filter_words(st):
    result = st.capitalize()
    return " ".join(result.split())

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Reversing Words in a String
def reverse(st):
    a = st.split(" ")
    a.reverse()
    return  " ".join(a)

# Reverse List Order
def reverse_list(l):
  l.reverse()
  return l

#Multiples of 3 or 5
def solution(number):
    result = 0
    if number < 0:
        return 0
    for x in range(1, number):
        if x%3==0 or x%5==0:
            result += x
    return result

#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    result = True if mpg*fuel_left >= distance_to_pump else False
    return result

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    result = f"{name}"
    if name.lower()[0]=="r":
        result += " plays banjo"
    else:
        result += " does not play banjo"
    return result

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return 'Yes' if boolean==True else 'No'

#Counting sheep...
def count_sheeps(sheep):
    present = 0
    for x in sheep:
        if x:
            present += 1
    return present

#Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    return True if sub == tail else False
