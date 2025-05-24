''' task 1.1 from HW06'''
#In the range from 1 to 10 determine 
#-even numbers thatare divisible by 2, 
#-odd numbers, witch are divisble by 3, 
#-numbers that are not divisible by 2 and 3

# Declaring variables
numbers_range = list(range(1,11))

# Function that returns specific numbers:
def specific_numbers(numbers, condition):    
    '''The first argument is a list of numbers.
    The second argument determines which numbers we want:

    If the second argument is a number, the function returns all numbers divisible by that number.

    If the second argument is the word "not", the function returns all numbers that are not divisible by 2 or 3.'''

    if condition == "not":
        not_numbers = list(filter(lambda item : item % 2 != 0 and item % 3 != 0, numbers))
        print(not_numbers)
    elif isinstance(condition, int):
        numbers_need = list(filter(lambda item : item % condition == 0, numbers ))
        print(numbers_need)
    else:
        print("Something wrong")

# Display results
specific_numbers(numbers_range, 2)
specific_numbers(numbers_range, 3)
specific_numbers(numbers_range, "not")
specific_numbers(numbers_range, 5)
specific_numbers(numbers_range, "hello")
        