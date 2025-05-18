def largest(a, b):
    """function that returns the largest number of two numbers"""
    if len(a) > len(b):
        return a
    else:
        return b

print(largest('asd','sdfsdf'))

def max_of_two(a, b):
    """function that returns the max number of two numbers"""
    return max(a,b)
print(max_of_two('asd','sdfsdf'))