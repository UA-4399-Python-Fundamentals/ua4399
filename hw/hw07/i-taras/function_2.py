################################################################### Jenny's secret message ###################################################################

# def secret_message(name: str) -> str:
#     if name == 'Johnny':
#         return f"Hi, Johnny ❤️❤️❤️"
#     else:
#         return(f"Hello my friend {name}")

# greeting = input("Call your name: ")
# print(secret_message(greeting))


############################################################ Find The Distance Between Two Points ############################################################

# def calculate(x1: float, y1: float, x2: float, y2: float) -> float:
#     return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
        

# print(calculate(9, 15, 4, 7))


######################################################################### No yelling!##########################################################################

# def filter_words(some_str: str) -> str:
#     words = some_str.lower().split()
#     words[0] = words[0].capitalize()
#     return ' '.join(words)

# bad_str = input('Give text: ')
# print(filter_words(bad_str))


################################################################ Convert a Number to a String! ################################################################

# def num_str(num: int) -> str:
#     return str(f"'{num}'") # '' - це для виводу!

# print(type(num_str(55)))
# print(num_str(55))


################################################################# Reversing Words in a String #################################################################

# def reversing(normal_str: str) -> str:
#     revers_str = normal_str.split()
#     revers_str.reverse()
#     return ' '.join(revers_str)

# print(reversing("Hello World"))


##################################################################### Reverse List Order #####################################################################

# def revers_list(normal_list: list) -> list:
#     return normal_list[::-1]

# print(revers_list([4, 9, 43, 24]))


##################################################################### Multiples of 3 or 5 #####################################################################

# def multiples(num: int) -> int:
#     if num < 0:
#         return 0
#     total = 0
#     for i in range(num):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total

# print(multiples(1000))


###################################################################### Will you make it? ######################################################################

# def way(mile: float, gallon: float, miles_per_gallon: float = 25) -> bool:
#     if gallon * miles_per_gallon >= mile:
#         return True
#     else:
#         return False
    
# print(way(49, 2))


################################################################### Are You Playing Banjo? ###################################################################

# def banjo(name: str) -> str:
#     if name[0].lower() == 'r':
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"

# word = input("Are you playing banjo? ")
# print(banjo(word))


###################################################### Convert boolean values to strings 'Yes' or 'No'. ######################################################

# def convert_bool(value: bool) -> str:
#     if value == True:
#         return 'Yes'
#     else:
#         return 'No'

# print(convert_bool(True))
# print(convert_bool(False))


###################################################################### Counting sheep... ######################################################################

# def count_sheep(array: list) -> int:
#     sheeps = 0
#     for sheep in array:
#         if sheep:
#             sheeps += 1
#     return sheeps

# print(count_sheep([True,  True,  7,  False, True,  None,  True,  'True' , True,  False, True,  False, 0,  False, False, True , True,  True, 
#                   True,  '',     False,  False, True,  True]))


###################################################################### Is this my tail? ######################################################################

def body_tail(body: str, tail: str) -> bool:
    if body[-1] == tail[0]:
        return True
    else:
        return False
    
print(body_tail('taiger', 'roolf'))