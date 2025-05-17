#Task 1 Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, " + name + "!"
name_input = input("Enter your name: ")
print(greet(name_input))
        #Task 2 Find The Distance Between Two Points
import math
def distance(p1, p2):
    return round(math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2), 2)
print(distance((1, 2), (4, 6)))
# Task 3  No yelling!
def filter_words(st):
    words = st.split()
    if words:
        words[0] = words[0].capitalize()
        for i in range(1, len(words)):
            words[i] = words[i].lower()
    result = words[0] if words else ""
    for word in words[1:]:
        result += " " + word
    return result
print(filter_words("WOW this is REALLY          amazing"))
print(filter_words("HELLO CAN YOU HEAR ME"))
print(filter_words("now THIS is REALLY interesting"))
# Task 4 Convert a Number to a String
def number_to_string(num):
    return f"{num}"
user_input = input("Enter an integer: ")
number = int(user_input)
result = number_to_string(number)
print("String output:", result)
# Task 5 Reversing Words in a String
def reverse_words(st):
    words = st.split()
    result = ""
    for i in range(len(words) - 1, -1, -1):
        if result:
            result += " " + words[i]
        else:
            result = words[i]
    return result
print(reverse_words("Hello World"))
# Test 6 Reverse List Order
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4]))
# Test 7 Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i  # Add it to the sum
    return total
print(solution(10))
# Test 8 Will you make it?
def can_reach_pump(distance, miles_per_gallon, gallons_left):
    max_distance = miles_per_gallon * gallons_left
    return max_distance >= distance
print(can_reach_pump(50, 25, 2))
print(can_reach_pump(60, 25, 2))
# Test 9 Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
print(are_you_playing_banjo("Ringo"))
print(are_you_playing_banjo("John"))
print(are_you_playing_banjo("roger"))
print(are_you_playing_banjo("Paul"))
print(are_you_playing_banjo("Ringo"))
print(are_you_playing_banjo("John"))
# Task 10 Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
print(bool_to_word(True))
print(bool_to_word(False))
# Task 11 Counting sheep
def count_sheep(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count
sheep_list = [
    True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
]
print(count_sheep(sheep_list))
# Task 12 Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail
print(correct_tail("elephant", "t"))
print(correct_tail("giraffe", "e"))
print(correct_tail("lion", "x"))