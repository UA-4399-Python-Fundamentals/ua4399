def largest_number(num1,num2):
    """
    This function takes two numbers and returns the largest of them.
    """
    if num1>=num2:
        return num1
    elif num2>=num1:
        return num2
print(largest_number(10,100))  