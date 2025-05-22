''' Homework 05 task 1.1'''
#Task
#Create a list that contains elements of integer type, then use
#the loop to change the type of these elements to a floating type.
#(Hint: use the built-in float () function).

numbers_list = list(range(21))

for item in range(len(numbers_list)):
    print(f"before type of '{numbers_list[item]}' was {type(numbers_list[item])}",end="")
    numbers_list[item]=float(numbers_list[item])
    print(f"and now type of '{numbers_list[item]}' are {type(numbers_list[item])}", end="\n")

