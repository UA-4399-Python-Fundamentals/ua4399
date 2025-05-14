''' Homework 05 task 1.2'''
#Task
#Task2. Print Fibonacci numbers up to the entered number n,
#using cycles.
#(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

#Declared the constanta
FIRST_FIBONACCI_NUMBER=0
SECOND_FIBONACCI_NUMBER=1

#Declared the variable
length_list = None 

#Getting and validating user input
while length_list == None:
    input_value = input("Please input Length of the Fibonacci list: ")
    if input_value.isdigit():
        if int(list(input_value)[0]) == 0:
            print("Dont use ZERO") 
        else:
            length_list=int(input_value)
    else:
        print("Please input Length of the Fibonacci list and use only numeric symbol")
        
#Generetated Fibonacci numbers
def fibonacci_generator (length):
    index = 2
    fibonacci_list=[FIRST_FIBONACCI_NUMBER,SECOND_FIBONACCI_NUMBER]
    while index<length:
        next_fibonacci_number = fibonacci_list[index-1] + fibonacci_list[index-2]
        fibonacci_list.append(next_fibonacci_number)
        index+=1
    print(fibonacci_list)

fibonacci_generator(length_list) 
