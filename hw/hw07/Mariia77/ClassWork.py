def factorial(in_data):
    if in_data == 1:
        return 1
    return factorial(in_data-1)*in_data
print(factorial(3))