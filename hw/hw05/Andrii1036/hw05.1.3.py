''' Homework 05 task 1.3'''
#Task
#Write a script that will calculate the factorial of the entered
#number without using recursion.
#Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, ….

#Declared constanta
ZERO_FACTORIAL = 1

#Declared variable
value_to_factorial = None

#Getting and validating user input
while value_to_factorial == None:
    input_value = input('Please enter the number to calculate the factorial of: ')
    if input_value.isdigit():
        value_to_factorial=int(input_value)
    else:
        print("Please use only numeric symbol")
            
#calculate the factorial of the entered number
def calculate_factorial (number):
    multiplier = 1
    finish_calculate = 1
    if number == 0:
        finish_calculate = ZERO_FACTORIAL
        #print(f"Factorial of '0' are {ZERO_FACTORIAL}")
    else:
        while multiplier <= number:
            finish_calculate *=multiplier
            multiplier+=1
    print(f"Factorial of {number} are {finish_calculate}")

calculate_factorial (value_to_factorial)